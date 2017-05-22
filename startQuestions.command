echo "Driver Query for Is Now a Good Time?"
printf "Participant ID: "
read answer
echo "$answer"

cd ~/IsNowAGoodTime-ParticipantData

echo "Starting driver query"

cd "$answer"
mkdir RESPONSES

cd responses
python ~/GitRepos/IsNowAGoodTime/isNowAGoodTime.py
