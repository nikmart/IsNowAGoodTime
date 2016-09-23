import speech_recognition as sr
import timeit
import os
import _thread

def processSpeech():
    _thread.start_new_thread(os.system,('afplay Morse.aiff',)) # play a sound to let the driver know they can speak

    try:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source, timeout=5.0)

        # recognize speech using Google Speech Recognition
        start_time = timeit.default_timer()
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            response = r.recognize_google(audio)
            print("Google Speech Recognition thinks you said " + response)
            os.system('afplay Pop.aiff') # play a beep when you process the response to let the driver know they were heard.
            # write audio to a WAV file
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        print("Google: " + str(timeit.default_timer() - start_time))

    except sr.WaitTimeoutError:
        print("Speech timeout, assume 'no'")


# def onEnd(name, completed):
#     processSpeech()         # listen and process the answer
#     engine.endLoop()        # stop the tts engine
#     print("finishing", name, completed)


# obtain audio from the microphone
r = sr.Recognizer()
os.system('say is now a good time?')
processSpeech()

# # initialize the speech system
# engine = pyttsx.init()
# engine.connect('finished-utterance', onEnd)
# engine.say('Is now a good time?', 'now')
# engine.startLoop()
