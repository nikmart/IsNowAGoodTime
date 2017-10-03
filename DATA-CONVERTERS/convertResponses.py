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
                time = float(data_time) - float(starttime)
                output.write("{}\n".format(time))

output.close()
