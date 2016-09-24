import time
import speech_recognition as sr
import os
import random
import sched, time
import _thread

def callback(recognizer, audio):
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source) # we only need to calibrate once, before we start listening

while True:
    print(time.time())
    ask_time = random.randint(1,3) # wait time in seconds
    print(ask_time)
    time.sleep(ask_time)
    os.system('say is now a good time?')

    #os.system,('afplay Morse.aiff',) # play a sound to let the driver know they can speak

    stop_listening = r.listen_in_background(m, callback)
    print("say something!")
    time.sleep(3)
    stop_listening()

# Resources
# [1] Event scheduling - https://docs.python.org/2/library/sched.html
# [2] Speech Recognition - https://pypi.python.org/pypi/SpeechRecognition/
# [3] Writing to files - https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
