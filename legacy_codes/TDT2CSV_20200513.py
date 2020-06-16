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
import scipy
import scipy.ndimage
import matplotlib.pyplot as plt
import tdt
#from tdt import read_block, read_sev, epoc_filter, download_demo_data
import mne
import pywt
#pywt.wavelist()

#vrange = [0,1e-4]
vrange = [-16,-10]
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
    #coeffs_p[9] = wav_hardth(coeffs_p[9])
    
    coeffs_p[9] = np.zeros(coeffs_p[9].shape)
    coeffs_p[10] = np.zeros(coeffs_p[10].shape)
    print(coeffs_p[11])
    #coeffs_p[10] = wav_hardth(coeffs_p[10])
    
    ## design a denoising method based on high pass filter scheme 
    
    """
    coeffs_p[0] =scipy.ndimage.gaussian_filter(wav_hardth(coeffs_p[0]),sigma =0.5)
    coeffs_p[1] =scipy.ndimage.gaussian_filter(wav_hardth(coeffs_p[1]),sigma =0.5)
    coeffs_p[2] =scipy.ndimage.gaussian_filter(wav_hardth(coeffs_p[2]),sigma =0.5)
    coeffs_p[3] =scipy.ndimage.gaussian_filter(wav_hardth(coeffs_p[3]),sigma =0.5)
    coeffs_p[4] =scipy.ndimage.gaussian_filter(wav_hardth(coeffs_p[4]),sigma =0.5)
    coeffs_p[5] =scipy.ndimage.gaussian_filter(wav_hardth(coeffs_p[5]),sigma =0.5)
    coeffs_p[6] =scipy.ndimage.gaussian_filter(wav_hardth(coeffs_p[6]),sigma =0.5)    
    
    coeffs_p[0] = wav_hardth(coeffs_p[0])
    coeffs_p[1] = wav_hardth(coeffs_p[1])
    coeffs_p[2] = wav_hardth(coeffs_p[2])
    coeffs_p[3] = wav_hardth(coeffs_p[3])    
    coeffs_p[4] = wav_hardth(coeffs_p[4])    
    coeffs_p[5] = wav_hardth(coeffs_p[5])    
    coeffs_p[6] = wav_hardth(coeffs_p[6])
    
    
    coeffs_p[0] = np.zeros(coeffs_p[0].size)
    coeffs_p[1] = np.zeros(coeffs_p[1].size)
    coeffs_p[2] = np.zeros(coeffs_p[2].size)
    coeffs_p[3] = np.zeros(coeffs_p[3].size)
    coeffs_p[4] = np.zeros(coeffs_p[4].size)
    coeffs_p[5] = np.zeros(coeffs_p[5].size)
    """
    dout = pywt.waverec(coeffs_p,'sym5')
    #dout = dout - scipy.ndimage.gaussian_filter(dout,sigma = 1)
    return dout
    

#import seaborn

#%%

base_path = "D:\\DGMIF\\Work\\2. Photobiomodulation\\20200514_coding_test"
#base_path = "E:\\DGMIF\\EEG\\20200428\\EEG_200428-200428"
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
        
        ## STFT, 768 PTS windowing
        data.data.stft_EEGG = mne.time_frequency.stft(data.data.EEGG, 768)        
        
        ## plot time-amplitude graph
        plt.figure(1)
        for data_ch in range(0, data.info.ch):
            plt.subplot(data.info.ch, 1, data_ch+1)
            plt.plot(data.time.timestamp, data.data.EEGG[data_ch,:])
            plt.plot(data.time.timestamp, data.time.trigger_timestamp * tmp.trig_disp_ampl[data_ch])
            if data_ch==0:
                plt.title('time-amplitude plot')
        plt.gcf().canvas.draw()
        plt.imsave(file_path + "_time-amplitude.png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')
       
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
        plt.imsave(file_path + "_STFT.png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')
        
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
        plt.imsave(file_path + "_WaveletDenoising_time-amplitude.png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')
      
        ## Plot denoised STFT chart
        data.data.stft_wavEEGG = mne.time_frequency.stft(data.data.wavEEGG, 768)        
        plt.figure(4)
        for data_ch in range(0, data.info.ch):            
            plt.subplot(data.info.ch/3, 3, data_ch+1)
            plt.imshow(np.flipud(np.squeeze(np.log(abs(data.data.stft_wavEEGG[data_ch,:,:])))),vmin = vrange[0], vmax = vrange[1], extent =[0,data.info.active_time,0,data.info.fs/2])
            #plt.imshow(np.flipud(np.squeeze((abs(data.data.stft_wavEEGG[data_ch,:,:])))),vmin = vrange[0], vmax = vrange[1], extent =[0,data.info.active_time,0,data.info.fs/2])
            plt.ylim([0, 160])
            plt.title('STFT, denoised, Ch' + str(data_ch))
            plt.ylabel('Hz')
            plt.xlabel('time(s)')            
        plt.gcf().canvas.draw()
        plt.imsave(file_path + "_WaveletDenoising_STFT.png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')


        xxx = data.data.stft_EEGG-data.data.stft_wavEEGG
        plt.figure(5)
        for data_ch in range(0, data.info.ch):            
            plt.subplot(data.info.ch/3, 3, data_ch+1)
            plt.imshow(np.flipud(np.squeeze(np.log(abs(xxx[data_ch,:,:])))),vmin = vrange[0], vmax = vrange[1], extent =[0,data.info.active_time,0,data.info.fs/2])
            #plt.imshow(np.flipud(np.squeeze((abs(xxx[data_ch,:,:])))),vmin = vrange[0], vmax = vrange[1], extent =[0,data.info.active_time,0,data.info.fs/2])
            plt.ylim([0, 160])
        plt.gcf().canvas.draw()

