# Hurricane-Tracking

This repository was created for the purpose of tracking Tropical Cyclones.

The first four scripts come from Eric Oliver's repository https://github.com/ecjoliver/stormTracking (Oliver, E., 2018).
these were changed by me to support the data that I was analyzing. Storm fuctions houses the fuctions created by Eric Oliver, that are called throughout the different scripts. It has been modified slightly for my research. The changes in the other scripts include switching from basemap to cartopy, and using the SubX (Sub seasonal forecasting) data (Pegion, K., 2019). The area I am researching is the Atlantic Basin, but the area can modified for your own usage in the storm plotting. 
With-in the storm plotting, sub-scripts have been added to plot the Precipitation, and the U and V winds as vectors. 

The next script is for the purpose of tracking the Madden-Julian Oscillation, this plots the Out-going Longwave Radiation as a proxy for the MJO (Kim, D et al.,2014).  

# Algorithm for Eric Olivers Storm Tracker. 
"Algorithm
Storms and anticylones are detected as extrema in the mean sea level pressure (slp) field. These extrema are detected following a modified form of the mesoscale ocean eddy tracking algorithm outlined in Chelton et al. (Progress in Oceanogaphy, 2011) and implemented in the eddyTracking code.

The first step is to run the storm_detection.py script which will load in the slp fields, detect extrema (minima for cyclones, maxima for anticyclones). Extrema must lie within a set of pixels no fewer than Npix_min (recommended value: 9). The cyclone/anticyclone position is then recorded as the centre of mass of this neighbourhood of points. The detected positions are then stored in a .npz file.

The next step is to run the storm_tracking.py script which will load in the detected positions and stitch together appropriate tracks. The positions are linked from one time step to the next if they are the nearest neighbours within a search radius given by a maximum storm speed of 80 km/hour. Tracks are further filtered by removing short tracks with a duration 12 hours or less. The tracked storms and anticyclones are then stored in a .npz file. (Oliver, E., 2018)"


# Contact

Jacquelyn Crowell

Student at George Mason University

Department of Atomospheric, Oceanic, and Earth Sciences

Fairfax, Virginia, United States

e: jcrowel@gmu.edu

Pegion, K., Kirtman, B., Becker, E., Collins, D., LaJoie, E., Burgman, R., Bell, R., DelSole, T., Min, D., Zhu, Y., Li, W., Sinsky, E., Guan, H., Gottschalck, J., Metzger, E., Barton, N., Achuthavarier, D., Marshak, J., Koster, R., Lin, H., Gagnon, N., Bell, M., Tippett, M., Robertson, A., Sun, S., Benjamin, S., Green, B., Bleck, R. and Kim, H., 2019. The Subseasonal Experiment (SubX): A Multimodel Subseasonal Prediction Experiment. Bulletin of the American Meteorological Society, 100(10), pp.2043-2060

Oliver, E. (2018). Ecjoliver - Overview. Retrieved September 07, 2020, from https://github.com/ecjoliver

Kim, D., Kug, J. and Sobel, A., 2014. Propagating versus Nonpropagating Madden–Julian Oscillation Events. Journal of Climate, 27(1), pp.111-125.
