import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from PIL import Image
import webbrowser


def speak(text) :
    tts = gTTS(text = text , lang = "en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def listen() :

    r = sr.Recognizer()

    with sr.Microphone() as source :

        audio = r.listen(source)
        said = ""

        try :

            said = r.recognize_google(audio, language = 'th')
            print(said)

        except sr.UnknownValueError :
            #print("เราไม่เข้าใจอะ พูดใหม่เถอะ")
            #speak("เราไม่เข้าใจอะ พูดใหม่เถอะ")
            listen()

        return said

speak("Black Pink")

val = listen()

while val != "หยุด" :

    if val == "รักติดไซเรน" :
        print("เดี๋ยวเรา จะเล่นเพลง {} ให้ฟัง ".format(val))
        speak("เดี๋ยวเรา จะเล่นเพลง" + val + "ให้ฟัง")
        
        webbrowser.open('https://youtu.be/ILU9NbWn4t0')

    elif val == "ประยุทธ์" or val == "คสช":
        print("เดี๋ยวเรา จะเล่นเพลง {} ให้ฟัง ".format(val))
        speak("เดี๋ยวเรา จะเล่นเพลง" + val + "ให้ฟัง")
        webbrowser.open('https://www.youtube.com/watch?v=gQH2P7-HG3I')
        
        

    elif val == "ดูดูดู"or val == "แบล็คพิ้งค์" or val == "Black Pink"  :
        print("เดี๋ยวเรา จะเล่นเพลง {} ให้ฟัง ".format(val))
        speak("เดี๋ยวเรา จะเล่นเพลง" + val + "ให้ฟัง")
        webbrowser.open('https://www.youtube.com/watch?v=IHNzOHi8sJs')
       
        
    elif val == "ดี๊ดี":
        print("เดี๋ยวเรา จะเล่นเพลง {} ให้ฟัง ".format(val))
        speak("เดี๋ยวเรา จะเล่นเพลง" + val + "ให้ฟัง")
        webbrowser.open('https://www.youtube.com/watch?v=8Z9kRAy2G_4')

    elif val == "เพลงชาติ" :
        print("เดี๋ยวเรา จะเล่นเพลง {} ให้ฟัง ".format(val))
        speak("เดี๋ยวเรา จะเล่นเพลง" + val + "ให้ฟัง")
        webbrowser.open('https://www.youtube.com/watch?v=YTgVDlE1HII')

    elif val!= "หยุด" :
        print("เดี๋ยวเรา จะเล่นเพลง {} ให้ฟัง ".format(val))
        speak("เดี๋ยวเรา จะเล่นเพลง" + val + "ให้ฟัง")
        webbrowser.open('https://www.youtube.com/watch?v=YTgVDlE1HII')  

    val = listen()



for i in range ( 3 ) :
    song = input("เพลงที่คุณชอบ เพลงที่ {} : ".format( i + 1 ))

    print("ว้าว !!! เราก็ชอบฟัง {} เหมือนกัน ".format(song))

    speak("ว้าว !!! เราก็ชอบฟัง {} เหมือนกัน ".format(song))

