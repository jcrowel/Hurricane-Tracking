#!/usr/bin/env python
# coding: utf-8

# 
# 
#   Software for the tracking of storms
#   based on detected storm position data.
# 
# 

# In[1]:


import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from datetime import date
from netCDF4 import Dataset
from matplotlib import pyplot as plt

import storm_functions as storm


# In[2]:


# Load in detected positions and date/hour information
filename = 'storm_det_psl'
data = np.load(filename + '.npz', allow_pickle=True)
print (filename)
data.files
print (data)
det_storms = data['storms']
year = data['year']
month = data['month']
day = data['day']
hour = data['hour']
#print ((det_storms[0]['lon']))
print (year)
print (month)
print (day)
print (hour)
print (len(det_storms))


# In[3]:


# Initialize storms discovered at first time step

storms = storm.storms_init(det_storms, year, month, day, hour)

#print (storms)


# In[4]:


T = len(det_storms) # number of time steps
print (T)
for tt in range(1, T-1):
    print (tt, T)
    # Track storms from time step tt-1 to tt and update corresponding tracks and/or create new storms
    storms = storm.track_storms(storms, det_storms, tt, year, month, day, hour,  dt=24,prop_speed=33.)

# Add keys for storm age and flag if storm was still in existence at end of run
print (len(storms))
for ed in range (len(storms)):
    storms[ed]['age'] = len(storms[ed]['lon'])

# Strip storms based on track lengths
storms = storm.strip_storms(storms, dt=24, d_tot_min=0.6, d_ratio=0.6, dur_min=12)

# Save tracked storm data
np.savez('storm_track_psl', storms=storms)


# In[ ]:




