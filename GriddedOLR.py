#!/usr/bin/env python
# coding: utf-8

# In[9]:


import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
import cartopy.mpl.ticker as cticker
from cartopy.util import add_cyclic_point
import pandas as pd


# In[10]:


#define the path to the file
path='/homes/jcrowel/Pangeo-at-AOES/docs/source/examples/stormTracking/'
#give the file name 
fname='ORLgrid.nc'
#open it up (can be called what ever you'd like)
da=xr.open_dataset(path+fname)
#this is to check to see whats inside
print (da)


# In[12]:


#creatinng a contour plot. The [243,:,:] allows me to look at the date I would like to analyze. 
plt.contourf(da['toa_lw_all_mon'][243,:,:])
# Set the axes using the specified map projection
ax=plt.axes(projection=ccrs.PlateCarree())

#add a cyclic point 
data=da['toa_lw_all_mon'][243,:,:]
data, lons = add_cyclic_point(data, coord=da['lon'])


# Make a filled contour plot
cs=ax.contourf(lons, da['lat'], data,
            transform = ccrs.PlateCarree(),cmap='RdYlBu',extend='both')

# Add coastlines
ax.coastlines()

# Define the xticks for longitude
ax.set_xticks(np.arange(-180,181,60), crs=ccrs.PlateCarree())
lon_formatter = cticker.LongitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)

# Define the yticks for latitude
ax.set_yticks(np.arange(-90,91,30), crs=ccrs.PlateCarree())
lat_formatter = cticker.LatitudeFormatter()
ax.yaxis.set_major_formatter(lat_formatter)

# Add colorbar
cbar = plt.colorbar(cs)

# defining what I would like the image to be called, in a specified format
date= pd.to_datetime(da['time'][243].values).strftime('%Y-%m-%d')
print(date)

#Saving the image to my folder as the date I chose.
image= date+'.png'
plt.savefig(image, dpi=150)


# In[ ]:




