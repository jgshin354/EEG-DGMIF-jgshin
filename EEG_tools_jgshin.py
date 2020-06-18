# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 11:09:01 2020

@author: JGSHIN
"""
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
from scipy import interpolate


def get_boundary():
 return np.array([
    -4.400, 0.030, -4.180, 0.609, -3.960, 1.148, -3.740, 1.646, -3.520, 2.105, -3.300, 2.525, -3.080, 2.908, -2.860, 3.255,
    -2.640, 3.566, -2.420, 3.843, -2.200, 4.086, -1.980, 4.298, -1.760, 4.4799, -1.540, 4.6321, -1.320, 4.7567, -1.100, 4.8553,
    -0.880, 4.9298, -0.660, 4.9822, -0.440, 5.0150, -0.220, 5.0312,0, 5.035, 0.220, 5.0312, 0.440, 5.0150, 0.660, 4.9822,
    0.880, 4.9298, 1.100, 4.8553, 1.320, 4.7567, 1.540, 4.6321,1.760, 4.4799, 1.980, 4.2986, 2.200, 4.0867, 2.420, 3.8430,
    2.640, 3.5662, 2.860, 3.2551, 3.080, 2.9087, 3.300, 2.5258,3.520, 2.1054, 3.740, 1.6466, 3.960, 1.1484, 4.180, 0.6099,
    4.400, 0.0302, 4.400, 0.0302, 4.467, -0.1597, 4.5268, -0.3497,4.5799, -0.5397, 4.6266, -0.7297, 4.6673, -0.9197, 4.7025, -1.1097,
    4.7326, -1.2997, 4.7579, -1.4897, 4.7789, -1.6797, 4.7960, -1.8697,4.8095, -2.0597, 4.8199, -2.2497, 4.8277, -2.4397, 4.8331, -2.6297,
    4.8366, -2.8197, 4.8387, -3.0097, 4.8396, -3.1997, 4.8399, -3.3897,4.8384, -3.5797, 4.8177, -3.7697, 4.7776, -3.9597, 4.7237, -4.1497,
    4.6620, -4.3397, 4.5958, -4.5297, 4.5021, -4.7197, 4.400, -4.8937,4.1800, -5.1191, 3.9600, -5.3285, 3.7400, -5.5223, 3.5200, -5.7007,
    3.3000, -5.8642, 3.0800, -6.0131, 2.8600, -6.1478, 2.6400, -6.2688,2.4200, -6.3764, 2.2000, -6.4712, 1.9800, -6.5536, 1.7600, -6.6241,
    1.5400, -6.6833, 1.3200, -6.7317, 1.1000, -6.7701, 0.8800, -6.7991,0.6600, -6.8194, 0.4400, -6.8322, 0.2200, -6.8385, 0, -6.840,
    -0.220, -6.8385, -0.440, -6.8322, -0.660, -6.8194, -0.880, -6.7991,-1.100, -6.7701, -1.320, -6.7317, -1.540, -6.6833, -1.760, -6.6241,
    -1.980, -6.5536, -2.200, -6.4712, -2.420, -6.3764, -2.640, -6.2688,-2.860, -6.1478, -3.080, -6.0131, -3.300, -5.8642, -3.520, -5.7007,
    -3.740, -5.5223, -3.960, -5.3285, -4.180, -5.1191, -4.400, -4.89370,-4.5021, -4.7197, -4.5958, -4.5297, -4.6620, -4.3397, -4.7237, -4.1497,
    -4.7776, -3.9597, -4.8177, -3.7697, -4.8384, -3.5797, -4.8399, -3.3897,-4.8397, -3.1997, -4.8387, -3.0097, -4.8367, -2.8197, -4.8331, -2.6297,
    -4.8277, -2.4397, -4.8200, -2.2497, -4.8095, -2.0597, -4.7960, -1.8697,-4.7789, -1.6797, -4.7579, -1.4897, -4.7326, -1.2997, -4.7025, -1.1097,
    -4.6673, -0.9197, -4.6266, -0.7297, -4.5799, -0.5397, -4.5268, -0.3497,-4.4670, -0.1597, -4.4000, 0.03025]).reshape(-1, 2)


def montage_table_rodent_full():
   ch_name = ['FP1', 'FP2', 'AF3', 'AF4', 'AF7', 'AF8', 'F1', 'F2', 'F5', 'F6', 'FC1', 'FC2', 'FC5', 'FC6', 'C1', 'C2', 'C3', 'C4', 
   'C5', 'C6', 'CP1', 'CP2', 'CP3', 'CP4', 'CP5', 'CP6', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'PO3', 'PO4', 'PO7', 'PO8', 'O1', 'O2']
   x_ml = [-1.461,1.461,-1.461,1.461,-2.147,2.147,-1.461,1.461,-2.396,2.396,-1.71,1.71,-3.243,3.243,-1.559,1.559,-2.512,2.512,-3.51,
           3.51,-1.666,1.666,-2.673,2.673,-3.67,3.67,-1.684,1.684,-2.949,2.949,-4.009,4.009,-1.675,1.675,-2.619,2.619,-1.76,1.764]
   y_ap = [3.457,3.457,2.396,2.396,2.396,2.396,1.131,1.131,1.131,1.131,0,0,0,0,-0.989,-0.989,-0.989,-0.989,-0.989,-0.989,-2.254,
           -2.254,-2.254,-2.254,-2.254,-2.254,-3.332,-3.332,-3.332,-3.332,-3.332,-3.332,-4.695,-4.695,-4.695,-4.695,-5.702,-5.702]
   z_dv = [0.437357631,0.437357631,0.328018223,0.328018223,0.482915718,0.482915718,0.23690205,0.23690205,0.501138952,0.501138952,
           0.264236902,0.264236902,0.738041002,0.738041002,0.118451025,0.118451025,0.291571754,0.291571754,0.765375854,0.765375854,
           0.027334852,0.027334852,0.118451025,0.118451025,0.61047836,0.61047836,0.018223235,0.018223235,0.346241458,0.346241458,
           0.84738041,0.84738041,0.291571754,0.291571754,0.464692483,0.464692483,0.4738041,0.4738041]
   return DataFrame({'ch_name' : ch_name, 'x_ml' : x_ml, 'y_ap':y_ap, 'z_dv':z_dv})


def montage_table_rodent_dgmif():
    ch_name = ['F1','F2','C0','P2','P1','LE','RE']
    x_ml = [-1.461, 1.461, 0, 1.684,-1.684,-5.2,5.2]
    y_ap = [1.131, 1.131, -1.1, -3.332, -3.332,-4,-4]
    z_dv = [0.23690205, 0.23690205, 0,0.018223235,0.018223235,0,0]
    return DataFrame({'ch_name' : ch_name, 'x_ml' : x_ml, 'y_ap':y_ap, 'z_dv':z_dv})

      

def get_band_power(spectrum, freq, targetBand):
  if spectrum.ndim==1:
    ind = np.where( (freq > targetBand[0]) & (freq <= targetBand[1]))
    power = np.mean( abs(spectrum[ind])**2 )
  else:
    power = np.zeros( spectrum.shape[0] )
    ind = np.where( (freq > targetBand[0]) & (freq <= targetBand[1]))
    for ch in range(spectrum.shape[0]):
        power[ch]=np.mean( abs(spectrum[ch,ind])**2 )
  return power

def plt_montage_template(montage_table):
    plt.style.use('ggplot')
    plt.rcParams['font.family']='sans-serif'
    plt.rcParams['text.color']='black'; plt.rcParams['axes.labelcolor']='black'
    plt.rcParams['xtick.color']='black'; plt.rcParams['ytick.color']='black'
    elec_montage = np.array(montage_table)[:, 1:3]
    
    # Open figure handle
    #plt.figure(figsize=(4.5,5))
    
    # Plot EEG channels position (total 36 channels)
    plt.plot( elec_montage[:5,0], elec_montage[:5,1], 'go' )
    for chanIdx in range(elec_montage.shape[0]):
      plt.text( elec_montage[chanIdx,0], elec_montage[chanIdx,1]+.2,
               montage_table['ch_name'][chanIdx], ha='center', fontsize=8 )
    
    # Plot Ref/Gnd electrode position
    plt.plot( elec_montage[5:,0], elec_montage[5:,1], 'rs' )
    plt.text(0, 0.0, 'BP', fontsize=12, weight='bold', ha='center',va='center');
    plt.text(0,-4.2, 'LP', fontsize=12, weight='bold', ha='center',va='center');
    
    plt.xlabel('ML coordinate (mm)'); plt.ylabel('AP coordinate (mm)');
    plt.title('2D electrode montage');
    plt.legend(['Active','Ref/Gnd'], loc='upper right', facecolor='w');
    plt.gca().set_facecolor((1,1,1))
    plt.grid(False); plt.axis([-5.5, 6.5, -7, 6])
       
    boundary = get_boundary()
    for p in range(len(boundary)-1): plt.plot(boundary[p:p+2,0],boundary[p:p+2,1], 'k-')

def plot_mont_2d(xx, yy, data, cmap_in, clim, title_fig, montage_table):
    plt.contourf(xx, yy,  data, cmap=cmap_in, levels = np.linspace(clim[0],clim[1],100))
    plt.title(title_fig, fontsize = 10)
    plt.grid(False)
    plt.gca().set_aspect('equal','box')
    plt.xlabel('ML coordinate (mm)', fontsize=10);
    plt.ylabel('AP coordinate (mm)', fontsize=10);
    plt.text(0, 0.0, 'BP', color='w', fontsize=10, weight='bold', ha='center',va='center');
    plt.text(0,-4.2, 'LP', color='w', fontsize=10, weight='bold', ha='center',va='center');
    if clim is not None: plt.clim(clim)
    plt.plot(montage_table['x_ml'][0:5],montage_table['y_ap'][0:5], 'k.')    
    plt.axis( (-5.5, 5.5, -7, 5.2) ) 
    plt.gca().set_facecolor((1,1,1))

class bi_interp2:
  def __init__(self, x, y, z, xb, yb, xi, yi, method='linear'):
    self.x = x
    self.y = y
    self.z = z
    self.xb = xb
    self.yb = yb
    self.xi = xi
    self.yi = yi
    self.x_new, self.y_new = np.meshgrid(xi, yi)
    self.id_out = np.zeros([len(self.xi), len(self.xi)], dtype='bool')
    self.x_up, self.y_up, self.x_dn, self.y_dn = [], [], [], []
    self.interp_method = method
    self.z_new = []

  def __call__(self):
    self.find_boundary()
    self.interp2d()
    return self.x_new, self.y_new, self.z_new

  def find_boundary(self):
    self.divide_plane()
    # sort x value
    idup = self.sort_arr(self.x_up)
    iddn = self.sort_arr(self.x_dn)
    self.x_up = self.x_up[idup]
    self.y_up = self.y_up[idup]
    self.x_dn = self.x_dn[iddn]
    self.y_dn = self.y_dn[iddn]
    self.remove_overlap()
    # find outline, use monotone cubic interpolation
    ybnew_up = self.interp1d(self.x_up, self.y_up, self.xi)
    ybnew_dn = self.interp1d(self.x_dn, self.y_dn, self.xi)
    for i in range(len(self.xi)):
        idt1 = self.y_new[:, i] > ybnew_up[i]
        idt2 = self.y_new[:, i] < ybnew_dn[i]
        self.id_out[idt1, i] = True
        self.id_out[idt2, i] = True
    # expand data points
    self.x = np.concatenate((self.x, self.x_new[self.id_out].flatten(), self.xb))
    self.y = np.concatenate((self.y, self.y_new[self.id_out].flatten(), self.yb))
    self.z = np.concatenate((self.z, np.zeros(np.sum(self.id_out) + len(self.xb))))

  def interp2d(self):
    pts = np.concatenate((self.x.reshape([-1, 1]), self.y.reshape([-1, 1])), axis=1)
    self.z_new = interpolate.griddata(pts, self.z, (self.x_new, self.y_new), method=self.interp_method)
    self.z_new[self.id_out] = np.nan
    
  def remove_overlap(self):
    id1 = self.find_val(np.diff(self.x_up) == 0, None)
    id2 = self.find_val(np.diff(self.x_dn) == 0, None)
    for i in id1:
      temp = (self.y_up[i] + self.y_up[i+1]) / 2
      self.y_up[i+1] = temp
      self.x_up = np.delete(self.x_up, i)
      self.y_up = np.delete(self.y_up, i)
    for i in id2:
      temp = (self.y_dn[i] + self.y_dn[i + 1]) / 2
      self.y_dn[i+1] = temp
      self.x_dn = np.delete(self.x_dn, i)
      self.y_dn = np.delete(self.y_dn, i)

  def divide_plane(self):
    ix1 = self.find_val(self.xb == min(self.xb), 1)
    ix2 = self.find_val(self.xb == max(self.xb), 1)
    iy1 = self.find_val(self.yb == min(self.yb), 1)
    iy2 = self.find_val(self.yb == max(self.yb), 1)
    # divide the plane with Quadrant
    qd = np.zeros([self.xb.shape[0], 4], dtype='bool')
    qd[:, 0] = (self.xb > self.xb[iy2]) & (self.yb > self.yb[ix2])
    qd[:, 1] = (self.xb > self.xb[iy1]) & (self.yb < self.yb[ix2])
    qd[:, 2] = (self.xb < self.xb[iy1]) & (self.yb < self.yb[ix1])
    qd[:, 3] = (self.xb < self.yb[iy2]) & (self.yb > self.yb[ix1])
    # divide the array with y axis
    self.x_up = self.xb[qd[:, 0] | qd[:, 3]]
    self.y_up = self.yb[qd[:, 0] | qd[:, 3]]
    self.x_dn = self.xb[qd[:, 1] | qd[:, 2]]
    self.y_dn = self.yb[qd[:, 1] | qd[:, 2]]

  def find_val(self, condition, num_of_returns):
    # find the value that satisfy the condition
    ind = np.where(condition == 1)
    return ind[:num_of_returns]

  def sort_arr(self, arr):
    # return sorting index
    return sorted(range(len(arr)), key=lambda i: arr[i])

  def interp1d(self, xx, yy, xxi):
    # find the boundary line
    interp_obj = interpolate.PchipInterpolator(xx, yy)
    return interp_obj(xxi)



""" 
def plot_topo2d(data, boundary, clim=[-15,25], montage_table, plot_opt = True)
    x, y = np.array(montage_table['x_ml']), np.array(montage_table['y_ap'])
    xb, yb = boundary[:, 0], boundary[:, 1]
    xi, yi = np.linspace(min(xb), max(xb), 500), np.linspace(min(yb), max(yb), 500)
    x_new, y_new = np.meshgrid(xi,yi)
    
    id_out = np.zeros([len(xi), len(xi)], dtype='bool')
    x_up, y_up, x_dn, y_dn = [], [], [], []
    interp_method = 'cubic'
    z_new = []
    
    xin = x
    yin = y
    zin = z
    xin = np.concatenate([xin, np.array([min(xb), max(xb), min(xb), max(xb)])])
    yin = np.concatenate([yin, np.array([min(yb), max(yb), max(yb), min(yb)])])
    zin = np.concatenate([zin, np.array([0,0,0,0,0])])
    
    pts = np.concatenate((xin.reshape([-1,1]), yin.reshape([-1,1])),axis=1)
    
    z_new = interpolate.griddata(pts, zin, (x_new, y_new), method=interp_method)
    

    plt.contourf(x_new, y_new, z_new.reshape([500,500]), cmap=cm.jet, levels = np.linspace(5e-5,1e-4,50))
    plt.grid(False)
    plt.gca().set_aspect('equal','box')
    plt.xlabel('ML coordinate (mm)', fontsize=15);
    plt.ylabel('AP coordinate (mm)', fontsize=15);
    plt.text(0, 0.0, 'BP', color='w', fontsize=10, weight='bold', ha='center',va='center');
    plt.text(0,-4.2, 'LP', color='w', fontsize=10, weight='bold', ha='center',va='center');
    if clim is not None: plt.clim(clim)
    plt.plot(montage_table['x_ml'][0:5],montage_table['y_ap'][0:5], 'w.')    
"""



"""
    
    z_new = interpolate.griddata(pts, z.reshape([-1,1]), (x_new, y_new))#, method=interp_method)
    z_new[id_out] = np.nan

    
    # finding boundary()
    ix1 = np.argmin(xb)
    ix2 = np.argmax(xb)
    iy1 = np.argmin(yb)
    iy2 = np.argmax(yb)
    
    qd = np.zeros([xb.shape[0],4],dtype='bool')
    qd[:, 0] = (xb > xb[iy2]) & (yb > yb[ix2])
    qd[:, 1] = (xb > xb[iy1]) & (yb < yb[ix2])
    qd[:, 2] = (xb < xb[iy1]) & (yb < yb[ix1])
    qd[:, 3] = (xb < yb[iy2]) & (yb > yb[ix1])
    # divide the array with y axis
    x_up = xb[qd[:, 0] | qd[:, 3]]
    y_up = yb[qd[:, 0] | qd[:, 3]]
    x_dn = xb[qd[:, 1] | qd[:, 2]]
    y_dn = yb[qd[:, 1] | qd[:, 2]]
    
    # sort x value
    idup = sort_arr(x_up)
    iddn = sort_arr(x_dn)
    x_up = x_up[idup]
    y_up = y_up[idup]

    x_dn = x_dn[iddn]
    y_dn = y_dn[iddn]
    
    
    id1 = find_val(np.diff(x_up) == 0, None)
    id2 = find_val(np.diff(x_dn) == 0, None)
    for i in id1:
      temp = (y_up[i] + y_up[i+1]) / 2
      y_up[i+1] = temp
      x_up = np.delete(x_up, i)
      y_up = np.delete(y_up, i)
    for i in id2:
      temp = (y_dn[i] + y_dn[i + 1]) / 2
      y_dn[i+1] = temp
      x_dn = np.delete(x_dn, i)
      y_dn = np.delete(y_dn, i)
      
    """

 

def redundancy():
    plt.style.use('ggplot')
    plt.rcParams['font.family']='sans-serif'
    plt.rcParams['text.color']='black'; plt.rcParams['axes.labelcolor']='black'
    plt.rcParams['xtick.color']='black'; plt.rcParams['ytick.color']='black'
    
    montage_table = read_csv('montage.csv')
    elec_montage = np.array(montage_table)[:, 1:3]
    
    # Open figure handle
    plt.figure(figsize=(4.5,5))
    
    # Plot EEG channels position (total 36 channels)
    plt.plot( elec_montage[:36,0], elec_montage[:36,1], 'go' )
    for chanIdx in range(36):
      plt.text( elec_montage[chanIdx,0], elec_montage[chanIdx,1]+.2,
               montage_table['ch_name'][chanIdx], ha='center', fontsize=8 )
    
    # Plot Ref/Gnd electrode position
    plt.plot( elec_montage[36:,0], elec_montage[36:,1], 'rs' )
    plt.text(0, 0.0, 'BP', fontsize=12, weight='bold', ha='center',va='center');
    plt.text(0,-4.2, 'LP', fontsize=12, weight='bold', ha='center',va='center');
    
    plt.xlabel('ML coordinate (mm)'); plt.ylabel('AP coordinate (mm)');
    plt.title('2D electrode montage');
    plt.legend(['Active','Ref/Gnd'], loc='upper right', facecolor='w');
    plt.gca().set_facecolor((1,1,1))
    plt.grid(False); plt.axis([-5.5, 6.5, -7, 6])
       
    boundary = get_boundary()
    for p in range(len(boundary)-1): plt.plot(boundary[p:p+2,0],boundary[p:p+2,1], 'k-')
    #    plt.gcf().savefig(img_save_path+'A08_fig1-4.png', format='png', dpi=300);
    