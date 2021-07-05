# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 09:38:00 2020

@author: USER
"""
import os
import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt
import tdt
import mne
import dill
from pandas import read_csv
from scipy import interpolate
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import EEG_tools_jgshin as ets


fft_n = 2**12
channel_use = 4
data_tot = tdt.StructType()        
data_path_load = 'D:\\Backup\\DGMIF_data\\002_photobiomodulation\\preprocessed_EEG_proc_2nd_trial\\'
img_save_path =  'D:\\Backup\\DGMIF_data\\002_photobiomodulation\\preprocessed_EEG_proc_2nd_trial\\figures\\'

plt.close('all')
data_epoc = tdt.StructType()        
data_epoc.data = tdt.StructType()
data_epoc.time = tdt.StructType()
data_epoc.info = tdt.StructType()

source_n = 'Subject3'


dill.load_session(data_path_load + source_n + '-SHAM.pkl')
data_epoc.data.sham = data.data.epoc_div_avg
data_epoc.data.all_epoc_sham = data.data.epoc_div_ret
dill.load_session(data_path_load + source_n + '-RCW.pkl')
data_epoc.data.rcw = data.data.epoc_div_avg
data_epoc.data.all_epoc_rcw = data.data.epoc_div_ret
dill.load_session(data_path_load + source_n + '-RPW.pkl')
data_epoc.data.rpw = data.data.epoc_div_avg
data_epoc.data.all_epoc_rpw = data.data.epoc_div_ret
dill.load_session(data_path_load + source_n + '-GCW.pkl')
data_epoc.data.gcw = data.data.epoc_div_avg
data_epoc.data.all_epoc_gcw = data.data.epoc_div_ret
dill.load_session(data_path_load + source_n + '-GPW.pkl')
data_epoc.data.gpw = data.data.epoc_div_avg
data_epoc.data.all_epoc_gpw = data.data.epoc_div_ret
dill.load_session(data_path_load + source_n + '-BCW.pkl')
data_epoc.data.bcw = data.data.epoc_div_avg
data_epoc.data.all_epoc_bcw = data.data.epoc_div_ret
dill.load_session(data_path_load + source_n + '-BPW.pkl')
data_epoc.data.bpw = data.data.epoc_div_avg
data_epoc.data.all_epoc_bpw = data.data.epoc_div_ret
    
#Fast Fourier Transform
data_epoc.data.SHAM = np.fft.fft(data_epoc.data.sham[: , pts_des:pts_des+fft_n])
data_epoc.data.RCW = np.fft.fft(data_epoc.data.rcw[:, pts_des:pts_des+fft_n])
data_epoc.data.RPW = np.fft.fft(data_epoc.data.rpw[:, pts_des:pts_des+fft_n])
data_epoc.data.GCW = np.fft.fft(data_epoc.data.gcw[:, pts_des:pts_des+fft_n])
data_epoc.data.GPW = np.fft.fft(data_epoc.data.gpw[:, pts_des:pts_des+fft_n])
data_epoc.data.BCW = np.fft.fft(data_epoc.data.bcw[:, pts_des:pts_des+fft_n])
data_epoc.data.BPW = np.fft.fft(data_epoc.data.bpw[:, pts_des:pts_des+fft_n])
data_epoc.data.freq = np.linspace(0,data.info.fs-(1/fft_n),fft_n)

#Extraction of band component, montage boundary, channel informations 
pw_offset = 150
data_epoc.data.band_power_sham = 20*np.log10(ets.get_band_power(data_epoc.data.SHAM,data_epoc.data.freq,[35,45]))+pw_offset
data_epoc.data.band_power_rcw = 20*np.log10(ets.get_band_power(data_epoc.data.RCW,data_epoc.data.freq,[35,45]))+pw_offset
data_epoc.data.band_power_rpw = 20*np.log10(ets.get_band_power(data_epoc.data.RPW,data_epoc.data.freq,[35,45]))+pw_offset
data_epoc.data.band_power_gcw = 20*np.log10(ets.get_band_power(data_epoc.data.GCW,data_epoc.data.freq,[35,45]))+pw_offset
data_epoc.data.band_power_gpw = 20*np.log10(ets.get_band_power(data_epoc.data.GPW,data_epoc.data.freq,[35,45]))+pw_offset
data_epoc.data.band_power_bcw = 20*np.log10(ets.get_band_power(data_epoc.data.BCW,data_epoc.data.freq,[35,45]))+pw_offset
data_epoc.data.band_power_bpw = 20*np.log10(ets.get_band_power(data_epoc.data.BPW,data_epoc.data.freq,[35,45]))+pw_offset



#     plt.plot(20*np.log10(np.abs(data_epoc.data.RPW[1,:])))
 

boundary = ets.get_boundary_rat()
montage_table = ets.montage_table_rat_20200924()

#z = band_power[0:5]

plt.rcParams["figure.figsize"] = [4.5, 5]
plt.figure(1)
ets.plt_montage_template(montage_table)
plt.gcf().canvas.draw()
plt.gcf().savefig(img_save_path+'B01_montage_template_' + source_n + '.png', format='png', dpi=300)


plt.rcParams["figure.figsize"] = [14, 8]
plt.figure(2)
x, y = np.array(montage_table['x_ml']), np.array(montage_table['y_ap'])
xb, yb = boundary[:, 0], boundary[:, 1]
xi, yi = np.linspace(min(xb), max(xb), 500),np.linspace(min(yb), max(yb), 500)
clim = [0, 100]
xx, yy, data_epoc.data.mont_sham = ets.bi_interp2(x[0:13],y[0:13],data_epoc.data.band_power_sham[0:13],xb,yb,xi,yi, method='linear')()
xx, yy, data_epoc.data.mont_rcw = ets.bi_interp2(x[0:13],y[0:13],data_epoc.data.band_power_rcw[0:13],xb,yb,xi,yi, method='linear')()
xx, yy, data_epoc.data.mont_rpw = ets.bi_interp2(x[0:13],y[0:13],data_epoc.data.band_power_rpw[0:13],xb,yb,xi,yi, method='linear')()
xx, yy, data_epoc.data.mont_gcw = ets.bi_interp2(x[0:13],y[0:13],data_epoc.data.band_power_gcw[0:13],xb,yb,xi,yi, method='linear')()
xx, yy, data_epoc.data.mont_gpw = ets.bi_interp2(x[0:13],y[0:13],data_epoc.data.band_power_gpw[0:13],xb,yb,xi,yi, method='linear')()
xx, yy, data_epoc.data.mont_bcw = ets.bi_interp2(x[0:13],y[0:13],data_epoc.data.band_power_bcw[0:13],xb,yb,xi,yi, method='linear')()
xx, yy, data_epoc.data.mont_bpw = ets.bi_interp2(x[0:13],y[0:13],data_epoc.data.band_power_bpw[0:13],xb,yb,xi,yi, method='linear')()



data_epoc.data.mont_sham_draw = data_epoc.data.mont_sham.copy()
data_epoc.data.mont_sham_draw[np.where(data_epoc.data.mont_sham_draw>clim[1])] = clim[1]
data_epoc.data.mont_sham_draw[np.where(data_epoc.data.mont_sham_draw<clim[0])] = clim[0]
data_epoc.data.mont_rcw_draw = data_epoc.data.mont_rcw.copy()
data_epoc.data.mont_rcw_draw[np.where(data_epoc.data.mont_rcw_draw>clim[1])] = clim[1]
data_epoc.data.mont_rcw_draw[np.where(data_epoc.data.mont_rcw_draw<clim[0])] = clim[0]
data_epoc.data.mont_gcw_draw = data_epoc.data.mont_gcw.copy()
data_epoc.data.mont_gcw_draw[np.where(data_epoc.data.mont_gcw_draw>clim[1])] = clim[1]
data_epoc.data.mont_gcw_draw[np.where(data_epoc.data.mont_gcw_draw<clim[0])] = clim[0]
data_epoc.data.mont_bcw_draw = data_epoc.data.mont_bcw.copy()
data_epoc.data.mont_bcw_draw[np.where(data_epoc.data.mont_bcw_draw>clim[1])] = clim[1]
data_epoc.data.mont_bcw_draw[np.where(data_epoc.data.mont_bcw_draw<clim[0])] = clim[0]

plt.subplot(2,4,1)
fig_title = 'sham'
ets.plot_mont_2d_rat(xx,yy,data_epoc.data.mont_sham_draw, cm.jet, clim, fig_title, montage_table)
plt.subplot(2,4,2)
fig_title = 'Red CW light'
ets.plot_mont_2d_rat(xx,yy,data_epoc.data.mont_rcw_draw, cm.jet, clim, fig_title, montage_table)
plt.subplot(2,4,3)
fig_title = 'Green CW light'
ets.plot_mont_2d_rat(xx,yy,data_epoc.data.mont_gcw_draw, cm.jet, clim, fig_title, montage_table)
plt.subplot(2,4,4)
fig_title = 'Blue CW light'
ets.plot_mont_2d_rat(xx,yy,data_epoc.data.mont_bcw_draw, cm.jet, clim, fig_title, montage_table)


data_epoc.data.mont_sham_draw = data_epoc.data.mont_sham.copy()
data_epoc.data.mont_sham_draw[np.where(data_epoc.data.mont_sham_draw>clim[1])] = clim[1]
data_epoc.data.mont_sham_draw[np.where(data_epoc.data.mont_sham_draw<clim[0])] = clim[0]
data_epoc.data.mont_rpw_draw = data_epoc.data.mont_rpw.copy()
data_epoc.data.mont_rpw_draw[np.where(data_epoc.data.mont_rpw_draw>clim[1])] = clim[1]
data_epoc.data.mont_rpw_draw[np.where(data_epoc.data.mont_rpw_draw<clim[0])] = clim[0]
data_epoc.data.mont_gpw_draw = data_epoc.data.mont_gpw.copy()
data_epoc.data.mont_gpw_draw[np.where(data_epoc.data.mont_gpw_draw>clim[1])] = clim[1]
data_epoc.data.mont_gpw_draw[np.where(data_epoc.data.mont_gpw_draw<clim[0])] = clim[0]
data_epoc.data.mont_bpw_draw = data_epoc.data.mont_bpw.copy()
data_epoc.data.mont_bpw_draw[np.where(data_epoc.data.mont_bpw_draw>clim[1])] = clim[1]
data_epoc.data.mont_bpw_draw[np.where(data_epoc.data.mont_bpw_draw<clim[0])] = clim[0]

plt.subplot(2,4,5)
fig_title = 'sham'
ets.plot_mont_2d_rat(xx,yy,data_epoc.data.mont_sham_draw, cm.jet, clim, fig_title, montage_table)
plt.subplot(2,4,6)
fig_title = 'Red pulsed light 40hz'
ets.plot_mont_2d_rat(xx,yy,data_epoc.data.mont_rpw_draw, cm.jet, clim, fig_title, montage_table)
plt.subplot(2,4,7)
fig_title = 'Green pulsed light 40hz'
ets.plot_mont_2d_rat(xx,yy,data_epoc.data.mont_gpw_draw, cm.jet, clim, fig_title, montage_table)
plt.subplot(2,4,8)
fig_title = 'Blue pulsed light 40hz'
ets.plot_mont_2d_rat(xx,yy,data_epoc.data.mont_bpw_draw, cm.jet, clim, fig_title, montage_table)

plt.gcf().savefig(img_save_path+'B02_all_montage_' + source_n +'.png', format='png', dpi=300)

























"""
for source_n in (['S01', 'S02', 'S03', 'S04', 'S05']):
#data loading
       
    dill.load_session(data_path_load + source_n + '-SHAM.pkl')
    data_epoc.data.sham = data.data.epoc_div_avg
    data_epoc.data.all_epoc_sham = data.data.epoc_div_ret
    dill.load_session(data_path_load + source_n + '-RCW.pkl')
    data_epoc.data.rcw = data.data.epoc_div_avg
    data_epoc.data.all_epoc_rcw = data.data.epoc_div_ret
    dill.load_session(data_path_load + source_n + '-RPW.pkl')
    data_epoc.data.rpw = data.data.epoc_div_avg
    data_epoc.data.all_epoc_rpw = data.data.epoc_div_ret
    dill.load_session(data_path_load + source_n + '-GCW.pkl')
    data_epoc.data.gcw = data.data.epoc_div_avg
    data_epoc.data.all_epoc_gcw = data.data.epoc_div_ret
    dill.load_session(data_path_load + source_n + '-GPW.pkl')
    data_epoc.data.gpw = data.data.epoc_div_avg
    data_epoc.data.all_epoc_gpw = data.data.epoc_div_ret
    dill.load_session(data_path_load + source_n + '-BCW.pkl')
    data_epoc.data.bcw = data.data.epoc_div_avg
    data_epoc.data.all_epoc_bcw = data.data.epoc_div_ret
    dill.load_session(data_path_load + source_n + '-BPW.pkl')
    data_epoc.data.bpw = data.data.epoc_div_avg
    data_epoc.data.all_epoc_bpw = data.data.epoc_div_ret
        
    #Fast Fourier Transform
    data_epoc.data.SHAM = np.fft.fft(data_epoc.data.sham[: , pts_des:pts_des+fft_n])
    data_epoc.data.RCW = np.fft.fft(data_epoc.data.rcw[:, pts_des:pts_des+fft_n])
    data_epoc.data.RPW = np.fft.fft(data_epoc.data.rpw[:, pts_des:pts_des+fft_n])
    data_epoc.data.GCW = np.fft.fft(data_epoc.data.gcw[:, pts_des:pts_des+fft_n])
    data_epoc.data.GPW = np.fft.fft(data_epoc.data.gpw[:, pts_des:pts_des+fft_n])
    data_epoc.data.BCW = np.fft.fft(data_epoc.data.bcw[:, pts_des:pts_des+fft_n])
    data_epoc.data.BPW = np.fft.fft(data_epoc.data.bpw[:, pts_des:pts_des+fft_n])
    data_epoc.data.freq = np.linspace(0,data.info.fs-(1/fft_n),fft_n)
    
    #Extraction of band component, montage boundary, channel informations 
    pw_offset = 150
    data_epoc.data.band_power_sham = 20*np.log10(ets.get_band_power(data_epoc.data.SHAM,data_epoc.data.freq,[35,45]))+pw_offset
    data_epoc.data.band_power_rcw = 20*np.log10(ets.get_band_power(data_epoc.data.RCW,data_epoc.data.freq,[35,45]))+pw_offset
    data_epoc.data.band_power_rpw = 20*np.log10(ets.get_band_power(data_epoc.data.RPW,data_epoc.data.freq,[35,45]))+pw_offset
    data_epoc.data.band_power_gcw = 20*np.log10(ets.get_band_power(data_epoc.data.GCW,data_epoc.data.freq,[35,45]))+pw_offset
    data_epoc.data.band_power_gpw = 20*np.log10(ets.get_band_power(data_epoc.data.GPW,data_epoc.data.freq,[35,45]))+pw_offset
    data_epoc.data.band_power_bcw = 20*np.log10(ets.get_band_power(data_epoc.data.BCW,data_epoc.data.freq,[35,45]))+pw_offset
    data_epoc.data.band_power_bpw = 20*np.log10(ets.get_band_power(data_epoc.data.BPW,data_epoc.data.freq,[35,45]))+pw_offset
    
    
    
#     plt.plot(20*np.log10(np.abs(data_epoc.data.RPW[1,:])))
     
    
    boundary = ets.get_boundary_rat()
    montage_table = ets.montage_table_rat_20200924()
    
    #z = band_power[0:5]
    
    plt.rcParams["figure.figsize"] = [4.5, 5]
    plt.figure(1)
    ets.plt_montage_template(montage_table)
    plt.gcf().canvas.draw()
    plt.gcf().savefig(img_save_path+'B01_montage_template_' + source_n + '.png', format='png', dpi=300)
    
    
    plt.rcParams["figure.figsize"] = [14, 8]
    plt.figure(2)
    x, y = np.array(montage_table['x_ml']), np.array(montage_table['y_ap'])
    xb, yb = boundary[:, 0], boundary[:, 1]
    xi, yi = np.linspace(min(xb), max(xb), 500),np.linspace(min(yb), max(yb), 500)
    clim = [0, 100]
    xx, yy, data_epoc.data.mont_sham = ets.bi_interp2(x[0:13],y[0:13],data_epoc.data.band_power_sham[0:13],xb,yb,xi,yi, method='linear')()
    xx, yy, data_epoc.data.mont_rcw = ets.bi_interp2(x[0:13],y[0:13],data_epoc.data.band_power_rcw[0:13],xb,yb,xi,yi, method='linear')()
    xx, yy, data_epoc.data.mont_rpw = ets.bi_interp2(x[0:13],y[0:13],data_epoc.data.band_power_rpw[0:13],xb,yb,xi,yi, method='linear')()
    xx, yy, data_epoc.data.mont_gcw = ets.bi_interp2(x[0:13],y[0:13],data_epoc.data.band_power_gcw[0:13],xb,yb,xi,yi, method='linear')()
    xx, yy, data_epoc.data.mont_gpw = ets.bi_interp2(x[0:13],y[0:13],data_epoc.data.band_power_gpw[0:13],xb,yb,xi,yi, method='linear')()
    xx, yy, data_epoc.data.mont_bcw = ets.bi_interp2(x[0:13],y[0:13],data_epoc.data.band_power_bcw[0:13],xb,yb,xi,yi, method='linear')()
    xx, yy, data_epoc.data.mont_bpw = ets.bi_interp2(x[0:13],y[0:13],data_epoc.data.band_power_bpw[0:13],xb,yb,xi,yi, method='linear')()
    
    
    
    data_epoc.data.mont_sham_draw = data_epoc.data.mont_sham.copy()
    data_epoc.data.mont_sham_draw[np.where(data_epoc.data.mont_sham_draw>clim[1])] = clim[1]
    data_epoc.data.mont_sham_draw[np.where(data_epoc.data.mont_sham_draw<clim[0])] = clim[0]
    data_epoc.data.mont_rcw_draw = data_epoc.data.mont_rcw.copy()
    data_epoc.data.mont_rcw_draw[np.where(data_epoc.data.mont_rcw_draw>clim[1])] = clim[1]
    data_epoc.data.mont_rcw_draw[np.where(data_epoc.data.mont_rcw_draw<clim[0])] = clim[0]
    data_epoc.data.mont_gcw_draw = data_epoc.data.mont_gcw.copy()
    data_epoc.data.mont_gcw_draw[np.where(data_epoc.data.mont_gcw_draw>clim[1])] = clim[1]
    data_epoc.data.mont_gcw_draw[np.where(data_epoc.data.mont_gcw_draw<clim[0])] = clim[0]
    data_epoc.data.mont_bcw_draw = data_epoc.data.mont_bcw.copy()
    data_epoc.data.mont_bcw_draw[np.where(data_epoc.data.mont_bcw_draw>clim[1])] = clim[1]
    data_epoc.data.mont_bcw_draw[np.where(data_epoc.data.mont_bcw_draw<clim[0])] = clim[0]
    
    plt.subplot(2,4,1)
    fig_title = 'sham'
    ets.plot_mont_2d_rat(xx,yy,data_epoc.data.mont_sham_draw, cm.jet, clim, fig_title, montage_table)
    plt.subplot(2,4,2)
    fig_title = 'Red CW light'
    ets.plot_mont_2d_rat(xx,yy,data_epoc.data.mont_rcw_draw, cm.jet, clim, fig_title, montage_table)
    plt.subplot(2,4,3)
    fig_title = 'Green CW light'
    ets.plot_mont_2d_rat(xx,yy,data_epoc.data.mont_gcw_draw, cm.jet, clim, fig_title, montage_table)
    plt.subplot(2,4,4)
    fig_title = 'Blue CW light'
    ets.plot_mont_2d_rat(xx,yy,data_epoc.data.mont_bcw_draw, cm.jet, clim, fig_title, montage_table)
    
    
    data_epoc.data.mont_sham_draw = data_epoc.data.mont_sham.copy()
    data_epoc.data.mont_sham_draw[np.where(data_epoc.data.mont_sham_draw>clim[1])] = clim[1]
    data_epoc.data.mont_sham_draw[np.where(data_epoc.data.mont_sham_draw<clim[0])] = clim[0]
    data_epoc.data.mont_rpw_draw = data_epoc.data.mont_rpw.copy()
    data_epoc.data.mont_rpw_draw[np.where(data_epoc.data.mont_rpw_draw>clim[1])] = clim[1]
    data_epoc.data.mont_rpw_draw[np.where(data_epoc.data.mont_rpw_draw<clim[0])] = clim[0]
    data_epoc.data.mont_gpw_draw = data_epoc.data.mont_gpw.copy()
    data_epoc.data.mont_gpw_draw[np.where(data_epoc.data.mont_gpw_draw>clim[1])] = clim[1]
    data_epoc.data.mont_gpw_draw[np.where(data_epoc.data.mont_gpw_draw<clim[0])] = clim[0]
    data_epoc.data.mont_bpw_draw = data_epoc.data.mont_bpw.copy()
    data_epoc.data.mont_bpw_draw[np.where(data_epoc.data.mont_bpw_draw>clim[1])] = clim[1]
    data_epoc.data.mont_bpw_draw[np.where(data_epoc.data.mont_bpw_draw<clim[0])] = clim[0]
    
    plt.subplot(2,4,5)
    fig_title = 'sham'
    ets.plot_mont_2d_rat(xx,yy,data_epoc.data.mont_sham_draw, cm.jet, clim, fig_title, montage_table)
    plt.subplot(2,4,6)
    fig_title = 'Red pulsed light 40hz'
    ets.plot_mont_2d_rat(xx,yy,data_epoc.data.mont_rpw_draw, cm.jet, clim, fig_title, montage_table)
    plt.subplot(2,4,7)
    fig_title = 'Green pulsed light 40hz'
    ets.plot_mont_2d_rat(xx,yy,data_epoc.data.mont_gpw_draw, cm.jet, clim, fig_title, montage_table)
    plt.subplot(2,4,8)
    fig_title = 'Blue pulsed light 40hz'
    ets.plot_mont_2d_rat(xx,yy,data_epoc.data.mont_bpw_draw, cm.jet, clim, fig_title, montage_table)
    
    plt.gcf().savefig(img_save_path+'B02_all_montage_' + source_n +'.png', format='png', dpi=300)
    
    

"""













