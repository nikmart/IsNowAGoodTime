#!/bin/bash

echo "Video, GPS, and IMU startup for Is Now a Good Time?"
printf "Participant ID: "
read participant
echo "$participant"

# create a new directory for the participant and go to taht directoty
mkdir "$participant"

# start the video recording
python startVideo.py "$participant"

# start the GPS logger
python GPSLogger.py "$participant"

# start the IMU logger
python imu_logger.py "$participant"
