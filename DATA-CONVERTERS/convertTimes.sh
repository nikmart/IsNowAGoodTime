echo "Is Now A Good Time Data Time Converter"

echo "This program will convert the Unix timestamps to video timecode based on the initial video start time"

echo "Please provide the Is Now a Good Time participant data directory:"

read directory

echo "Converting data in $directory"

mkdir $directory/"SYNCED-DATA"

echo "Getting the video start in Unix time"

videostart=$(tail -n 1 $directory/VIDEO/QUAD/*.txt | tr ' ' '\n' | perl -MScalar::Util -ne 'Scalar::Util::looks_like_number($_) && print')

echo "Video start = $videostart"

echo "Converting data...\n"
#(python3 convertBio.py $directory/BIOPHYS/*.csv $videostart ; echo "Biosignals Converted!") &
(python convertIMU.py $directory/IMU/*.csv $videostart ; echo "IMU Converted!") &
(python convertResponses.py $directory/RESPONSES/*.csv $videostart ; echo "Responses Converted!") &
(python convertGPS.py $directory/GPS/*.csv $videostart ; echo "GPS Converted!") &
(python convertCAN.py $directory/CAN/*.txt $videostart ; echo "CAN Converted!") &&

echo "Moving data...\n"

mv *.csv $directory/SYNCED-DATA

echo "Data in directory\n"

ls $directory/SYNCED-DATA
