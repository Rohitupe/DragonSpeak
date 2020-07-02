import getpass   # get user name of person using this pc
import pyttsx3  # text to speech


userName = ""
try:
    userName = getpass.getuser()
except:
    userName = "User"


def say(text):
    """ say function for all voice message"""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

