#!/bin/bash

echo "Video, GPS, and IMU startup for Is Now a Good Time?"
printf "Participant ID: "
read participant
echo "$participant"

cd ~/IsNowAGoodTime-ParticipantData

mkdir "$participant"/IMU

# start the IMU logger
python imu_logger.py "$participant"/IMU
