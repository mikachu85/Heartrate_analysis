from __future__ import division
__author__ = 'Damien'

import matplotlib.pyplot as plt
import numpy as np
import math

import csv


# Pre-Data (user-input based)

max_heartrate = int(input('What is your max heartrate?')) # Max hjerteslag - hoy intensitet
resting_heartrate = int(input('What is your heartrate when rested?')) # Hvilepuls - Generell
heartrate_reserve = max_heartrate - resting_heartrate # Heartrate reserve
print "Your heartrate reserve is: ", heartrate_reserve
# csv - file loader

def heartrate_loader(filename):
    records = []
    with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        next(csvreader,'none') # Skips header line
        for row in csvreader:
            if len(row) == 5:
                records.append({
                    "navn": row[0].strip(),
                    "heartratelow_percentage": float(row[1].strip()),
                    "heartratehigh_percentage": float(row[2].strip()),
                    "heartreserve_low": float(row[3].strip()),
                    "heartreserve_high": float(row[4].strip())
                })
    return records

# csv-data
heartrate_data = heartrate_loader("Data/heartrate.data")


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
hrr = heartrate_reserve
rhr = resting_heartrate

template = "{0:8}|{1:10}|{2:15}|{3:7}"
#print template.format("[", (mh*hm1[i]), '\t', (mh*hm2[i]), "]", "\t", "[", (hrr*hr3[i]+rhr), '\t', (hrr*hr4[i]+rhr), "]")

for i in range (0,6):
    print '%20s  %1s  %8s %8s %1s %1s  %8s %8s %1s' % (navn[i], "[", (mh*hm1[i]), (mh*hm2[i]), "]", "[", (hrr*hr3[i]+rhr), (hrr*hr4[i]+rhr), "]")





