import speech_recognition as sr
import timeit
import os
import random
import sched, time
import _thread
import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

# record the audio after a question is asked [4]
def recordAudio():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    output_file = str(time.time()) + "_answer.wav"
    wf = wave.open(output_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def queryDriver():
    # write the ask time to the file
    f.write(str(time.time()) + '\n')

    os.system('say is now a good time?')

    _thread.start_new_thread(os.system,('afplay Morse.aiff',)) # play a sound to let the driver know they can speak

    recordAudio()


# set up a file to log the question times and the answers [3]
f = open('isNowAGoodTime_queryTimes' + str(int(time.time())) + '.csv', 'w')
f.write('time')

# set up a scheduler to pick random times to say is now a good time [1]
s = sched.scheduler(time.time, time.sleep)

while True:
    print(time.time())
    ask_time = random.randint(1,3) # wait time in seconds
    print(ask_time)
    s.enter(ask_time, 1, queryDriver, ())
    s.run()

# Resources
# [1] Event scheduling - https://docs.python.org/2/library/sched.html
# [2] Speech Recognition - https://pypi.python.org/pypi/SpeechRecognition/
# [3] Writing to files - https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
# [4] Record Audio - http://people.csail.mit.edu/hubert/pyaudio/
