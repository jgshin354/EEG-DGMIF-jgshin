# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:19:39 2020

@author: JGSHIN

refer the TDT python package https://www.tdt.com/support/python-sdk/
"""
#%%
import os
#import glob
import numpy as np
from scipy.interpolate import interp1d
import scipy.ndimage
import matplotlib.pyplot as plt
import tdt
#from tdt import read_block, read_sev, epoc_filter, download_demo_data
import mne
import pywt
import dill
#pywt.wavelist()

#vrange = [0,1e-4]
plt.rcParams["figure.figsize"] = [8.6, 6.4]
vrange = [-16,-10]
denoising_epocdiv_flag = True
subpoint_intp_epocdiv_flag = True
epoc_time_des = 8 ## desired epoc time window = plus minus 5 seconds
stft_pts = 768

# Harender, and R. K. Sharma. “EEG Signal Denoising Based on Wavelet Transform.” 
# In 2017 International Conference of Electronics, Communication and Aerospace Technology (ICECA), 
# 758–61. Coimbatore: IEEE, 2017. https://doi.org/10.1109/ICECA.2017.8203645.
def wav_hardth(din):
    din_p = 1*din
    din_th = np.std(din)*1.504
    din_p[np.where(abs(din_p) > abs(din_th))] = din_th * np.sign(din_p[np.where(abs(din_p) > abs(din_th))])
    return din_p
def wav_denoising(data_in):
    import pywt    
    #pywt.wavelist()
    import numpy as np
    coeffs = pywt.wavedec(data_in, 'sym5', mode='cpd', level=10)
    coeffs_p = 1*coeffs

    coeffs_p[0] = wav_hardth(coeffs_p[0])
    coeffs_p[1] = wav_hardth(coeffs_p[1])
    coeffs_p[2] = wav_hardth(coeffs_p[2])
    coeffs_p[3] = wav_hardth(coeffs_p[3])    
    coeffs_p[4] = wav_hardth(coeffs_p[4])    
    coeffs_p[5] = wav_hardth(coeffs_p[5])    
    coeffs_p[6] = wav_hardth(coeffs_p[6])
    coeffs_p[7] = wav_hardth(coeffs_p[7])

    coeffs_p[8] = wav_hardth(coeffs_p[8])
    #coeffs_p[8] = np.zeros(coeffs_p[8].shape)  
    #coeffs_p[9] = wav_hardth(coeffs_p[9])
    coeffs_p[9] = np.zeros(coeffs_p[9].shape)
    #coeffs_p[10] = wav_hardth(coeffs_p[10])    
    coeffs_p[10] = np.zeros(coeffs_p[10].shape)
    
    dout = pywt.waverec(coeffs_p,'sym5')
    return dout
    

#import seaborn

#%%

#base_path = "D:\\DGMIF\\Work\\2. Photobiomodulation\\20200514_coding_test"
#base_path = "E:\\DGMIF\\EEG\\20200428\\EEG_200428-200428"
#base_path = "E:\\DGMIF\\EEG_proc"
base_path = "D:\\Backup\\DGMIF_data\\002_photobiomodulation\\EEG_proc"
path_list = os.listdir(base_path)
d_format = "i16"
d_scale_factor = 1e6
data = tdt.StructType()        
data.data = tdt.StructType()
data.time = tdt.StructType()
data.info = tdt.StructType()
tmp = tdt.StructType()

for file_path in path_list:
    data_path =  base_path + "\\" + file_path 
    if os.path.isdir(data_path) == 1:
        plt.close('all')
        data_read = tdt.read_block(data_path)
        data.info.fs = data_read.streams.Wav1.fs
        data.info.ch = data_read.streams.Wav1.data.shape[0]
        data.info.pts = data_read.streams.Wav1.data.shape[1]
        data.info.active_time = 1/data.info.fs * data.info.pts
        data.data.Wav1 = data_read.streams.Wav1.data
        data.data.EEGG = data_read.streams.EEGG.data
        data.time.timestamp = np.linspace(0,data.info.pts-1,data.info.pts)/data.info.fs
        data.time.trigger_edge = data_read.epocs.PrtA.onset
        data.time.trigger_timestamp = np.zeros(len(data.time.timestamp))
        tmp.trigger_index = []
        data.time.rising_index = []        
        tmp.trig_disp_ampl = np.max(abs(data.data.EEGG),1)/2
        
        ## find trigger index (prt1 changes) position in EEG signal /  data.time.trigger_edge is timestamp of trigger edges
        for onset_time_div in data.time.trigger_edge:
            tmp.tmp = abs(data.time.timestamp-onset_time_div)
            tmp.trigger_index = np.concatenate((tmp.trigger_index, np.argmin(tmp.tmp)), axis = None)
        
        ## Divide the rising and falling edges on the trigger point of Prt1
        for onset_time_div in range(0,int(np.floor(len(tmp.trigger_index)/2))):
            tmp.rising_index = int(tmp.trigger_index[int(2*onset_time_div)])
            tmp.falling_index = int(tmp.trigger_index[int(2*onset_time_div)+1])
            data.time.trigger_timestamp[tmp.rising_index:tmp.falling_index] = 1
            data.time.rising_index = np.concatenate((data.time.rising_index, tmp.rising_index), axis = None)
        
        ## STFT, 768 PTS windowing
        data.data.stft_EEGG = mne.time_frequency.stft(data.data.EEGG, stft_pts)        
        
        ## plot time-amplitude graph
        plt.figure(1)
        for data_ch in range(0, data.info.ch):
            plt.subplot(data.info.ch, 1, data_ch+1)
            plt.plot(data.time.timestamp, data.data.EEGG[data_ch,:])
            plt.plot(data.time.timestamp, data.time.trigger_timestamp * tmp.trig_disp_ampl[data_ch])
            if data_ch==0:
                plt.title('time-amplitude plot')
        plt.gcf().canvas.draw()
        plt.imsave("001_time-amplitude_" + file_path + "_.png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')
       
        ## plot 2D STFT chart
        plt.figure(2)
        for data_ch in range(0, data.info.ch):            
            plt.subplot(data.info.ch/3, 3, data_ch+1)
            plt.imshow(np.flipud(np.squeeze(np.log(abs(data.data.stft_EEGG[data_ch,:,:])))),vmin = vrange[0], vmax = vrange[1], extent =[0,data.info.active_time,0,data.info.fs/2])
            plt.ylim([0, 160])
            plt.title('STFT, Ch' + str(data_ch))
            plt.ylabel('Hz')
            plt.xlabel('time(s)')
        plt.gcf().canvas.draw()
        plt.imsave("002_STFT_" +file_path + "_.png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')
        
        ## Denoising based wavelet transform
        data.data.wavEEGG = np.zeros(data.data.EEGG.shape)
        for data_ch in range(0,data.info.ch):
            data.data.wavEEGG[data_ch,:] = wav_denoising(data.data.EEGG[data_ch,:])
        
        ## Plot denoised time-amplitude chart       
        tmp.trig_disp_ampl_denoise = np.max(abs(data.data.wavEEGG),1)/2            
        plt.figure(3)            
        for data_ch in range(0, data.info.ch):
            plt.subplot(data.info.ch, 1, data_ch+1)
            plt.plot(data.time.timestamp, data.data.wavEEGG[data_ch,:])
            plt.plot(data.time.timestamp, data.time.trigger_timestamp * tmp.trig_disp_ampl_denoise[data_ch])            
            if data_ch==0:
                plt.title('time-amplitude plot, wavelet denoised')
        plt.gcf().canvas.draw()
        plt.imsave("003_WaveletDenoising_time-amplitude_" + file_path + "_.png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')
      
        ## Plot denoised STFT chart
        data.data.stft_wavEEGG = mne.time_frequency.stft(data.data.wavEEGG, stft_pts)        
        plt.figure(4)
        for data_ch in range(0, data.info.ch):            
            plt.subplot(data.info.ch/3, 3, data_ch+1)
            plt.imshow(np.flipud(np.squeeze(np.log(abs(data.data.stft_wavEEGG[data_ch,:,:])))),vmin = vrange[0], vmax = vrange[1], extent =[0,data.info.active_time,0,data.info.fs/2])
            #plt.imshow(np.flipud(np.squeeze((abs(data.data.stft_wavEEGG[data_ch,:,:])))),vmin = vrange[0], vmax = vrange[1], extent =[0,data.info.active_time,0,data.info.fs/2])
            plt.ylim([0, 160])
            plt.title('STFT,Denoised,Ch' + str(data_ch))
            plt.ylabel('Hz')
            plt.xlabel('time(s)')            
        plt.gcf().canvas.draw()
        plt.imsave("004_WaveletDenoising_STFT_" + file_path + "_.png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')

        ## plot Extracted noise
        extracted_noise = data.data.stft_EEGG-data.data.stft_wavEEGG
        plt.figure(5)
        for data_ch in range(0, data.info.ch):            
            plt.subplot(data.info.ch/3, 3, data_ch+1)
            plt.imshow(np.flipud(np.squeeze(np.log(abs(extracted_noise[data_ch,:,:])))),vmin = vrange[0], vmax = vrange[1], extent =[0,data.info.active_time,0,data.info.fs/2])
            plt.ylim([0, 160])
            plt.title('Noise,Ch' + str(data_ch))
            plt.ylabel('Hz')
            plt.xlabel('time(s)') 
        plt.gcf().canvas.draw()
        plt.imsave("005_ExtractedNoise_STFT_" + file_path + "_.png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')
        
        
        
        #extract time difference between sampling time and Prt1 onset time
        data.time.prt1_onset = data_read.epocs.PrtA.onset[np.where(data_read.epocs.PrtA.data != 0)]
        data.time.smp_onset = np.zeros(data.time.prt1_onset.shape)
        for onset_n in range(0, data.time.prt1_onset.size):
            data.time.smp_onset[onset_n] = data.time.timestamp[int(data.time.rising_index[onset_n])]
                        
        ## epoc division data representation
        ## The first and the last epoc data cannot be used due to lack of sampling time

        pts_des = int(epoc_time_des * data.info.fs)
        data.data.epoc_div = np.zeros([data.info.ch, data.time.rising_index.size-2, pts_des*2])
        data.data.epoc_div_intp = np.zeros([data.info.ch, data.time.rising_index.size-2, pts_des*2])
        
        if denoising_epocdiv_flag == True:
            tmp.epoc_div = data.data.wavEEGG
        else:
            tmp.epoc_div = data.data.EEGG
            
        if subpoint_intp_epocdiv_flag == True:            
            for data_ch in range(0,data.info.ch):
                for epoc_iter in range(1,data.time.rising_index.size-1):
                    data.data.epoc_div[data_ch, epoc_iter-1, :] = tmp.epoc_div[data_ch,int(data.time.rising_index[epoc_iter]-pts_des):int(data.time.rising_index[epoc_iter]+pts_des)]
            ############ subsample interpolation for jitter compensation
            for data_ch in range(0,data.info.ch):
                for epoc_iter in range(1,data.time.rising_index.size-1):
                    tmp.data = tmp.epoc_div[data_ch,int(data.time.rising_index[epoc_iter]-pts_des-1):int(data.time.rising_index[epoc_iter]+pts_des+1)]
                    tmp.intpind = np.arange(data.time.rising_index[epoc_iter]-pts_des-1,data.time.rising_index[epoc_iter]+pts_des+1)
                    tmp.intpind_new = np.arange(data.time.rising_index[epoc_iter]-pts_des,data.time.rising_index[epoc_iter]+pts_des)  \
                                        +((data.time.prt1_onset[epoc_iter] - data.time.smp_onset[epoc_iter])/(1/data.info.fs)) #index + ((prt1 - smp) / T )
                    tmp.intp = interp1d(tmp.intpind, tmp.data, kind='cubic')
                    data.data.epoc_div_intp[data_ch,epoc_iter-1,:] = tmp.intp(tmp.intpind_new)
            data.data.epoc_div_ret = data.data.epoc_div_intp
        else:
            for data_ch in range(0,data.info.ch):
                for epoc_iter in range(1,data.time.rising_index.size-1):
                    data.data.epoc_div[data_ch, epoc_iter-1, :] = tmp.epoc_div[data_ch,int(data.time.rising_index[epoc_iter]-pts_des):int(data.time.rising_index[epoc_iter]+pts_des)]                    
            data.data.epoc_div_ret = data.data.epoc_div


        #plot epoc division time-amplitude chart                            
        plt.figure(6)
        data.data.epoc_timestamp = np.linspace(np.float64(-pts_des)*(1/data.info.fs),np.float64(pts_des)*(1/data.info.fs)-(1/data.info.fs),2*pts_des)
        for data_ch in range(0, data.info.ch):       
            plt.subplot(data.info.ch/3, 3, data_ch+1) 
            plt.plot(data.data.epoc_timestamp,np.transpose(data.data.epoc_div[data_ch,:,:],(1,0)))
            plt.grid(True)
            plt.title('all epocs,Ch' + str(data_ch))

        plt.gcf().canvas.draw()
        plt.imsave("006_all_channel_time-amplitude_" + file_path + ".png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')

        
        #plot subpixel registration result
        if subpoint_intp_epocdiv_flag == True:   
            plt.figure(7)
            plt.plot(data.data.epoc_div[0,0,:])
            plt.plot(data.data.epoc_div_intp[0,0,:])
            plt.xlim(pts_des-32,pts_des+32)
            plt.legend(('sampled signal','interpolated, compensated signal'))        
            plt.title('example of jitter compensated result')
            plt.gcf().canvas.draw()
            plt.imsave("007_subpixel_compensation-interpolation_" + file_path + ".png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')

        
        #averaging 
        data.data.epoc_div_avg = np.average(data.data.epoc_div_ret,1)
        plt.figure(8)
        for data_ch in range(0, data.info.ch):
            plt.subplot(data.info.ch, 1, data_ch+1)
            plt.plot(data.data.epoc_timestamp, data.data.epoc_div_avg[data_ch,:],linewidth=0.3)
            plt.ylim([np.min(data.data.epoc_div_avg), np.max(data.data.epoc_div_avg)])
            if data_ch==0:
                plt.title('time-amplitude plot/averaged')
        plt.gcf().canvas.draw()
        plt.imsave("008_time-amplitude_avg_intp_" + file_path + "_.png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')        
        
        # STFT
        ## Plot denoised STFT from denoised/averaged/compensated signals
        data.data.stft_epoc_avg = mne.time_frequency.stft(data.data.epoc_div_avg, stft_pts, 32)   
        plt.figure(9)
        for data_ch in range(0, data.info.ch):            
            plt.subplot(data.info.ch/3, 3, data_ch+1)
            plt.imshow(np.flipud(np.squeeze(np.log(abs(data.data.stft_epoc_avg[data_ch,:,:])))),vmin = vrange[0], vmax = vrange[1], extent=[-epoc_time_des*10,epoc_time_des*10,0,data.info.fs/2])
            plt.ylim([0, 160])
            plt.title('STFT-avg, Ch' + str(data_ch))
            plt.ylabel('Hz')
            plt.xlabel('time(0.1s)')
        plt.gcf().canvas.draw()
        plt.imsave("009_STFT_epoc_avg_" +file_path + "_.png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')

        filename = file_path + '.pkl'        
        dill.dump_session(filename)        
        
        """
        # Common average reference of all channel
        tmp.comm_ref = np.average(data.data.epoc_div_avg, axis = 0)
        data.data.epoc_div_commref_avg = np.zeros([data.info.ch, 2*pts_des])
        for data_ch in range(0, data.info.ch):
            data.data.epoc_div_commref_avg[data_ch,:] = data.data.epoc_div_avg[data_ch,:] - tmp.comm_ref

        plt.figure(10)
        for data_ch in range(0, data.info.ch):       
            plt.subplot(data.info.ch/3, 3, data_ch+1) 
            plt.plot(data.data.epoc_timestamp,data.data.epoc_div_commref_avg[data_ch,:])
            plt.grid(True)
            plt.title('all epocs (CAR) ,Ch' + str(data_ch))
        plt.gcf().canvas.draw()
        plt.imsave("010_CAR_epoc_avg_" +file_path + "_.png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')   
        
        
        # STFT CAR signal
        data.data.stft_epoc_div_commref_avg = mne.time_frequency.stft(data.data.epoc_div_commref_avg, stft_pts, 32)   
        plt.figure(11)
        for data_ch in range(0, data.info.ch):            
            plt.subplot(data.info.ch/3, 3, data_ch+1)
            plt.imshow(np.flipud(np.squeeze(np.log(abs(data.data.stft_epoc_div_commref_avg[data_ch,:,:])))),vmin = vrange[0], vmax = vrange[1], extent=[-epoc_time_des*10,epoc_time_des*10,0,data.info.fs/2])
            plt.ylim([0, 160])
            plt.title('STFT-avg, Ch' + str(data_ch))
            plt.ylabel('Hz')
            plt.xlabel('time(0.1s)')
        plt.gcf().canvas.draw()
        plt.imsave("011_STFT_CAR_epoc_avg_" +file_path + "_.png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')
        
        """

        
        
              
        
        
        
        