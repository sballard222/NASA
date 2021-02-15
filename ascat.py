# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 15:33:25 2017

@author: sballar2
"""
import numpy as np

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
from scipy import interpolate

def wrapToPi(x):
    return mod(x+pi,2*pi)-pi   

def wrapToInt(x, period):
    return mod(x+period,2*period)-period


file_name = 'ascat_20140331_031200_metopa_38635_eps_o_250_2300_ovw.l2.nc.gz.nc'
#file_name = 'ascat_20140101_021500_metopa_37370_eps_o_coa_2200_ovw.l2.nc.gz.nc'
#file_name = 'subsetted-ascat_20140401_025100_metopa_38649_eps_o_250_2300_ovw.l2.nc'
f = Dataset(file_name, mode='r')

time_ascat = f.variables['time'][:]
lat_ascat = f.variables['lat'][:]
lon_ascat = f.variables['lon'][:]-360
speed_ascat = f.variables['wind_speed'][:]
direction_ascat_file = f.variables['wind_dir'][:]

lon = scipy.io.loadmat('lon_HRHL.mat')
lat= scipy.io.loadmat('lat_HRHL.mat')
hei = scipy.io.loadmat('image_HRHL.mat')

lon = wrapToInt(lon['lon'],180)
lat = lat['lat']
hei = hei['image']
#rad = 4.0*np.atan(1.0)/180
direction_ascat =wrapToPi(np.deg2rad(direction_ascat_file+90))https://cdn.instructables.com/ORIG/F8Q/GUXC/IJAEJ9J5/F8QGUXCIJAEJ9J5.py
windu = speed_ascat*np.cos((direction_ascat))
windv =  speed_ascat*np.sin((direction_ascat))



#limits for the plot 
#longitudes
x1 = -83.1#+360  #max
x2 = -84.1 #+360 #min
#latitudes
y1 =8   #min
y2 =9  # max 



lonidx=(lon_ascat>x2) & (lon_ascat<x1)
latidx=(lat_ascat>y1) & (lat_ascat<y2)
idx=latidx & lonidx
plt.figure()
#d0,d1=numpy.meshgrid(lon,lat)
#m = Basemap(llcrnrlon=d0.min(), llcrnrlat=d1.min(), urcrnrlon=d0.max(), urcrnrlat=d1.max(), resolution='f', area_thresh=1., projection='cyl')
m = Basemap(resolution='f',projection='merc',area_thresh = 0.01, llcrnrlat=y1,urcrnrlat=y2,llcrnrlon=x2,urcrnrlon=x1,lat_ts=(x1+x2)/2)
m.drawcountries(linewidth=0.5)
m.drawcoastlines(linewidth=0.5)
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='coral',lake_color='aqua')
#lon_ascat,lat_ascat = np.meshgrid(lon_ascat,lat_ascat)
x,y =  m(*np.meshgrid(lon_ascat[idx],lat_ascat[idx])) 
xl,yl =  m(*np.meshgrid(lon,lat)) 
X,Y = m(*np.meshgrid(np.linspace(x.min(),x.max(),1000),np.linspace(y.min(),y.max(),1000)))
#x,y = m(lon_ascat[idx],lat_ascat[idx], inverse= True)
#m.contourf = (x,y,speed_ascat[idx])
#m.colorbar()

m.quiver(x,y,windu[idx],windv[idx],speed_ascat[idx], headwidth = 10,scale = 100,cmap = 'hsv')
m.colorbar()
d0,d1=m(*np.meshgrid(lon,lat))

#hei2 = interpolate.interpn((yl[:,0], xl[0,:]),hei,(Y, X),bounds_error = False)
#m.imshow(hei, extent=[d0.min(),d0.max(),d1.min(),d1.max()],cmap='gray', vmin = 200, vmax = 220)
#

#m.imshow(hei);pl.gray();


#map.quiver(x,y,windu,windv)
#target_lat = 8.6
#target_lon = -83.7
#diff = 1000
#for i in range(1632):
#    for j in range(42):
#        lat = lats2[i,j]
#        lon = lons2[i,j]
#        lat_d = target_lat - lat
#        lon_d = target_lon - lon
#        diff_n = np.sqrt(lat_d**2 + lon_d**2)
#        if diff_n < diff:
#            diff = diff_n
#            time_ix = i
#            space_ix = j

#x_t, y_t = map(lons2[time_ix,space_ix],lats2[time_ix,space_ix])
#map.quiver(x_t,y_t,np.cos(np.deg2rad(wind_dir[time_ix,space_ix])),np.sin(np.deg2rad(wind_dir[time_ix,space_ix])),edgecolor='k', facecolor='white', linewidth=.5,scale = 10)



plt.show()
f.close()
