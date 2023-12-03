import pyttsx3
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('rate', 200)
engine.setProperty('voice', voices[1].id)


def Speak(*args, **kwargs):
    audio = ""
    for i in args:
        audio += str(i)
    print(audio.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
    engine.say(audio)
    engine.runAndWait()

Speak("कृपया मेरे चैनल को सब्सक्राइब करें")
