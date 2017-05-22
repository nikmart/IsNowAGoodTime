#!/bin/bash

echo "Video and GPS startup for Is Now a Good Time?"
printf "Participant ID: "
read answer
echo "$answer"

cd ~/IsNowAGoodTime-ParticipantData

# create a new directory for the participant and go to that directoty
mkdir "$answer"
mkdir "$answer"/VIDEO
mkdir "$answer"/VIDEO/QUAD

# start the video recording
python startVideo.py "$answer"/VIDEO/QUAD

mkdir "$answer"/GPS

# start the GPS logger
python GPSLogger.py "$answer"/GPS
