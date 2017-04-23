import sys
from datetime import datetime, timedelta

response_data = sys.argv[1]
starttime = sys.argv[2]

# create the output file
output = open('response_out.csv', 'w')
output.write("time\n")

with open(response_data, newline='\n') as csvfile:
    for data_time in csvfile:
        if data_time != "time\n":
            if float(data_time) - float(starttime) > 0:
                time = datetime.fromtimestamp(float(data_time) - float(starttime))
                time -= timedelta(hours = 16) #16 is the timeshift for the hour that raw seconds convert to in Unix time
                timecode = time.strftime('%H:%M:%S.%f')
                output.write(timecode + "\n")

output.close()
