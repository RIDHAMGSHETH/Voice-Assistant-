import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wolframalpha

# Initialize WolframAlpha client
try:
    app = wolframalpha.Client("TVR5EP-PY6UTR7EGU")
except Exception:
    print("Your internet connection is off or the API key is incorrect.")
    app = None

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    """Speaks the given text."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listens for a command and returns it."""
    command = ""
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source)
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            command = command.lower()
            if 'sunday' in command:
                command = command.replace('sunday', '')
            print(f"Recognized command: {command}")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Request error from Google Speech Recognition service.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return command

def run_sunday():
    """Executes commands based on the user's input."""
    command = take_command()
    if command:
        print(f"Command: {command}")
        if 'youtube' in command:
            song = command.replace('youtube', '').strip()
            talk(f'Playing {song}')
            pywhatkit.playonyt(song)

        elif 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            print(current_time)
            talk(f'Current time is {current_time}')
        
        elif 'hello' in command:
            talk('Hey how can i help you?')
 
        elif 'hi' in command:
            talk('Hey how can i help you?')
 
        elif 'who are you' in command:
            talk('I am Sunday, Ridham made me for speech recognition and simple tasks.')
        
        elif 'hu r u' in command:
            talk('I am Sunday, Ridham made me for speech recognition and simple tasks.')    

        elif 'how can you help' in command:
            talk('I am Sunday and i can do multiple tasks. I can tell time and temperature. I can perform tasks like playing songs on youtube')

        elif 'temperature' in command:
            if app:
                try:
                    res = app.query(command)
                    result = next(res.results).text
                    print(result)
                    talk(result)
                except Exception as e:
                    print(f"An error occurred with WolframAlpha: {e}")
                    talk("Sorry, I couldn't fetch the temperature.")
            else:
                talk("WolframAlpha client is not initialized.")
        else:
            talk("Sorry, I did not understand that command.")

if __name__ == "__main__":
    run_sunday()

