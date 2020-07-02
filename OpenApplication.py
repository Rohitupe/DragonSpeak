import subprocess
import os
from SaySpeak import say

errorNumber = 0

def OpenApplication(textCommand):

    # Open Notepad
    if ("open notepad") in textCommand.lower():
        subprocess.call(r"C:\Windows\System32\notepad.exe")

    elif ("close notepad") in textCommand.lower():
        errorNumber = os.system("TASKKILL /F /IM notepad.exe")
        if errorNumber == 128:
            say("Application Notepad is not Running")

    # Open WordPad
    elif ("open wordpad") in textCommand.lower():
        subprocess.Popen(r"C:\Windows\System32\write.exe")

    elif ("close wordpad") in textCommand.lower():
        errorNumber = os.system("TASKKILL /F /IM wordpad.exe")
        if errorNumber == 128:
            say("Application Wordpad is not Running")

    # Open Calculator
    elif ("open calculator") in textCommand.lower():
        subprocess.call(r"C:\Windows\System32\calc.exe")

    elif ("close calculator") in textCommand.lower():
        errorNumber = os.system("TASKKILL /F /IM Calculator.exe")
        if errorNumber == 128:
            say("Application Calculator is not Running")

    # Open File manager
    elif ("open filemanager") in textCommand.lower():
        subprocess.call(r"C:\Windows\explorer.exe")

    elif ("close filemanager") in textCommand.lower():
        errorNumber = os.system("TASKKILL /F /IM explorer.exe")
        if errorNumber == 128:
            say("Application filemanager is not Running")

    else:
        say("Application is Not Installed")

OpenApplication("Please close filemanager For me")