import os
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import smtplib
import main


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

engine.say("hello buddy")
engine.runAndWait()

hour = int(datetime.datetime.now().hour)

if hour < 12:
        engine.say("good morning!")
        engine.runAndWait()
elif hour >= 12 and hour < 18:
        engine.say("good after noon!")
        engine.runAndWait()
else:

    engine.say("good evening!")
    engine.runAndWait()

engine.say("I am Vaani! How can I help you sir?")
engine.runAndWait()



def speak(word):
    engine.say(word)
    engine.runAndWait()
def hearing():
    speak("I am ready")
    r = sr.Recognizer()
    with sr.Microphone() as mic:

        r.pause_threshold = 1
        audio = r.listen(mic)

        try:
            print("recognizing")
            query = r.recognize_google(audio)
            print(query)
            speak(query)
            work(query)

        except Exception as e:
            print(e)
            speak("say that again")
            hearing()
            return "none"
        return query


def what():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        audio = r.listen(mic)
        query = r.recognize_google(audio)
        z = query.lower()
        if "what" in z:
            hearing()

def sendingmail():
    sender = "abcd@cmail.com"
    receiver = "infofinders01@gmail.com"
    message = "hi"
    try:
        g = smtplib.SMTP("localhost")
        print("email sent successfully")
    except Exception as e:
        print(e)
        speak("sorry i cannot send mail")

def work(z
        ):
    x = z.lower()
    if "open youtube" in x:
        webbrowser.open("youtube.com")
        #what()
    elif "wikipedia" in x:
        speak("search in wikipedia")
        x = x.replace("wikipedia", "")
        result = wikipedia.summary(x, sentences = 3)
        speak(result)
    elif "time" in x:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak("sir, the time is"+time)
    elif "send mail" in x:
        sendingmail()
    elif "exit" in x:
        speak("by by sir. have a nice day.")
        exit()
    elif "press" in x:
        x = x.replace("press", "")
        speak(x)
        main.keyboard(x)
    elif "hold" in x:
        main.holdkey(x)
    elif "release" in x:
        main.releasekey(x)
    else:
        main.shortcut(x)



while True:
    what()

