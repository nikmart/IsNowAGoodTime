"""
convertGPS.py

Author: Nik Martelaro (nikmart@stanford.edu)

Purpose: Convert the IMU data into a human-readable CSV that is readable by
         tools like ChronoViz and other data analysis software

Requirements: Python 3

Usage: python convertIMU.py [imu_data] [starttime]
[imu_data]: csv file with the raw imu data
"""

import sys

# CONSTANTS
DATA_LEN = 27
COMPTIME_IDX = 0

## IMU Data labels
# accelX,accelY,accelZ,magnetX,magnetY,magnetZ,gyroX,gyroY,gyroZ,eulerX,eulerY,
# eulerZ,linAccelX,linAccelY,linAccelZ,gravityX,gravityY,gravityZ,quatW,quatX,
# quatY,quatZ,systemCal,gyroCal,accelCal,magCal

imu_data = sys.argv[1]
starttime = float(sys.argv[2])

# create the output file
output = open('imuData_out.csv', 'w')
output.write("time,accelX,accelY,accelZ,magnetX,magnetY,magnetZ,gyroX,gyroY,gyroZ,eulerX,eulerY,eulerZ,linAccelX,linAccelY,linAccelZ,gravityX,gravityY,gravityZ,quatW,quatX,quatY,quatZ,systemCal,gyroCal,accelCal,magCal\n")

# Convert GPRMC lat/long to google maps readable decimal lat/long
with open(imu_data, newline='\n') as csvfile:
    for row in csvfile:
        row = row.strip().split(',')
        # only convert properley formatted data lines
        if len(row) == DATA_LEN:
            time = float(row[COMPTIME_IDX]) - starttime
            # only write out time that is greater than zero, the begining of vid
            if time >= 0:
                output.write("{},{}\n".format(time, ','.join(row[1:])))

print("Data time = {} minutes".format(round(time/60,1)))
if time/60 < 40:
    print("IMU data looks short...possibly not all there")
else:
    print("IMU data looks OK")

output.close()
