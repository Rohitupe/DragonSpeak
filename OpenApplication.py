import subprocess
import os
from SaySpeak import say

errorNumber = 0

def OpenApplication(textCommand):

    # Open Notepad
    if ("open notepad") in textCommand.lower():
        subprocess.Popen(r"C:\Windows\System32\notepad.exe")

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
        subprocess.Popen(r"C:\Windows\System32\calc.exe")

    elif ("close calculator") in textCommand.lower():
        errorNumber = os.system("TASKKILL /F /IM Calculator.exe")
        if errorNumber == 128:
            say("Application Calculator is not Running")

    # Open Code
    elif ("open code") in textCommand.lower():
        subprocess.Popen(r"C:\Program Files (x86)\Microsoft VS Code\Code.exe")

    elif ("close code") in textCommand.lower():
        errorNumber = os.system("TASKKILL /F /IM Code.exe")
        if errorNumber == 128:
            say("Application code is not Running")

    # Open Skype
    elif ("open skype") in textCommand.lower():
        subprocess.Popen(r"C:\Program Files\WindowsApps\Microsoft.SkypeApp_15.61.100.0_x86__kzf8qxf38zg5c\Skype\Skype.exe")
    elif ("close skype") in textCommand.lower():
        errorNumber = os.system("TASKKILL /F /IM Skype.exe")
        if errorNumber == 128:
            say("Application Skype is not running")

    else:
        say("Application is Not Installed")

# OpenApplication("Please close skype For me")