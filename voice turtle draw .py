import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from PIL import Image
import turtle
import time 
def listen() :

    r = sr.Recognizer()

    with sr.Microphone() as source :

        audio = r.listen(source)
        said = ""

        try :

            said = r.recognize_google(audio, language = 'th')
            print(said)

        except sr.UnknownValueError : 
            listen()

        return said

t = turtle.Turtle() 

def draw_square(color) :
   
    t.pencolor(color)

    t.fillcolor(color)
    t.begin_fill()

    t.right(90)
    t.forward(100)
    t.left(90)
    t.backward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)

    t.end_fill()
    

def draw_circle(color) :
    
    
    t.pencolor(color)
    t.fillcolor(color)
    t.pensize(5)
    t.speed(5)
    t.begin_fill()
    t.circle(90)
    t.end_fill()


def draw_triangle(color) :

    t.pencolor(color)
    t.fillcolor(color)
    t.pensize(5)
    t.speed(5)

    t.begin_fill()
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)

    t.end_fill()

def draw_star(color) :

    t.pencolor(color)
    t.fillcolor(color)
    t.pensize(5)
    t.speed(5)

    t.begin_fill() 

    for i in range(5) :

        t.forward(100)

        t.right(144)

    t.end_fill()

def draw_random(color) :

    t.pencolor(color)
    t.pensize(5)
    t.speed(5)

    for i in range( 12 ) :

        t.forward( 200 )

        t.right( 150  ) 

def clear() :
    t.clear() 

count = int(input("อยาก วาดรูปกี่ครั้ง : "))

for i in range(count) :
    print("วาดครั้งที่ {}".format(i+1)) 
    print( " อยากได้สีอะไร : ")
    color = listen()

    if color == "ชมพู" :
        color = "pink"
        
    elif color == "นำ้เงิน" or color == "ฟ้า" :
        color = "blue"

    elif color == "เหลือง" :
        color = "yellow"

    elif color == "เขียว" :
        color = "green"

    elif color == "ดำ" :
        color = "black"

    elif color == "แดง" :
        color = "red"

    elif color == "ม่วง"   :
        color = "purple"

    print("อยากได้รูปทรงอะไร : ")

    shape = listen()

    if shape == "สี่เหลี่ยม" or shape == "สี่เหลี่ียมจัตุรัส" or shape == "จัตุรัส" :
        draw_square(color)

    elif shape == "วงกลม" :
        draw_circle(color)

    elif shape == "สามเหลี่ยม" :
        draw_triangle(color)

    elif shape == "ดาว" :
        draw_star(color)

    else :

        draw_random(color) 

    time.sleep(5)
    clear()

    
