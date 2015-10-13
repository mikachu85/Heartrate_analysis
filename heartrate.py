from __future__ import division
__author__ = 'Damien'

import matplotlib.pyplot as plt
import numpy as np
import math

import methods


'''Heartrate for zone training'''

# Pre-Data (user-input based)
max_heartrate = 188
resting_heartrate = 50
#max_heartrate = int(input('What is your max heartrate?')) # Max hjerteslag - hoy intensitet
#resting_heartrate = int(input('What is your heartrate when rested?')) # Hvilepuls - Generell
hrr = max_heartrate - resting_heartrate # Heartrate Reserve
print "\nYour max, resting and reserve heartrate are: ", max_heartrate, ",", resting_heartrate, ",", hrr
print "\nYour heartrate for the desired running types are as follows: \n\n"
# csv-data
heartrate_data = methods.heartrate_loader("Data/heartrate.data")

# Iterate through attributes in csv-file
navn = [x['navn'] for x in heartrate_data]
heartratelow_percentage = [x['heartratelow_percentage'] for x in heartrate_data]
heartratehigh_percentage = [x['heartratehigh_percentage'] for x in heartrate_data]
heartreserve_low = [x['heartreserve_low'] for x in heartrate_data]
heartreserve_high = [x['heartreserve_high'] for x in heartrate_data]

# Shortcuts
hm1 = heartratelow_percentage
hm2 = heartratehigh_percentage
hr3 = heartreserve_low
hr4 = heartreserve_high
mh = max_heartrate
rhr = resting_heartrate

# Print table
methods.tabledraw()

for i in range (0,6):
    print '%18s  %1s  %3s %1s %3s %1s %1s %3s %1s %3s %1s' % (navn[i], "[", int(mh*hm1[i]), "-", int(mh*hm2[i]), "]", "[", int(hrr*hr3[i]+rhr),"-", int(hrr*hr4[i]+rhr), "]")

# Race predictor
methods.racepredictor()



