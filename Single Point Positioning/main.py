# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:15:49 2021

@author: Maciek

SPP z odległoscią geometryczną w pętli
"""
from readrnx import readrnxobs, readrnxnav
from functions import satpos
import numpy as np
# path to the broadcast navigation data - navigation RINEX file
# nav_file = "nav\\BRDC00WRD_R_20213180000_01D_GN.rnx"
# path to the observation data - observation RINEX file
obs_file = "nav\\KRA100POL_R_20213180000_01D_30S_MO.rnx"
  
# define time of observation file - should be the time the same that in the observation file
# for first epoch only:
time_start = [2021, 11, 14,  0,  0,  0]
time_end = [2021, 11, 14,  1,  0,  0]

# reading the observation data from the file
obs,iobs = readrnxobs(obs_file, time_start, time_end, 'R')
# reading the navigation data from the file:
# nav, inav = readrnxnav(nav_file)
#%%
# defining the approximate receiver coordinates: X,Y,Z
Xtrue = np.array([3856937.5695,  1397749.6854,  4867719.1135])
Xr0 = np.array([3850000.0000,  1390000.0000,  4860000.0000])
# some settings:
el_mask = 10 # elevation mask/cut off in degrees

# for the calculations only of the first epoch in the file, t is equal to 0 (because the data are from Sunday),
# week equal to 2184. If uou want to make calculations for different epochs, you can use the function date2tow(data), which can
# be found in the readrnx file, using the same as in the project 1
tr = 0
week = 2184

# taking only the observations from the specified epoch
# i = iobs[:,2]==t
# iobst = iobs[i,:]

# observation from one epoch - Pseudorange obs

#PRNs of satellites from the epoch
# sats = iobst[:,0]

dtr = 0
# create a vector of ro (geometric distance) for all satellites, in the first epoch ro can be tau*C, where tau is approximate transmission time, equal to 0.07s
# in the first epoch tau should be 0.07 and ro should be tau*C

for i in range (5):
    # loop for all the satellites in the epoch, good ideas is to get also index, using enumerate
    for isat, sat in enumerate(sats):


        # calculate transmission epoch: ts = tr - tau + dtr, dtr is the receiver clock error, in the first iteration, it is zero
        ts = ...
        # taking the ephemerides for one satellite - it should be an array of nav data, use (inav==sat)
        nav1sat = nav[(inav==sat),:]
        
        # calculating the coordinates of satellites, for the transmission epoch, use the satpos function, see the input values in the code
        # the outputs should be the XYZ and dts: inputs: satpos(week, ts, nav1sat)
         #!!!!!!!!!!!!!!!!!!!!
        Xs, dts = ...
       # rotation of the satellite coordinates due to rotation of the earth, use the rotation around Z-axis
        Xs_rot = ...
        
        # satellite-receiver vector
        Xsr = Xs_rot - Xr
        # the geometric distance between the satellite and the receiver
        ro = ...
        # elevation and azimuth calculations
        
        # if elevation above elevation mask, do the following calculations
        
        #!!!# calculate the atmospehric corrections: tropo and iono
        
        # compute calculated Pseudorange: Pcalc = ro + C*dtr-C*dts + tropo + iono
        # in testing, ommit the atmosphere, and assume that tropo = 0 and iono = 0
        
        # compute vector L: L = Pobs - Pcalc
        
        # compute A matrix
    
    # solve the equation system using least-squares method (after all satellites processed)
    # use function: np.dot, np.linalg.inv
    
    # modify the X, Y and Z using the results of the least square method
    # Xr = Xr + x[0:-1]
	# modify the receiver clock error, remember to divise the resulting cdt by speed of light (C) before adding to dt_r
# 	 dt_r = dt_r + x[-1]/C

    # if all iterations are done, save the epoch, X, Y, Z and dt_r for some whole day analysis






