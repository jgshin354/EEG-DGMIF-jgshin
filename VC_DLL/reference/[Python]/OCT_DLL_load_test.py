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
os.chdir('C:\\Users\\USER\\Desktop\\DGMIF\\data\\Code\\jgshin_priv\\Python3\\OCT_GUI\\20210217_OCT_GUI_octlab')
plt.close('all')

pts = 1024
ascan = 300
frame = 600
pts_img = ascan

fname = ['C:\\Users\\USER\\Desktop\\DGMIF\\data\\Code\\2_13_41-.unp']
fname = ['E:\\experimental_data\\20180820_AXSUN_OCTA\\20180817_eomtj\\4_37_02-.unp']

plt.close('all')
fname = ['C:\\Users\\USER\\Desktop\\DGMIF\\data\\Code\\2_13_41-.unp']
octdll = ctypes.WinDLL('OCTLib_64.dll')
OL_fft_u16 = octdll['OL_fft_u16']
OL_fft_u16.argtypes = (ctypes.c_uint, ctypes.c_uint, ctypes.c_byte, ctypes.c_byte, ctypes.c_wchar_p, ctypes.c_void_p,
                       ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)

file_oct = open(fname[0], 'rb')
raw_buffer = np.fromfile(file_oct, dtype=np.uint16, count=pts * ascan).reshape(ascan, pts)
FFT_frame = np.log(np.abs(np.fft.fft(raw_buffer, pts, axis=1)))

n_frame = 4

FFT_intensity = np.zeros([ascan*n_frame, np.uint(pts/2)], dtype=np.double)
FFT_phase = np.zeros([ascan*n_frame, np.uint(pts/2)], dtype=np.double)
FFT_re = np.zeros([ascan*n_frame, np.uint(pts/2)], dtype=np.double)
FFT_im = np.zeros([ascan*n_frame, np.uint(pts/2)], dtype=np.double)

raw_buffer2 = np.fromfile(file_oct, dtype=np.uint16, count=pts * ascan *n_frame ).reshape(ascan*n_frame, pts)
OL_fft_u16(pts, ascan*n_frame, 1, 1, raw_buffer2.ctypes.data_as(ctypes.c_wchar_p), FFT_intensity.ctypes.data_as(ctypes.c_void_p),
           FFT_phase.ctypes.data_as(ctypes.c_void_p), FFT_re.ctypes.data_as(ctypes.c_void_p),
           FFT_im.ctypes.data_as(ctypes.c_void_p))
plt.imshow(FFT_intensity)

### important: see number order np.arange(15).reshape(3, 5)  np.arange(2*3*4*5).transpose().reshape(2, 3, 4, 5)
bidir_n = 2
batch_n = 2
FFT_reshape = FFT_intensity.reshape(batch_n,bidir_n,ascan,np.int(pts/2)).copy()
plt.imshow(FFT_reshape[1,1,:,:])

FFT_reshape_mean = np.flipud(FFT_intensity.reshape(batch_n,bidir_n,ascan,np.int(pts/2)).copy().mean(axis=1).transpose(2,1,0))[-332:-32,:,1]
x = (FFT_reshape_mean - 70)/40*255
vminn = 70
vmaxx = 120
plt.imshow(np.uint8(FFT_reshape_mean), cmap='gray', vmin=vminn, vmax=vmaxx)

file_oct.close()


### rescaling code
FFT_line = np.fft.fft(raw_buffer[100])
plt.plot(np.log(np.abs(FFT_line)))
FFT_line2 = np.zeros(FFT_line.shape)
FFT_line2 = FFT_line.copy()
FFT_line2[0:8] = 0
FFT_line2[100:] = 0
phase_extracted = np.unwrap(np.angle(np.fft.ifft(FFT_line2)))
phase_normalized = (phase_extracted-np.min(phase_extracted)) / (np.max(phase_extracted) - np.min(phase_extracted))
phase_inverse = np.interp(np.arange(pts)/(pts-1),phase_normalized,np.arange(pts)/(pts-1))
plt.plot(phase_inverse)
CAL = phase_inverse*(pts-1)

np.save('cal.npy',CAL)

### dispersion compensation

raw_buffer3 = raw_buffer2.copy()
z = scipy.interpolate.interp1d(np.arange(0,pts), raw_buffer3, axis=1)
Z = np.uint16(z(CAL)).copy()


disp_a2 = 10
disp_a3 = -2

dix = np.linspace(-1,1,1024)
disp_v = np.exp(1j*((disp_a2*dix**2)+(disp_a3*dix**4)))
dix_2d = disp_v * np.ones([ascan*n_frame,1])
disp_comp = (Z*dix_2d).copy()


FFT_frame = np.log(np.abs(np.fft.fft(disp_comp, pts, axis=1)))
plt.imshow(np.flipud(np.log(FFT_frame[0:300, 0:300]).transpose()), cmap='gray', vmin = 2.2, vmax=2.8)




#plt.imshow(np.log(FFT_frame[0:300, 0:300]).transpose(), cmap='gray' , vmin = 10, vmax = 20)

### rescale evalution

raw_buffer3 = raw_buffer2.copy()
z = scipy.interpolate.interp1d(np.arange(0,pts), raw_buffer3, axis=1)
Z = np.uint16(z(CAL)).copy()

OL_fft_u16(pts, ascan*n_frame, 1, 1, Z.ctypes.data_as(ctypes.c_wchar_p), FFT_intensity.ctypes.data_as(ctypes.c_void_p),
           FFT_phase.ctypes.data_as(ctypes.c_void_p), FFT_re.ctypes.data_as(ctypes.c_void_p),
           FFT_im.ctypes.data_as(ctypes.c_void_p))
plt.imshow(FFT_intensity)






""" Vlim calibration module

### important: see number order np.arange(15).reshape(3, 5)  np.arange(2*3*4*5).transpose().reshape(2, 3, 4, 5)
bidir_n = 2
batch_n = 2
FFT_reshape = FFT_intensity.reshape(batch_n,bidir_n,ascan,np.int(pts/2)).copy()
plt.imshow(FFT_reshape[1,1,:,:])

FFT_reshape_mean = np.flipud(FFT_intensity.reshape(batch_n,bidir_n,ascan,np.int(pts/2)).copy().mean(axis=1).transpose(2,1,0))[-332:-32,:,1]
x = (FFT_reshape_mean - 70)/40*255
vminn = 70
vmaxx = 120
plt.imshow(np.uint8(FFT_reshape_mean), cmap='gray', vmin=vminn, vmax=vmaxx)

"""





#FFT_data = np.abs(np.fft.fft(raw_buffer, self.pts, axis=0)) / 204342 * 255





"""
plt.imshow(FFT_frame[-332:-32, :], vmin=3, vmax=15, cmap='gist_gray', )

data_raw = np.fromfile(file_oct, dtype=np.uint16, count=pts * ascan * frame)
x = np.log(np.abs(np.fft.fft(data_raw[0:1023])))
plt.plot(x)

file_oct.close()
# frame_count = 0


fig = plt.figure()
data = np.zeros((ascan, pts_img))
im = plt.imshow(data)

frame_count = 10
raw_buffer = data_raw[frame_count * pts * ascan:(frame_count + 2) * pts * ascan].reshape(ascan, pts, 2).transpose(1, 0,
                                                                                                                  2)
FFT_frame = np.log(np.abs(np.fft.fft(raw_buffer, pts, axis=0)))
"""

"""

def init():
    im.set_data(np.zeros((ascan, pts_img)))


def animate(i):
    raw_buffer = np.transpose(data_raw[frame_count * pts * ascan:(frame_count + 1) * pts * ascan].reshape(ascan, pts))
    FFT_frame = np.log(np.abs(np.fft.fft(raw_buffer, pts, axis=0)))
    FFT_frame[1:32, :] = 0
    FFT_frame[-32:, :] = 0
    plt.imshow(FFT_frame[-332:-32, :], vmin=3, vmax=15)

    im.set_data(FFT_frame[-332:-32, :])
    print(i)
    return im


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=600, interval=500)

"""
#
# while True:
#    raw_buffer = data_raw[frame_count*pts*ascan:(frame_count+1)*pts*ascan].reshape(pts, ascan)
#    FFT_frame = np.abs(np.fft.fft(raw_buffer,pts,axis=0))
#    plt.imshow(FFT_frame[-300:,:])
#    
#    

#    frame_count = (frame_count+1) % frame
#    self.canvas232.figure.gca().plt.imshow(FFT_frame)
#    self.canvas232.draw()
#    print(frame_count)
