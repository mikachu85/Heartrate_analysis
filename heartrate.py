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
            if len(row) == 3:
                records.append({
                    "navn": row[0].strip(),
                    "heartratelow_percentage": float(row[1].strip()),
                    "heartratehigh_percentage": float(row[2].strip())
                })
    return records

# csv-data
heartrate_data = heartrate_loader("Data/heartrate.data")

# For loop to iterate through data from csv-file
navn = [x['navn'] for x in heartrate_data]
heartratelow_percentage = [x['heartratelow_percentage'] for x in heartrate_data]
heartratehigh_percentage = [x['heartratehigh_percentage'] for x in heartrate_data]

print heartratelow_percentage, heartratehigh_percentage
