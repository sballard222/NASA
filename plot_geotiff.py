# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:59:50 2017

@author: sballar2
"""
import sys

import pdb
#from mayavi import mlab
import pylab as pl
from scipy import interpolate
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy 
import scipy.io
from scipy.io import netcdf

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


import pylab as pl

from netCDF4 import Dataset
import datetime 
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import cPickle as pickle 
import numpy as np
import scipy.io
from scipy.io import netcdf

file_name = 'ascat_20140331_031200_metopa_38635_eps_o_250_2300_ovw.l2.nc.gz.nc'
f = Dataset(file_name, mode='r')

time_ascat = f.variables['time'][:]
lat_ascat = f.variables['lat'][:]
lon_ascat = f.variables['lon'][:]-360
speed_ascat = f.variables['wind_speed'][:]
direction_ascat = f.variables['wind_dir'][:]

lon = scipy.io.loadmat('lon_HRHL.mat')
lat= scipy.io.loadmat('lat_HRHL.mat')
hei = scipy.io.loadmat('image_HRHL.mat')

lon = lon['lon']
lat = lat['lat']
hei = hei['image']



#filename = 'ascat_20140331_031200_metopa_38635_eps_o_250_2300_ovw.l2.nc.gz.nc'
#filename = 'subsetted-ascat_20140401_144200_metopa_38656_eps_o_coa_2300_ovw.l2.nc'
#f = netcdf.netcdf_file(filename)
#
#time_ascat = f.variables['time'][:]
#lat_ascat = f.variables['lat'][:]/1e5
#lon_ascat = f.variables['lon'][:]/1e5
#speed_ascat = f.variables['wind_speed'][:]/100
#direction_ascat = f.variables['wind_dir'][:]/10
#
#windu = -speed_ascat * numpy.cos(direction_ascat*(numpy.pi/180))
#windv = -speed_ascat * numpy.sin(direction_ascat*(numpy.pi/180))




  #d0 is longitude, d1 is latitude
#d0,d1=numpy.meshgrid(numpy.linspace(lat.min(),lat.max(), lon.shape[1]), 
#numpy.linspace(lon.min(), lon.max(), lon.shape[0]))  
#if lat[0,0] > 0: #northern hemisphere
#   if d1[0,0]<d1[-1,0]:
#      d1=numpy.flipud(d1)

windu = speed_ascat*np.cos(direction_ascat*(np.pi/180))
windv =  speed_ascat*np.sin(direction_ascat*(np.pi/180))



plt.figure()
d0,d1=numpy.meshgrid(lon,lat)
#hei_gridded = interpolate.griddata((lon.ravel(),lat.ravel()), hei.ravel(), (d1, d0), method='linear')
m = Basemap(llcrnrlon=d0.min(), llcrnrlat=d1.min(), urcrnrlon=d0.max(), urcrnrlat=d1.max(), resolution='f', area_thresh=0.01, projection='merc')
#if 'complex' in ires[product]['Data_output_format']:#any(numpy.iscomplex(hei_gridded)):
#   if mode=='p':
#      m.imshow(numpy.angle(hei_gridded), interpolation='nearest', origin='upper')
#   else:
#      m.imshow(10*numpy.log10(abs(hei_gridded)), interpolation='nearest', origin='upper')
#      pl.gray();
#else:
#  m.imshow(hei_gridded, interpolation='nearest', origin='upper')

#limits for the plot 
#longitudes

#d0,d1=numpy.meshgrid(lon,lat)
#x1 = d0.max() #+360  #max
#x2 = d0.min() #+360 #min
##latitudes
#y1 = d1.min()  #min
#y2 = d1.max() # max 
#
#lonidx=(lon_ascat>x2) & (lon_ascat<x1)
#latidx=(lat_ascat>y1) & (lat_ascat<y2)
#idx=latidx & lonidx
#
##x,y = m(lon_ascat,lat_ascat)
#x,y =  m(*np.meshgrid(lon_ascat[idx],lat_ascat[idx])) 
m.imshow(hei,cmap='gray', vmin = 210, vmax = 220)
 # draw a line around the map region
m.drawrivers() 
m.drawcountries(linewidth=0.5)
m.drawcoastlines(linewidth=0.5)
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='coral',lake_color='aqua')

m.drawparallels(numpy.arange(int(d1.min()), int(d1.max()), 0.5),linewidth=0.2,labels=[1,0,0,])  
m.drawmeridians(numpy.arange(int(d0.min()), int(d0.max()), 0.5),linewidth=0.2,labels=[0,0,0,1]) 
#m.title('B1L3_Pinpong_120MHz_200MHZ2014Mar31-17.27.50.854175_)
plt.title('EcoSAR HRHL Pingpong Mode: March 31 2014 22:27:50 UTC')
#m.quiver(x,y,windu[idx],windv[idx],width = 0.002,scale = 20)
plt.show
#m.contour(lon_ascat,lat_ascat, speed_ascat)

#lat_index = np.where(8.5673<=<=8.7452)



f.close()