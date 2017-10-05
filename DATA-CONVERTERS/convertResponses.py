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

# CONSTANTS
# names of shit go here

COMPTIME_IDX = 0

## get file and start time from cmd line args

response_data = sys.argv[1]
starttime = float(sys.argv[2])

## create output file

output = open('response_out.csv', 'w')
output.write("time\n")

with open(response_data, newline='\n') as csvfile:
    for row in csvfile:
        row = row.strip()
        # only convert properley formatted data lines
        if row != "time":
            time = float(row) - starttime
            # only write out time that is greater than zero, the begining of vid
            if time >= 0:
                output.write('{}\n'.format(time))

print("Data time = {} minutes".format(round(time/60,2)))
if time/60 < 40:
    print("Response data looks short...possibly not all there")
else:
    print("Response data is longer than 40 mins, looks OK")

output.close()
