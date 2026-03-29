import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import time 

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
    except:
        print("Not understood")
        return "none"

    return command.lower()

# main function
def run_assistant():
    while True:
        command = take_command()

        if "open youtube" in command:
            speak("Opening YouTube")
            time.sleep(1)
            webbrowser.open("https://youtube.com")
            
        elif "open google" in command:
            speak("Opening Google")
            time.sleep(1)
            webbrowser.open("https://google.com")
            

        elif "roblox" in command:
            speak("Opening Roblox")
            time.sleep(1)
            webbrowser.open("https://roblox.com")
            
        elif "open notepad" in command:
            speak("Opening Notepad")
            time.sleep(1)
            os.system("notepad")
            

        elif "shutdown" in command:
            speak("Shutting down")
            os.system("shutdown /s /t 1")

        elif "exit" in command:
         speak("Goodbye")
         time.sleep(2)
         break
    
run_assistant()