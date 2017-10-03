"""
convertGPS.py

Author: Nik Martelaro (nikmart@stanford.edu)

Purpose: Convert the GPS data into a CSV that is readable by tools like
         ChronoViz and other data analysis software

Requirements: Python 3
              pynmea2

Usage: python convertGPS.py [gps_data] [starttime] [session]
[gps_data]: csv file with the raw gps data
[starttime]: UNIX timestamp from the start of the quad video
[session]: participant session name
"""

import pynmea2
import sys

# Data index postions
COMPTIME_IDX = 0
UTC_IDX = 2
VALID_IDX = 3
LAT_IDX = 4
NS_IDX = 5
LONG_IDX = 6
EW_IDX = 7
KNOT_IDX = 8
COURSE_IDX = 9
DATE_IDX = 10
VARIATION_IDX = 11

# get the command line arguments
if len(sys.argv) == 3:
    gps_data = sys.argv[1]
    starttime = float(sys.argv[2])
else:
    print("Incorrect number of arguments\nUsage: python convertGPS.py [gps_data] [starttime] [session]")
    quit()

# create the output file
output = open('gps.csv', 'w')
output.write("time,latitude,longitude\n") # output header

# compute the total time of the session data
f = open(gps_data, 'r')

for line in f:
    line = line.strip().split(",")
    #skip lines with bad data
    if line[VALID_IDX] == "A":
        # Convert GPRMC lat/long to google maps readable decimal lat/long [2]
        msg = pynmea2.parse(','.join(line[1:-3]))
        # compute the video time in seconds
        time = float(line[COMPTIME_IDX]) - starttime
        # write the data to the output
        output.write("{},{},{}\n".format(time, msg.latitude, msg.longitude))

print("Data time = {} minutes".format(round(time/60,1)))
if time/60 < 40:
    print("Data looks short...possibly not all there")
else:
    print("Data length looks OK")

f.close()
output.close()

# REFERENCES
# [1] Convert RMC -> decimal: https://community.oracle.com/thread/3619431
# [2] GPRMC Sentences: http://aprs.gids.nl/nmea/#rmc
