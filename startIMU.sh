#!/bin/bash

echo "Video, GPS, and IMU startup for Is Now a Good Time?"
printf "Participant ID: "
read participant
echo "$participant"

# start the IMU logger
python imu_logger.py "$participant"
