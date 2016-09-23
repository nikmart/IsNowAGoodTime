import speech_recognition as sr
import timeit
import os
import random
import sched, time
import _thread

def queryDriver():
    # write the ask time to the file
    f.write(str(time.time()) + ',')

    # obtain audio from the microphone
    r = sr.Recognizer()
    os.system('say is now a good time?')

    _thread.start_new_thread(os.system,('afplay Morse.aiff',)) # play a sound to let the driver know they can speak

    try:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source, timeout=5.0)

        # recognize speech using Google Speech Recognition [2]
        start_time = timeit.default_timer()
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            response = r.recognize_google(audio)
            print("Google Speech Recognition thinks you said " + response)
            f.write(response + '\n')
            os.system('afplay Pop.aiff') # play a beep when you process the response to let the driver know they were heard.
            # write audio to a WAV file
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            f.write('N/A,error\n')
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            f.write('N/A,error\n')
        print("Google: " + str(timeit.default_timer() - start_time))

    except sr.WaitTimeoutError:
        print("Speech timeout, assume 'no'")
        f.write('no,timeout\n')


# set up a file to log the question times and the answers [3]
f = open('isNowAGoodTime_labels' + str(int(time.time())) + '.csv', 'w')
f.write('time,label,note\n')

# set up a scheduler to pick random times to say is now a good time [1]
s = sched.scheduler(time.time, time.sleep)

while True:
    print(time.time())
    ask_time = random.randint(30,3*60) # wait time in seconds
    print(ask_time)
    s.enter(ask_time, 1, queryDriver, ())
    s.run()

# Resources
# [1] Event scheduling - https://docs.python.org/2/library/sched.html
# [2] Speech Recognition - https://pypi.python.org/pypi/SpeechRecognition/
# [3] Writing to files - https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
