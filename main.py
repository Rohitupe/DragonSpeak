""" Dragon Commang Line Program """
import pyttsx3  # text to speech
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import getpass   # get user name of person using this pc
userName = getpass.getuser()

def say(text):
    """ say function for all vioce message"""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speakAndwish(messsage):
    """Speak Function and Wish user with his name"""
    say(messsage)

    hour  = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        say(f"Hello, {userName} Good Morning!")
    elif hour >= 12 and hour < 18:
        say(f"Hello, {userName} Good Afternoon!")
    else:
        say(f"Hello, {userName} Good Evening!")

# take command from microphone
def command():
    """ try to speak something with your microphone to perform the action """
    recognize = sr.Recognizer()
    with sr.Microphone() as s:
        say("listening ...")
        audio = recognize.listen(s)

    try:
        say("Wait.. Recognizing the Command")
        speak = recognize.recognize_google(audio,language='en-in')
        print(f"Command : {speak}\n")

    except:
        say("you didn't speak anything")

speakAndwish("Initializing.....")
command()

