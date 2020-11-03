#!/usr/bin/env python
# coding: utf-8

# ### Software for the tracking of storms and high-pressure systems

# Load required modules

# In[2]:


import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from datetime import date
from netCDF4 import Dataset


# In[3]:


from matplotlib import pyplot as plt

import storm_functions as storm


# In[4]:


#
# Load in Sea level Pressure data and lat/lon coordinates
#

dataset1 = '20201018'
#dataset2 = '20200726'
#dataset3 = '20200625'


# In[6]:


# Parameters
pathroot = {dataset1: '/shared/subx/forecast/psl/daily/full/RSMAS-CCSM4/'}#, dataset2:'/shared/subx/forecast/psl/daily/full/RSMAS-CCSM4/'}
var = {dataset1: 'psl'}#, dataset2 : 'psl'}#, '20200625': 'psl'}


# In[7]:


yearStart = {dataset1: 2020}#, dataset2:2020}
yearEnd = {dataset1: 2020}#, dataset2:2020} 


# In[8]:


# Load lat, lon
filename = {dataset1: pathroot[dataset1] + 'psl__RSMAS-CCSM4_'+dataset1+'.e1.daily.nc'}#,
            #dataset2: pathroot[dataset2] + 'psl__RSMAS-CCSM4_'+dataset2+'.e1.daily.nc'}
            #'NCEP_CFSR': pathroot['NCEP_CFSR'] + 'prmsl.gdas.' + str(yearStart['NCEP_CFSR']) + '01.grb2.nc'}


# In[9]:


fileobj = Dataset(filename[dataset1], 'r')
print (fileobj)
lon = fileobj.variables['lon'][:].astype(float)
lat = fileobj.variables['lat'][:].astype(float)

fileobj.close()

#fileobj = Dataset(filename[dataset2], 'r')
#print (fileobj)
#lon = fileobj.variables['lon'][:].astype(float)
#lat = fileobj.variables['lat'][:].astype(float)

#fileobj.close()


# In[10]:


psl = np.zeros((0, len(lat), len(lon)))
year = np.zeros((0,))
month = np.zeros((0,))
day = np.zeros((0,))
hour = np.zeros((0,))
print (day)


# In[11]:


print (psl)


# In[12]:


if (dataset1== dataset1):
    
    fileobj = Dataset(filename[dataset1], 'r')
    time = fileobj.variables['time'][:]
    time_ordinalDays = time/24. + date(1800,1,1).toordinal()
    year = np.append(year, [date.fromordinal(np.floor(time_ordinalDays[tt]).astype(int)).year for tt in range(len(time))])
    month = np.append(month, [date.fromordinal(np.floor(time_ordinalDays[tt]).astype(int)).month for tt in range(len(time))])
    day = np.append(day, [date.fromordinal(np.floor(time_ordinalDays[tt]).astype(int)).day for tt in range(len(time))])
    hour = np.append(hour, (np.mod(time_ordinalDays, 1)*24).astype(int))
    psl0 = fileobj.variables[var[dataset1]][:].astype(float)
    psl = np.append(psl, psl0, axis=0)
    fileobj.close()
    print (year, psl.shape[0])
    
#if (dataset2== dataset2):
    
    #fileobj = Dataset(filename[dataset2], 'r')
    #time = fileobj.variables['time'][:]
    #time_ordinalDays = time/24. + date(1800,1,1).toordinal()
    #year = np.append(year, [date.fromordinal(np.floor(time_ordinalDays[tt]).astype(int)).year for tt in range(len(time))])
    #month = np.append(month, [date.fromordinal(np.floor(time_ordinalDays[tt]).astype(int)).month for tt in range(len(time))])
    #day = np.append(day, [date.fromordinal(np.floor(time_ordinalDays[tt]).astype(int)).day for tt in range(len(time))])
    #hour = np.append(hour, (np.mod(time_ordinalDays, 1)*24).astype(int))
    #psl0 = fileobj.variables[var[dataset1]][:].astype(float)
    #psl = np.append(psl, psl0, axis=0)
    #fileobj.close()
    #print (year, psl.shape[0])


# In[13]:


#
# Storm Detection
#

# Initialisation

lon_storms_a = []
lat_storms_a = []
amp_storms_a = []
lon_storms_c = []
lat_storms_c = []
amp_storms_c = []

print (lon_storms_a)
# Loop over time

#T = CCSM4.shape[0]
#print (T)


# In[14]:


T=psl.shape[0]
print (T)
for tt in range(T):
    
    print (tt, T)
    
    # Detect lon and lat coordinates of storms
    
    lon_storms, lat_storms, amp = storm.detect_storms(psl[tt,:,:], lon, lat, res=1, Npix_min=9, cyc='anticyclonic', globe=True)
    lon_storms_a.append(lon_storms)
    lat_storms_a.append(lat_storms)
    amp_storms_a.append(amp)
    
   
  
    lon_storms, lat_storms, amp = storm.detect_storms(psl[tt,:,:], lon, lat, res=1, Npix_min=9, cyc='cyclonic', globe=True)
    lon_storms_c.append(lon_storms)
    lat_storms_c.append(lat_storms)
    amp_storms_c.append(amp)
   
   
    # Save as we go
    
    
    if (np.mod(tt, 100) == 0) + (tt == T-1):
        print ('Save data')
    #
    # Combine storm information from all days into a list, and save
    #
        storms = storm.storms_list(lon_storms_a, lat_storms_a, amp_storms_a, lon_storms_c, lat_storms_c, amp_storms_c)
        np.savez('storm_det_psl', storms=storms, year=year, month=month, day=day, hour=hour)
        #print (storms)

                                    


# In[ ]:




