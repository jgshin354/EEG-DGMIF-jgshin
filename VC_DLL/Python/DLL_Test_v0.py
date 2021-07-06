# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 17:41:55 2021

@author: jgshi
"""

import sys

import numpy as np
from matplotlib.backends.qt_compat import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import ctypes
import scipy.interpolate
import os
from matplotlib import animation


n_pts = 256
n_channel = 4
s_freq = 256

raw_input=np.zeros(1024,)
depression_index = np.zeros(4,)
stress_index = 0;
attention_index = np.zeros(4,)

depression_index_single = 0
stress_index_single = 0
attention_index_single = 0


eegdll = ctypes.WinDLL('EEG_Quantization.dll')
get_quantized_index = eegdll['get_quantized_index']
get_quantized_index.argtypes = (ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float,)

get_quantized_index(raw_input.ctypes.data_as(ctypes.c_void_p), 
                    stress_index_single.ctypes.data_as(ctypes.c_float),
                    depression_index_single.ctypes.data_as(ctypes.c_float),
                    attention_index_single.ctypes.data_as(ctypes.c_float))

'''
get_stress_index = eegdll['get_stress_index']
get_stress_index(....)


get_depression_index = eegdll['get_depression_index']

get_attention_index = eegdll['get_attention_index']
'''


