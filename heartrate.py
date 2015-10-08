from __future__ import division
__author__ = 'Damien'

import matplotlib.pyplot as plt
import numpy as np
import math
import csv

# Pre-Data (Damien) Legger input fra bruker til slutt.

max_heartrate = 188 # Max hjerteslag - hoy intensitet
resting_heartrate = 52 # Hvilepuls - Generell

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

for i in range (0,6):
    print (mh*hm1[i]), '\t', (mh*hm2[i])



