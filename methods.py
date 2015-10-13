from __future__ import division
__author__ = 'Damien'

import csv
import time

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

def tabledraw():
    print '%18s' % "Type", '%12s' % "Heart I", '%14s' % "Heart II"
    print "_________________________________________________"


def racepredictor():
    time1k = float(input('\nHow fast can you run 1km? [Type minutes:seconds]'))
    print '\nThe approximated times for 5k,10k,21k will be:\n'
    if time1k >= 5 and time1k <= 6:
        print "5k time: " , time1k*5.3 , "\n\n10k time:" , time1k*10.6 , "\n\n21k time:" , time1k*21.9
    elif time1k >= 6 and time1k <= 7:
        print "5k time: " , time1k*5.6 , "\n\n10k time:" , time1k*10.9 , "\n\n21k time:" , time1k*22.5



