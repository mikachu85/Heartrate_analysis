from __future__ import division
__author__ = 'Damien'

import matplotlib.pyplot as plt
import numpy as np
import math
import csv

# Pre-Data (Damien)

max_heartrate = 188 # Max hjerteslag - hoy intensitet
resting_heartrate = 52 # Hvilepuls - Generell

# csv - file loader

def heartrate_loader(filename):
    records = []
    with open(filename, 'rb') as csvfile: # Don't overwrite file.
        csvreader = csv.reader(csvfile, delimiter = ',') # Distinguishes between types
        for row in csvreader:
            if len(row) == 2: # Amount of rows.
                records.append({
                    "navn": row[0].strip(),
                    "heartrate_low": int(row[1].strip())
                })
    return records

# Import fil fra mappe
heartrate_data = heartrate_loader("Data/heartrate.data")


