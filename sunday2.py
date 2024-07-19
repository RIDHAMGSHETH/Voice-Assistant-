#project sunday
import speech_recognition as sr
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os
import pywhatkit


#text to speech

engine = pyttsx3.init('sapi5')
voice =  engine.getProperty('voices')
#print(voice)
engine .setProperty('voice', voice[1].id)

def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >- 0 and hour < 12:
        speak("Good morning sir, how can i help you")
    elif hour>-12 and hour<18 :
        speak('Good afternoon sir, i am ready to help you')
    else:
        speak('Good night sir, working hard nice, how may i help you')


def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        audio = r.listen(source)
    try:
        print("Recognising...")
        text = r.recognize_google(audio, language='en-in')
        print(text)
    except Exception:
        speak("Sorry sir, i am not getting it")
        print("Error")
        return "none"
    return text


#main function
if __name__ == "__main__":
    wish()
    while True:
        query = takecom().lower()

        if 'wikipedia' in query:
            speak('searching on wikipedia... just a moment')
            query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        elif 'how can you help me' in query:
            speak('you can ask me anything')
        elif 'who are my family members':
            speak('Your family members are your sister, mother, and father')
        elif 'open youtube' in query or 'open video online' in query:
            webbrowser.open("www.youtube.com")
            speak('opening youtube')
        elif 'open google' in query:
            webbrowser.open("www.google.co.in")
            speak('opening google')
        elif 'goodbye' in query:
            speak('Good bye sir')
            exit()
        elif "shutdown my pc" in query:
            speak('Shutting down')
            os.system('shutdown -s')
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)
        elif 'who are you' in query:
            speak('I am sunday, Ridham made me to help his things done')
        elif 'youtube' in query:
            song = query.replace('play',  '')
            speak('playing' + song)
            pywhatkit.playonyt(song)

