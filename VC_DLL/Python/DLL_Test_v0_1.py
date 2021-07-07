# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 17:41:55 2021

@author: jgshi
"""

import sys

import numpy as np
#from matplotlib.backends.qt_compat import QtCore, QtWidgets
#from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
#from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from ctypes import c_float,c_uint32,c_double,pointer,POINTER
import ctypes
#import scipy.interpolate
import os
#from matplotlib import animation


n_pts = 256
n_channel = 4
s_freq = 256

#raw_input=np.zeros(1024,)
#raw_input = (1024*np.random.randn(1024)+1024).astype('uint32')

sig_freq = 15
raw_input_tmp = (1024+1024*np.sin(2*np.pi*sig_freq*np.linspace(0,1-1/256,256))).astype('uint32')
raw_input = np.array([])
raw_input = np.append(raw_input, raw_input_tmp)
raw_input = np.append(raw_input, raw_input_tmp)
raw_input = np.append(raw_input, raw_input_tmp)
raw_input = np.append(raw_input, raw_input_tmp)

raw_input = raw_input.astype('uint32')
raw_input_p = raw_input.ctypes.data_as(POINTER(c_uint32))



eegdll = ctypes.WinDLL('EEG_Quantization.dll')



delta = np.zeros(4).astype('float32')
delta_p = delta.ctypes.data_as(POINTER(c_float))
theta = np.zeros(4).astype('float32')
theta_p = theta.ctypes.data_as(POINTER(c_float))
alpha = np.zeros(4).astype('float32')
alpha_p = alpha.ctypes.data_as(POINTER(c_float))
SMR = np.zeros(4).astype('float32')
SMR_p = SMR.ctypes.data_as(POINTER(c_float))
LowBeta = np.zeros(4).astype('float32')
LowBeta_p = LowBeta.ctypes.data_as(POINTER(c_float))
MidBeta = np.zeros(4).astype('float32')
MidBeta_p = MidBeta.ctypes.data_as(POINTER(c_float))
HighBeta = np.zeros(4).astype('float32')
HighBeta_p = HighBeta.ctypes.data_as(POINTER(c_float))
beta = np.zeros(4).astype('float32')
beta_p = beta.ctypes.data_as(POINTER(c_float))
gamma = np.zeros(4).astype('float32')
gamma_p = gamma.ctypes.data_as(POINTER(c_float))
#spectrum_r = 1e84*np.ones(1024).astype('float')

spectrum_r = np.zeros(1024).astype('float32')
spectrum_r_p = spectrum_r.ctypes.data_as(POINTER(c_float))

prep_freq_div = eegdll['prep_freq_div']
prep_freq_div.argtypes = (POINTER(ctypes.c_uint32), POINTER(c_float), POINTER(c_float), POINTER(c_float), 
                          POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float), 
                          POINTER(c_float), POINTER(c_float), POINTER(c_float))
prep_freq_div(raw_input_p, delta_p, theta_p, alpha_p, SMR_p, LowBeta_p, MidBeta_p, HighBeta_p, beta_p, gamma_p, spectrum_r_p)
plt.subplot(2,1,1)
plt.plot(spectrum_r)
x = [delta[0], theta[0], alpha[0], SMR[0], LowBeta[0], MidBeta[0], HighBeta[0], beta[0], gamma[0]]
plt.subplot(2,1,2)
plt.plot(x)









q_result = np.zeros(3).astype('float32')
q_result_p = q_result.ctypes.data_as(POINTER(c_float))


get_quantized_index = eegdll['get_quantized_index']
get_quantized_index.argtypes = (POINTER(c_uint32), POINTER(c_float))
get_quantized_index(raw_input_p, q_result_p)

stress_index_single = q_result[0]
depression_index_single = q_result[1]
attention_index_single = q_result[2]

print(q_result)


plt.figure()
plt.plot(raw_input)
'''


stress_index = np.zeros(1).astype('float32')
stress_index_p = stress_index.ctypes.data_as(POINTER(c_float))
get_stress_index = eegdll['get_stress_index']
get_stress_index(....)



depression_index = np.zeros(4).astype('float32')
depression_index_p = depression_index.ctypes.data_as(POINTER(c_float))
get_depression_index = eegdll['get_depression_index']


attention_index = np.zeros(4).astype('float32')
attention_index_p = attention_index.ctypes.data_as(POINTER(c_float))
get_attention_index = eegdll['get_attention_index']
'''


