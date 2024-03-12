import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr
import concurrent.futures
import wikipedia


#used to take voices from window
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


#converts text to audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# wishes me whenever the program is runned
def wish():
    hour=int(datetime.datetime.now().hour)
    if 0<hour<12:
        speak("Good morning")
    elif 12<=hour<18:
        speak("Good afternoon")
    else:
         speak("Good evening")
    speak("Its good to see you. please tell me how may i help you")


def takecommand():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening")
        recognizer.adjust_for_ambient_noise(source, duration = 1)  # Adjust for ambient noise
        try:
            audio = recognizer.listen(source, timeout=5)
        except sr.WaitTimeoutError:
                print("Speech recognition time out.")
                return None
    try:
        # Use Google Web Speech API to recognize speech
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()  # Convert the command to lowercase for easier comparison
    except sr.UnknownValueError as e:
        print(f"could not understand audio.")
        return "nothing"
    

# runs when the program is runned
if __name__ == "__main__":
    wish()
    while True:
        query=takecommand()
        #logic to executing the task based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
        elif 'explosive' in query:
            speak("Opening the mine game")
            webbrowser.open("minesweeper-pro.com")
        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open("google.com")
        elif 'the time' in query:
            strTime =datetime.datetime.now().strftime("%H:%M")
            speak(f" sir time is {strTime}")
        elif 'nothing' in query:
            speak("i m waiting")
        elif 'stop' in query:
            exit(0)
