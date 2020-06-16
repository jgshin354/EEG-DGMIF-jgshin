# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:29:47 2020

@author: JGSHIN
"""

import os

import numpy as np
from scipy.interpolate import interp1d
import scipy.ndimage
import matplotlib.pyplot as plt
import tdt
import mne
import pywt
import dill
import seaborn as sns
from pandas import Series, DataFrame


fft_n = 2**12
channel_use = 4
data_tot = tdt.StructType()        
data_tot.peak_amp = []
data_tot.color = []

for source_n in (['S01', 'S02', 'S03', 'S04', 'S05']):
    print(source_n)
    data_epoc = tdt.StructType()        
    data_epoc.data = tdt.StructType()
    data_epoc.time = tdt.StructType()
    data_epoc.info = tdt.StructType()
    
    
    dill.load_session(source_n + '_SHAM.pkl')
    data_epoc.data.sham = data.data.epoc_div_avg
    dill.load_session(source_n + '_RCW.pkl')
    data_epoc.data.rcw = data.data.epoc_div_avg
    dill.load_session(source_n + '_RPW.pkl')
    data_epoc.data.rpw = data.data.epoc_div_avg
    dill.load_session(source_n + '_GCW.pkl')
    data_epoc.data.gcw = data.data.epoc_div_avg
    dill.load_session(source_n + '_GPW.pkl')
    data_epoc.data.gpw = data.data.epoc_div_avg
    dill.load_session(source_n + '_BCW.pkl')
    data_epoc.data.bcw = data.data.epoc_div_avg
    dill.load_session(source_n + '_BPW.pkl')
    data_epoc.data.bpw = data.data.epoc_div_avg
    
    
    ##왜 3번 채널 AMPLITUDE가 제일 센거지???
    data_epoc.data.SHAM = np.fft.fft(data_epoc.data.sham[channel_use , pts_des:pts_des+fft_n])
    data_epoc.data.RCW = np.fft.fft(data_epoc.data.rcw[channel_use, pts_des:pts_des+fft_n])
    data_epoc.data.RPW = np.fft.fft(data_epoc.data.rpw[channel_use, pts_des:pts_des+fft_n])
    data_epoc.data.GCW = np.fft.fft(data_epoc.data.gcw[channel_use, pts_des:pts_des+fft_n])
    data_epoc.data.GPW = np.fft.fft(data_epoc.data.gpw[channel_use, pts_des:pts_des+fft_n])
    data_epoc.data.BCW = np.fft.fft(data_epoc.data.bcw[channel_use, pts_des:pts_des+fft_n])
    data_epoc.data.BPW = np.fft.fft(data_epoc.data.bpw[channel_use, pts_des:pts_des+fft_n])
    
    f_ind = np.linspace(0,data.info.fs-1/fft_n,fft_n)
    plt.close('all')
    
    plt.figure(1)
    plt.plot(f_ind, 20*np.log10(np.abs(data_epoc.data.SHAM)),'K')
    plt.title('Spectral amplitude, Sham')
    plt.legend(['Sham'])
    plt.xlim([0,80])
    plt.ylim([-100, -35])
    plt.grid(True)
    plt.gcf().canvas.draw()
    plt.imsave("A01_Spectral_amplitude_sham_" + source_n + ".png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')
    
    
    
    
    plt.figure(2)
    plt.plot(f_ind, 20*np.log10(np.abs(data_epoc.data.RCW)),'R')
    plt.plot(f_ind, 20*np.log10(np.abs(data_epoc.data.GCW)),'G')
    plt.plot(f_ind, 20*np.log10(np.abs(data_epoc.data.BCW)),'B')
    plt.title('Spectral amplitude, CW')
    plt.legend(['RED','GREEN','BLUE'])
    plt.xlim([0,80])
    plt.ylim([-100, -35])
    plt.grid(True)
    plt.gcf().canvas.draw()
    plt.imsave("A02_Spectral_amplitude_CW_" + source_n + ".png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')
    
    
    plt.figure(3)
    plt.plot(f_ind, 20*np.log10(np.abs(data_epoc.data.RPW)),'R')
    plt.plot(f_ind, 20*np.log10(np.abs(data_epoc.data.GPW)),'G')
    plt.plot(f_ind, 20*np.log10(np.abs(data_epoc.data.BPW)),'B')
    plt.legend(['RED','GREEN','BLUE'])
    
    plt.title('Spectral amplitude, 40Hz')
    plt.xlim([0, 80])
    plt.ylim([-100, -35])
    plt.grid(True)
    plt.gcf().canvas.draw()
    plt.imsave("A03_Spectral_amplitude_Mod_" + source_n + ".png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')
    
    
    
    plt.figure(4)
    scale_f = 16
    plt.plot(np.linspace(0,data.info.fs-(1/(fft_n*16)),fft_n*scale_f), 
              20*np.log10(np.abs(np.fft.fft(data_epoc.data.rpw[channel_use , pts_des:pts_des+fft_n],n=fft_n*scale_f))),'R')
    plt.plot(np.linspace(0,data.info.fs-(1/(fft_n*16)),fft_n*scale_f), 
              20*np.log10(np.abs(np.fft.fft(data_epoc.data.gpw[channel_use , pts_des:pts_des+fft_n],n=fft_n*scale_f))),'G')
    plt.plot(np.linspace(0,data.info.fs-(1/(fft_n*16)),fft_n*scale_f), 
              20*np.log10(np.abs(np.fft.fft(data_epoc.data.bpw[channel_use , pts_des:pts_des+fft_n],n=fft_n*scale_f))),'B')
    plt.legend(['RED','GREEN','BLUE'])
    
    plt.title('Spectral amplitude, 40-45hzHz')
    plt.xlim([40, 43])
    plt.ylim([-100, -35])
    plt.grid(True)
    plt.gcf().canvas.draw()
    plt.imsave("A04_Spectral_amplitude_Mod_40-45hz_" + source_n + ".png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')
    
    
    plt.figure(5)
    scale_f = 16
    plt.plot(np.linspace(0,data.info.fs-(1/(fft_n*16)),fft_n*scale_f),
                20*np.log10(np.abs(np.fft.fft(data_epoc.data.rpw[0, pts_des:pts_des+fft_n],n=fft_n*scale_f))),'R')
    plt.plot(np.linspace(0,data.info.fs-(1/(fft_n*16)),fft_n*scale_f),
                20*np.log10(np.abs(np.fft.fft(data_epoc.data.rpw[1, pts_des:pts_des+fft_n],n=fft_n*scale_f))),'G')
    plt.plot(np.linspace(0,data.info.fs-(1/(fft_n*16)),fft_n*scale_f),
                20*np.log10(np.abs(np.fft.fft(data_epoc.data.rpw[2, pts_des:pts_des+fft_n],n=fft_n*scale_f))),'B')
    plt.plot(np.linspace(0,data.info.fs-(1/(fft_n*16)),fft_n*scale_f),
                20*np.log10(np.abs(np.fft.fft(data_epoc.data.rpw[3, pts_des:pts_des+fft_n],n=fft_n*scale_f))),'C')
    plt.plot(np.linspace(0,data.info.fs-(1/(fft_n*16)),fft_n*scale_f),
                20*np.log10(np.abs(np.fft.fft(data_epoc.data.rpw[4, pts_des:pts_des+fft_n],n=fft_n*scale_f))),'M')
                 
    plt.legend(['Ch1','Ch2','Ch3','Ch4','Ch5'])
    plt.title('Spectral amplitude')
    plt.xlim([41, 42])
    plt.ylim([-60, -35])
    plt.grid(True)
    plt.gcf().canvas.draw()
    plt.imsave("A05_Spectral_amplitude_Mod_all_channel_rpw_" + source_n + ".png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')
           

    data_tot.peak_bpw =  np.max(20*np.log10(np.abs(data_epoc.data.BPW[100:400])))
    data_tot.peak_amp = np.concatenate((data_tot.peak_amp,data_tot.peak_bpw),axis = None)
    data_tot.color = np.concatenate((data_tot.color,'Blue'),axis = None)

    data_tot.peak_gpw =  np.max(20*np.log10(np.abs(data_epoc.data.GPW[100:400])))
    data_tot.peak_amp = np.concatenate((data_tot.peak_amp,data_tot.peak_gpw),axis = None)
    data_tot.color = np.concatenate((data_tot.color,'Green'),axis = None)

    
    data_tot.peak_rpw = np.max(20*np.log10(np.abs(data_epoc.data.RPW[100:400])))
    data_tot.peak_amp = np.concatenate((data_tot.peak_amp,data_tot.peak_rpw),axis = None)
    data_tot.color = np.concatenate((data_tot.color,'Red'),axis = None)
      
                
bp_data = DataFrame({'Peak Amplitude(db)' : data_tot.peak_amp,'Color':data_tot.color})        
plt.figure(6)

sns.boxplot(x="Color", y="Peak Amplitude(db)", data = bp_data,  color=("#95a5a6"))

plt.gcf().canvas.draw()
plt.imsave("A06_Peak_amplitude_CLR_" + source_n + ".png", np.array(plt.gcf().canvas.renderer._renderer), format = 'png')
