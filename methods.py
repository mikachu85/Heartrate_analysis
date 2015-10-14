from __future__ import division
__author__ = 'Damien'

import math
import csv
import time
import random
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
    time1k = raw_input('\nHow fast can you run 1km? [Minutes:Seconds]')
    print '\nThe approximated times for 5k,10k,21k will be:\n'

    calc = time1k.split(':')
    calc_0 = int(calc[0])
    calc_1 = int(calc[1])

    time5k_min = math.ceil(calc_0*5.3)
    print time5k_min
    time5k_sec = (calc_1 - calc_1) + random.randint(1,59)
    print "5k time: " , '%00.1s' % time5k_min, ':' , time5k_sec


# def get_sec(s):
#     l = s.split(':')
#     return int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])
#
# print get_sec('1:23:45')
# print get_sec('0:04:15')
# print get_sec('0:00:25')