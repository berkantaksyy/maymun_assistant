from datetime import datetime
import webbrowser
import speech_recognition as sr
import time
from gtts import gTTS as gt
from playsound import playsound as ps
import random
import os


catch = sr.Recognizer()

def record(ask = False):

    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = catch.listen(source)
        voice = ""
        try:
            voice = catch.recognize_google(audio , language="tr-TR")
        except sr.RequestError:
            speak("Bir hata oldu")
        except sr.UnknownValueError:
            speak("Bana bu kelimeyi öğretmediniz")
        return voice

def response(voice):
    if "maymun" in voice:
        speak("Efendim, berkant")
    if "nasılsın" in voice:
        speak("Teşekkürler, sen nasılsın")
    if "Sen kimsin" in voice:
        speak("benim ismim maymun beni berkant tasarladı")
    if "hayat nasıl gidiyor" in voice:
        speak("Hayat dediğin nedir ki gülüm vur birini değiştir ötekini")
    if "saat kaç" in voice:
        speak(datetime.now())
    if "arama yap" in voice:
        search = record("ne arama yapmak istiyorsun")
        url = "https://google.com/search?q= " + search
        webbrowser.get().open(url)
        print(search + " için bulduklarım")
    if "maymun kapan" in voice:
        speak("görüşürüz berkant")
        exit()

def speak(string):
    tts = gt(string,lang="tr")
    rand = random.randint(1,10000)
    file = "audio-"+str(rand)+".mp3"
    tts.save(file)
    ps(file)
    os.remove(file)


speak("Nasıl Yardımcı Olabilirim")
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)


