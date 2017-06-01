#!/bin/bash

echo "Depth recording startup for Is Now a Good Time?"
printf "Participant ID: "
read participant
echo "$participant"

cd ~/IsNowAGoodTime-ParticipantData

mkdir "$participant"/DEPTH

cd "$participant"/DEPTH

# start the depth recorder
~/GitRepos/record_realsense/./record_realsense "$participant" 2 1 640 480  480 360
