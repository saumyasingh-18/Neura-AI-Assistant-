import speech_recognition as sr
import os
import webbrowser
import datetime
import pyttsx3
import google.generativeai as genai
from config import gemini_key  

genai.configure(api_key=gemini_key)

chatStr = ""
engine = pyttsx3.init()

def say(text):
    engine.say(text)
    engine.runAndWait()

def chat(query):
    global chatStr
    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        response = model.generate_content(query)
        reply = response.text
    except Exception as e:
        print("Error:", e)
        reply = "Sorry, I couldn’t connect to my AI brain."

    chatStr += f"User: {query}\nNeura: {reply}\n"
    print("Neura:", reply)
    say(reply)
    return reply

def ai(prompt):
    text = f"Local AI response for Prompt: {prompt}\n*************************\n\n"
    text += "This was saved using Gemini AI."

    if not os.path.exists("NeuraAI"):
        os.mkdir("NeuraAI")

    filename = f"NeuraAI/{prompt[:20].replace(' ', '_')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...\n\n")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception:
            return "Some Error Occurred. Sorry from Neura"

if __name__ == '__main__':
    print('Welcome to Neura!')
    say("Welcome to, Speech to text recognition, My name is Neura, and I can do various type of tassks ")
    
    while True:
        print("Listening........")
        query = takeCommand()

        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"],
        ]
        for site in sites:
            if f"open {site[0]}" in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "open music" in query.lower():
            musicPath = "C:/Users/victus/Downloads/downfall-21371.mp3" 
            os.startfile(musicPath)

        elif "the time" in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Sir, the time is {hour} hours and {minute} minutes")

        elif "using artificial intelligence" in query.lower():
            ai(prompt=query)

        elif "neura quit" in query.lower():
            say("Goodbye sir!")
            exit()

        elif "reset chat" in query.lower():
            chatStr = ""
            say("Chat history cleared!")

        else:
            print("Chatting...")
            chat(query)
