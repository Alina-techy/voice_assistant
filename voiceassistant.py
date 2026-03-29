import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime
import time


# speak function
def speak(text):
    try:
        print("Assistant:", text)

        engine = pyttsx3.init()
        engine.setProperty('rate', 170)
        engine.setProperty('volume', 1.0)

        voices = engine.getProperty('voices')
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)
        elif len(voices) > 0:
            engine.setProperty('voice', voices[0].id)

        engine.say(text)
        engine.runAndWait()
        engine.stop()

        time.sleep(0.5)

    except Exception as e:
        print("Speak error:", e)


# greeting
def wish_me():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good morning")
    elif hour < 17:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am ready to help you")


# listening and recognizing
def take_command():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("\nListening...")
            r.adjust_for_ambient_noise(source, duration=1)
            r.pause_threshold = 0.8
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print("You said:", command)
        return command.lower()

    except sr.WaitTimeoutError:
        print("No speech detected.")
        return ""

    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""

    except sr.RequestError as e:
        print("Speech recognition service error:", e)
        return ""

    except Exception as e:
        print("Error:", e)
        return ""


# main part
def run_assistant():
    wish_me()

    while True:
        command = take_command()

        if command == "":
            continue

        if "youtube" in command:
            speak("Opening YouTube")
            time.sleep(1)
            webbrowser.open("https://youtube.com")

        elif "google" in command:
            speak("Opening Google")
            time.sleep(1)
            webbrowser.open("https://google.com")

        elif "chat gpt" in command or "chatgpt" in command:
            speak("Opening ChatGPT")
            time.sleep(1)
            webbrowser.open("https://chatgpt.com")

        elif "roblox" in command:
            speak("Opening Roblox")
            time.sleep(1)
            webbrowser.open("https://roblox.com")

        elif "notepad" in command:
            speak("Opening Notepad")
            time.sleep(1)
            os.system("notepad")

        elif "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}")

        elif "exit" in command or "stop" in command:
            speak("Goodbye")
            break


# run
run_assistant()