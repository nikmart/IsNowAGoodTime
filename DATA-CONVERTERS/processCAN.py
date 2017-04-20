import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import time
import sys
start_time = time.time()


can_data = sys.argv[1] # filename for CAN data
starttime = sys.argv[2] # the UNIX start time of the video recording

# lists to store data before creating numpy arrays
brakeTimeList = []
brakeData = []

speedTimeList = []
speedData = []

pedalTimeList = []
pedalPos = []
pedalCanRange = 0xc8 # defines the no accelerator (0x00) and full accelerator (0xc8) press
pedalRange = 100 # scale the pedal from 0% - 100%

speed_out = open('speed_out.csv','w') # write data to a converted output file
brake_out = open('brake_out.csv','w') # write data to a converted output file
accel_out = open('accel_out.csv','w') # write data to a converted output file

speed_out.write('time,speed\n')
brake_out.write('time,brake\n')
accel_out.write('time,accel\n')

# Load a data file as read only
with open(can_data, 'rb') as f:
# run through each line and pick out the data we are interested in
# fortunatley, the data is always fomatted the same with the same spacing between everything
# Timestamp: 1472338941.008668        ID: 01aa    000    DLC: 6    00 00 00 00 00 b1
    for line in f:
        csv_line = ''

        # read the line an seperate out the data based on the index of the string
        # this is much faster than parsing in another way
        canID = int(line[40:44],16)
        canTimestamp = float(line[11:28])

        # check to make sure there is no negative data (before all systems are recording)
        data_time = float(canTimestamp) - float(starttime)
        if data_time < 0:
            pass
        else:
            time = datetime.fromtimestamp(data_time)
            time -= timedelta(hours = 16) #16 is the timeshift for the hour that raw seconds convert to in Unix time
            timecode = time.strftime('%H:%M:%S.%f')
            #timecode = datetime.fromtimestamp(data_time).strftime('%M:%S.%f')
            csv_line = str(timecode) + ','

            # brakes
            if canID == 0x0224:
                brakeTimeList.append(canTimestamp)
                # see if the first byte of data is 00 or 20 and label off or on
                if line[65:67] == "00":
                    brakeData.append(0) #off
                    csv_line = csv_line + '0\n'
                elif line[65:67] == "20":
                    brakeData.append(1) # on
                    csv_line = csv_line + '1\n'
                brake_out.write(csv_line)

            # speed
            if canID == 0x00B4:
                speedTimeList.append(canTimestamp)
                # speed = INT16(data[5],data[6]) * 0.0062 [MPH]
                # print(line[80:85])
                hexSpeed = int(line[80:85].replace(" ",""), 16)
                #print(hexSpeed)
                speedData.append(hexSpeed * 0.0062)
                csv_line = csv_line + str(hexSpeed * 0.0062) + '\n'
                speed_out.write(csv_line)

            # accelerator pedal position
            if canID == 0x0245:
                pedalTimeList.append(canTimestamp)
                # pedalPos = INT16(data[0]data[1]) / 2
                pedalPos.append(int(line[71:73],16) / 2) # 0xc8 = 200 we can scale by 2 to get a range of 0 - 100
                csv_line = csv_line + str(int(line[71:73],16) / 2) + '\n'
                accel_out.write(csv_line)

#print("--- %s seconds ---" % (time.time() - start_time)) #[1]

# plot the brake data
brakeTime = np.array(brakeTimeList)
brakeState = np.array(brakeData)
plt.plot(brakeTime, brakeState, linewidth=1, color='r', label='brakes') # scale to see better

# plot the speed data
speedTime = np.array(speedTimeList)
speedState = np.array(speedData)
plt.plot(speedTime, speedState, linewidth=1, color='b', label='speed')

# plot the accelerator pedal data
pedalTime = np.array(pedalTimeList)
pedalState = np.array(pedalPos)
plt.plot(pedalTime, pedalState, linewidth=1, color='g', label='accel')

# draw the legend
plt.legend()
plt.show()


## References
# [1] measuring time: http://stackoverflow.com/questions/1557571/how-to-get-time-of-a-python-program-execution
