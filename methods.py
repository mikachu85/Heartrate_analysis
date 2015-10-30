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
    return True


def racepredictor():
    time1k = raw_input('\nHow fast can you run 1km? [Minutes:Seconds]')
    print '\nThe approximated times for 5k,10k,21k will be:\n'

    calc = time1k.split(':')
    calc_0 = int(calc[0])
    calc_1 = int(calc[1])

    time5k_min = math.ceil(calc_0*5)
    time10k_min = math.ceil(calc_0*10)
    time21k_min = math.ceil(calc_0*21)
    time21k_h = 0

    if calc_1 < 10:
        time_sec = random.randint(5,20)
        time5k_min += 1
        time10k_min += 2
        time21k_min += 4

    elif calc_1 >= 10 and calc_1 < 30:
        time_sec = random.randint(20,40)
        time5k_min += 2
        time10k_min += 4
        time21k_min += 14

    elif calc_1 == 30:
        time_sec = 30
        time5k_min += 3
        time10k_min += 6
        time21k_min += 17

    elif calc_1 >= 30 and calc_1 < 45:
        time_sec = random.randint(30,59)
        time5k_min += 4
        time10k_min += 7
        time21k_min += 19

    elif calc_1 >= 45:
        time_sec = random.randint(40,59)
        time5k_min += 4
        time10k_min += 10
        time21k_min += 22


    # If person uses more than 60 minutes to complete 21k
    if time21k_min >= 60 and time21k_min <= 119:
        time21k_min -= 60
        time21k_h += 1

    elif time21k_min >= 120 <= 179:
        time21k_min -= 120
        time21k_h += 2

    elif time21k_min >= 180:
        time21k_min -= 180
        time21k_h += 3

    # Fixing decimals. Removing unwanted zeroes.
    time5k_min_fix = '%0.d' % time5k_min
    time10k_min_fix = '%0.d' % time10k_min
    time21k_min_fix = '%0.d' % time21k_min

    print "5k time: " , time5k_min_fix, 'minutes', ':' , time_sec, 'seconds'
    print "10k time: " , time10k_min_fix, 'minutes', ':' , time_sec - 2, 'seconds'

    if time21k_h > 1:
        print "21k time: " , time21k_h, 'hours', ':', time21k_min_fix, 'minutes', ':', time_sec - random.randint(1,3), 'seconds'
    elif time21k_h == 1:
        print "21k time: " , time21k_h, 'hour', ':', time21k_min_fix, 'minutes', ':', time_sec - random.randint(1,3), 'seconds'
    elif time21k_h == 0:
        print time21k_min_fix, 'minutes', ':', time_sec - random.randint(1,3), 'seconds'

    return True




# def get_sec(s):
#     l = s.split(':')
#     return int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])
#
# print get_sec('1:23:45')
# print get_sec('0:04:15')
# print get_sec('0:00:25')