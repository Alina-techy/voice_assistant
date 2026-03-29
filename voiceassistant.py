import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import time

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.5)  

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print("You said:", command)
    except:
        print("Not understood")
        return "none"

    return command.lower()

def run_assistant():
    speak("Assistant started")

    while True:
        command = take_command()

        if command == "none":
            continue
        
        if "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "chatgpt" in command:
            speak("Opening ChatGPT")
            webbrowser.open("https://chatgpt.com")

        elif "roblox" in command:
            speak("Opening Roblox")
            webbrowser.open("https://www.roblox.com")

        elif "open" in command:
            app = command.replace("open", "").strip()
            speak(f"Opening {app}")
            time.sleep(1)

            try:
                os.system(app)
            except:
                speak("Application not found")

        elif "exit" in command or "quit" in command:
            speak("Goodbye")
            time.sleep(1)
            break

run_assistant()