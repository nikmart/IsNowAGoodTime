import sys
from datetime import datetime, timedelta

# Data indecies
TIME_IDX = 0
GSR_IDX = 1
HR_IDX = 2

data = sys.argv[1]
starttime = sys.argv[2]

# create the output file
output = open('biophys_out.csv', 'w')
output.write("time,GSR,HR\n")

row_num = 0
with open(data, newline='\n') as data_file:
    for row in data_file:
        #print(row_num)
        bio_data = row.strip().split("\t")
        if row_num > 2:
            #print(bio_data)
            data_time = float(bio_data[TIME_IDX])/1000.0
            if data_time - float(starttime) > 0:
                time = datetime.fromtimestamp(float(row[0]) - float(starttime))
                time -= timedelta(hours = 16) #16 is the timeshift for the hour that raw seconds convert to in Unix time
                timecode = time.strftime('%H:%M:%S.%f')
                #print(timecode + "," + bio_data[GSR_IDX] + "," + bio_data[HR_IDX] + "\n")
                output.write(timecode + "," + bio_data[GSR_IDX] + "," + bio_data[HR_IDX] + "\n") # GSR + HR data

        row_num += 1
