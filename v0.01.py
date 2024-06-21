import speech_recognition as sr
import os
import subprocess
from gtts import gTTS
import subprocess
from gtts import gTTS
import pyaudio


def take_query():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 0.5
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected. Please try again.")
            return "None"

    try:
        query = r.recognize_google(audio, language="en")
    except sr.UnknownValueError:
        print("Could not understand audio")
        return "None"

    return query.lower()



while True:
    query = take_query()
    print(query)