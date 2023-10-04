#!/usr/bin/python3
import speech_recognition as sr
import pyttsx3 as tts
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import activity
from selenium import webdriver


def init():   
    #Creating an object of Recognizer class
    listen = sr.Recognizer()
    state = True
    engine = tts.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('voice','en-us')
    engine.setProperty('rate', 130)

    def talk(text):
        engine.say(text)
        engine.runAndWait()

    
    def take_command():
        try:
            # open the microphone and start recording
            with sr.Microphone() as mic:
                print("Listening...")
                # Listening to the user speech
                # Accepts the audio source as the parameter
                voice = listen.listen(mic)
                command = listen.recognize_google(voice)
                print(command)
        except sr.UnknownValueError: 
            command = "Sorry I didn't catch that."
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")    
        return str(command)


    def run_script():
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play','')
            talk('Playing '+ song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk("Current time is "+time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            pywhatkit.search(person)
            print(info)
            talk(info)
        elif 'date' in command:
            talk("Sorry I have a headache")
        elif 'activity' in command:
            talk(str(activity.get()))
        elif 'are you single' in command:
            talk('I am in relationship with a router')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'screenshot' in command:
            talk('taking screenshot of your window.')
            subprocess.run(['gnome-screenshot','-w'])
        elif 'close' in command:
            talk("it's good seeing you leaving")
            global state
            state = False
        else:
            talk("please say the command again")
        
        
    while state == True:
        run_script()        
