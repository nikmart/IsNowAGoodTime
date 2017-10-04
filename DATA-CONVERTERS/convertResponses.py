"""
convertResponses.py

Author: Nik Martelaro (nikmart@stanford.edu)

Purpose: Convert the UNIX timestamps for each time a question was asked

Requirements: Python 3

Usage: python convertResponses.py [response_data] [starttime]
[response_data]: csv file with the UNIX timestamps for each question
[starttime]: UNIX timestamp from the start of the quad video
"""

import sys

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

# Check that the data seems like the right length
print("Data time = {} minutes".format(round(time/60,1)))
if time/60 < 40:
    print("Response data looks short...possibly not all there")
else:
    print("Response data length looks OK")

output.close()
