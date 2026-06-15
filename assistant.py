import time
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import subprocess
import smtplib
import random
from dotenv import load_dotenv
load_dotenv()



engine = pyttsx3.init('sapi5')

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 150)  

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am varshini Assistant. How can I help you?")
def username():
    speak("What should i call you")
    uname = takeCommand()
    print("Welcome ", uname)
    speak(f"welcome {uname}")
     
    speak("How can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
    
    try:
        print("Recognizing....")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    try:
        print("Sending email...")
        sender_email = os.getenv("EMAIL_USER")
        sender_password = os.getenv("EMAIL_PASS")

        if not sender_email or not sender_password:
            raise RuntimeError("Email credentials not set")


        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to, content)
        print("Email sent successfully.")
    except Exception as e:
        print(e)
        speak("Sorry, I was unable to send the email.")
        print("Error while sending email:", e)


if __name__=="__main__":
    wishMe()
    username()
    while True:
        query =takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'how are you' in query:
            print("I am fine Thank you\n")
            speak("I am fine Thank you")
            print("How are you, Sir\n")
            speak("How are you, Sir")

        elif 'fine' in query or 'good'   in query:
            print("It's good to know that your fine\n")
            speak("It's good to know that your fine")

        elif "who made you" in query or "who created you" in query:
            print("I have been created by team of software engineers\n")
            speak("I have been created by team of software engineers")

        elif 'open youtube' in query:
            print("Opening YouTube\n")
            speak("Opening YouTube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            print("Opening Google\n")
            speak("Opening Google")
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            song_path = r"C:\Users\sivac\Music\[iSongs.info] 01 - Langa Vonilo.mp3"
            subprocess.Popen(['C:\\Program Files\\Windows Media Player\\wmplayer.exe', song_path])
        elif 'joke' in query:
            jk = random.randint(0, 5)
            if jk == 0:
                print("What do you call a boomerang that won’t come back?")
                speak("What do you call a boomerang that won’t come back?")
                print("stick")
                speak("stick")

            elif jk == 1:
                print("What time is it when the clock strikes 13?")
                speak("What time is it when the clock strikes 13?")
                print("Time to get a new clock.")
                speak("Time to get a new clock.")

            elif jk == 2:
                print("What is a computer's favorite snack?")
                speak("What is a computer's favorite snack?")
                print("Computer chips.")
                speak("Computer chips.")

            elif jk == 3:
                print(" What kind of tree fits in your hand?")
                speak(" What kind of tree fits in your hand?")
                print("Palm tree")
                speak("Palm tree")

            elif jk == 4:
                print("What's red and smells like blue paint?")
                speak("What's red and smells like blue paint?")
                print("Red paint!")
                speak("Red paint!")

            elif jk == 5:
                print("I'm so good at sleeping I can do it with my eyes closed!")
                speak("I'm so good at sleeping I can do it with my eyes closed!")

            speak("hahhahaha")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                print("Captured content:", content)  # Log the content
                to = "practicemail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent successfully.")
            except Exception as e:
                print("Error while sending email:", e)
                speak("Sorry, I was unable to send the email.")
        elif 'exit'  in query:
            print("See you later. Have a nice day.\n")
            speak("See you later. Have a nice day.")
            print("Exiting assistant...")
            exit()
        else:
            print("Oops! My Team forgot to add this function in me ,please try another \n")
            speak("Oops! My Team forgot to add this function in me ,please try another ")

