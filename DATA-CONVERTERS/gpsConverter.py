import csv
from datetime import datetime, timedelta
import pynmea2
import sys

gps_data = sys.argv[1]
starttime = sys.argv[2]

# create the output file
output = open('gpsData_out.csv', 'w')
output.write("time,latitude,longitude\n")

# Convert GPRMC lat/long to google maps readable decimal lat/long
with open(gps_data, newline='\n') as csvfile:
    output_writer = csv.writer(output, delimiter=',')

    gpsreader = csv.reader(csvfile, delimiter=',')

    line = 0
    for row in gpsreader:
        # get the starttime for offsetting
        if line == 0:
            starttime = float(row[0])
            line = 1 # stop updating the starttime
            #print(starttime)

        msg = pynmea2.parse(','.join(row[1:-3]))

        time = datetime.fromtimestamp(float(row[0]) - float(starttime))
        time -= timedelta(hours = 16) #16 is the timeshift for the hour that raw seconds convert to in Unix time
        timecode = time.strftime('%H:%M:%S.%f')
        #print(timecode, msg.latitude, msg.longitude)
        output_writer.writerow([timecode, msg.latitude, msg.longitude])

output.close()

# REFERENCES
# [1] Convert RMC -> decimal: https://community.oracle.com/thread/3619431
