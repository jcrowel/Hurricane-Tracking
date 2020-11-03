#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.mpl.ticker as cticker
from cartopy.util import add_cyclic_point


# In[2]:


data = np.load('storm_track_psl.npz',allow_pickle=True)
storms = data['storms']
print(range(len(storms)))


# In[4]:


#Test the quiver over the entire globe, below is over a specified area.

path='/shared/subx/forecast/ua850/daily/full/RSMAS-CCSM4/'
#defining the path name 
fname='ua_850_RSMAS-CCSM4_20201018.e1.daily.nc'
#opening the data with in the file and defining it (can be named whatever you'd like)
da=xr.open_dataset(path+fname)

path='/shared/subx/forecast/va850/daily/full/RSMAS-CCSM4/'
#defining the path name 
fname='va_850_RSMAS-CCSM4_20201018.e1.daily.nc'
#opening the data with in the file and defining it (can be named whatever you'd like)
dv=xr.open_dataset(path+fname)
x,y= np.meshgrid(dv['lon'],dv['lat'])
u=da['ua'][0,:,:]
v=dv['va'][0,:,:]
plt.quiver(x[::2,::2],y[::2,::2],u[::2,::2],v[::2,::2])


# In[13]:


#Open up the surface precipitation file
path='/shared/subx/forecast/prsfc/daily/full/RSMAS-CCSM4/'
#defining the path name 
fname='pr_sfc_RSMAS-CCSM4_20201018.e1.daily.nc'
#opening the data with in the file and defining it (can be named whatever you'd like)
ds=xr.open_dataset(path+fname)
print (ds)


# In[16]:


#create dimensions to keep the white spaces out
dim= ds.sel(lon=slice(270, 350),lat=slice(10,40))
lon= 300
minlon= -35 +lon
maxlon = +50 +lon
#here I have the extent to define where the map can go 
#The lat is different than what is defined above because this will get rid of white space 
extent=[minlon,maxlon, 11, 39]


fig = plt.figure(figsize=(11,8.5))

# Set the axes using the specified map projection
ax=plt.axes(projection=ccrs.PlateCarree())

ax.set_extent(extent)

# Add cyclic point to data
data=(dim['pr'][0,:,:]*86400)
#data, lons = add_cyclic_point(data, coord=ds['lon'])

# Make a filled contour plot
cs=ax.contourf(dim['lon'], dim['lat'], data,
            transform = ccrs.PlateCarree(),cmap='YlGn',extend='both')


#add the wind vectors on top of the contor plot
q=ax.quiver(x[::2,::2],y[::2,::2],u[::2,::2],v[::2,::2],transform = ccrs.PlateCarree())
# Add coastlines
ax.coastlines()


# Define the xticks for longitude
ax.set_xticks(np.arange(-80,-9,10), crs=ccrs.PlateCarree())
lon_formatter = cticker.LongitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)

# Define the yticks for latitude
ax.set_yticks(np.arange(10,41,5), crs=ccrs.PlateCarree())
lat_formatter = cticker.LatitudeFormatter()
ax.yaxis.set_major_formatter(lat_formatter)

# Add colorbar
cbar = plt.colorbar(cs)


# In[9]:


#this is a contour of the V winds, if contour is better than vectors.
# you can edit this to create a plot of the U winds too.

#finding the path to the data
path='/shared/subx/forecast/va850/daily/full/RSMAS-CCSM4/'
#defining the file name 
fname='va_850_RSMAS-CCSM4_20201018.e1.daily.nc'
#opening the data with in the file and defining it (can be named whatever you'd like)
dv=xr.open_dataset(path+fname)
print (dv)
dim= dv.sel(lon=slice(250, 350),lat=slice(10,40))
lon= 300
minlon= -30 +lon
maxlon = +50 +lon
#here I have the extent to define where the map can go 
#The lat is different than what is defined above because this will get rid of white space 
extent=[minlon,maxlon, 10, 40]
dv=dv.sel(lat=slice(10,40),lon=slice(270,350))
ax.set_extent(extent)
#Make the figure larger
fig = plt.figure(figsize=(11,8.5))

# Set the axes using the specified map projection
ax=plt.axes(projection=ccrs.PlateCarree())

# Add cyclic point to data
data=(dim['va'][0,:,:])
#data, lons = add_cyclic_point(data, coord=dv['lon'])


# Make a filled contour plot
cs=ax.contourf(dim['lon'], dim['lat'], data,
            transform = ccrs.PlateCarree(),cmap='spring',extend='both')

# Add coastlines
ax.coastlines()


# Define the xticks for longitude
ax.set_xticks(np.arange(-100,0,10), crs=ccrs.PlateCarree())
lon_formatter = cticker.LongitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)

# Define the yticks for latitude
ax.set_yticks(np.arange(10,40,5), crs=ccrs.PlateCarree())
lat_formatter = cticker.LatitudeFormatter()
ax.yaxis.set_major_formatter(lat_formatter)

# Add colorbar
cbar = plt.colorbar(cs)


# In[11]:


#this is back to the Storm tacker. It makes a plot of the specified area with 'tracks' of the areas with low pressure.
import cartopy.crs as ccrs
fig = plt.figure(figsize=(11,8.5))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.stock_img()
ax.set_extent([260,340,20,35])


for ed in range(len(storms)):
    
    storms[ed]['type'] == ('cyclonic')
    mcolor='b'
    ax.plot(storms[ed]['lon'], storms[ed]['lat'], marker='*', color=mcolor,
    transform=ccrs.PlateCarree())
    
    mcolor='r'
    ax.plot(storms[ed]['lon'], storms[ed]['lat'], marker='*', color=mcolor,
    transform=ccrs.PlateCarree())


# In[ ]:




