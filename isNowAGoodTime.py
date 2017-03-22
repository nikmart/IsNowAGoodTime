import speech_recognition as sr
import timeit
import os
import random
import sched, time
import _thread
import pyaudio
import wave
import sys

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
MIC = 2 # USB MIC

# record the audio after a question is asked [4]
def recordAudio():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index = MIC)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    output_file = str(int(time.time())) + "_answer.wav"
    wf = wave.open(output_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    os.system('afplay ~/IsNowAGoodTime-ParticipantData/sounds/Pop.aiff') # play a sound to let the driver know they can speak

    # AUDIO_FILE = os.path.join(path.dirname(path.realpath(__file__)), output_file)
    # recognizeAudio(AUDIO_FILE)

# def recognizeAudio():
#     # use the audio file as the audio source
#     r = sr.Recognizer()
#     with sr.AudioFile(AUDIO_FILE) as source:
#         audio = r.record(source) # read the entire audio file
#
#     # recognize speech using Google Speech Recognition
#     try:
#         # for testing purposes, we're just using the default API key
#         # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#         # instead of `r.recognize_google(audio)`
#         print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))

def queryDriver():
    # write the ask time to the file
    f.write(str(time.time()) + '\n')

    #os.system('say is now a good time?')
    os.system('afplay ~/IsNowAGoodTime-ParticipantData/sounds/isNowAGoodTime.m4a')
    os.system('afplay ~/IsNowAGoodTime-ParticipantData/sounds/Morse.aiff') # play a sound to let the driver know they can speak

    #recordAudio()


# set up a file to log the question times and the answers [3]
f = open('isNowAGoodTime_queryTimes_' + str(int(time.time())) + '.csv', 'w')
f.write('time\n')
print(os.getcwd())

# set up a scheduler to pick random times to say is now a good time [1]
s = sched.scheduler(time.time, time.sleep)

# do a test question
ask_time = 2
s.enter(ask_time, 1, queryDriver, ())
s.run()

while True:
    print(time.time())
    ask_time = random.randint(30,2*60) # wait time in seconds
    print(ask_time)
    s.enter(ask_time, 1, queryDriver, ())
    s.run()

# Resources
# [1] Event scheduling - https://docs.python.org/2/library/sched.html
# [2] Speech Recognition - https://pypi.python.org/pypi/SpeechRecognition/
# [3] Writing to files - https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
# [4] Record Audio - http://people.csail.mit.edu/hubert/pyaudio/
