import csv
import sys
from datetime import datetime, timedelta

# CONSTANTS
DATA_LEN = 27
TIME = 0

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
    imu_reader = csv.reader(csvfile, delimiter=',')

    for row in imu_reader:
        # only convert properley formatted data lines
        if len(row) == DATA_LEN:
            #print(float(row[0]) - float(starttime))
            time = datetime.fromtimestamp(float(row[0]) - float(starttime))
            time -= timedelta(hours = 16) #16 is the timeshift for the hour that raw seconds convert to in Unix time
            timecode = time.strftime('%H:%M:%S.%f')
            #print(timecode)
            #print(timecode + "," + ",".join(row[1:len(row)]))
            output.write(timecode + "," + ",".join(row[1:len(row)]) + "\n")
