import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import os
import pyjokes

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    elif hour>=18 and hour<24:
        speak("Good Evening!") 

    speak("Loading your AI desktop assistant saturday")
    speak("hi Boss how can I help you")

def goodwish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    elif hour>=18 and hour<21:
        speak("Good Evening!") 

    elif hour>=21 and hour<24:
        speak("Good Night!") 


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.energy_threshold=5000
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query =r.recognize_google(audio, language='en-in')
        print(F"user said: {query}\n")    
        
    except Expection as e:
        print("say that again please.....")
        return"None"

    return query   

def tellday():
    day=datetime.datetime.today().weekday()+1

    Day_dict ={1:'Monday',2:'Tuesday',
               3:'Wednesday',4:'Thursday',
               5:'Friday',6:'Saturday',
               7:'Sunday'}

    if  day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)     
    
        


if __name__ == "__main__":
    wishMe()
    while True:
         query = takeCommand().lower()

         if'wikipedia'in query:
          speak('Searching Wikipedia.....')
          query = query.replace("wikipedia","") 
          results = wikipedia.summary(query,sentences=3)
          speak("According to Wikipedia")
          print(results)
          speak(results)

         elif 'open youtube'in query:
             speak("Opening")
             webbrowser.open("https://www.youtube.com")

         elif 'open google'in query:
             speak("Opening")
             webbrowser.open("https://www.google.com")

         elif 'open instagram'in query:
             speak("Opening")
             webbrowser.open("https://www.instagram.com") 

         elif 'open facebook'in query:
             speak("Opening")
             webbrowser.open("https://www.facebook.com")  

         elif 'open stack overflow'in query:
             speak("Opening")
             webbrowser.open("stackoverflow.com")

         elif 'open white'in query or 'open hat' in query:
            speak("Opening")
            webbrowser.open("https://code.whitehatjr.com/s/dashboard")     
     

         elif'search' in query:
             speak("searching stuffs")
             query=query.replace('search', '')
             webbrowser.open(query)
             
         elif'play' in query:
             song = query.replace('play', '')   
             speak("playing")
             pywhatkit.playonyt(song)

         elif'time' in query:
             strftime = datetime.datetime.now().strftime('%I:%M:%p')
             speak(F"current time is{strftime}")
             print(strftime)

         elif'which day it is' in query:
             tellday()
             
         elif'open code' in query:
             speak("opening")
             codePath=("C:\\Users\\Alok Thakur\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
             os.startfile(codePath)

         elif'open edge' in query:
             speak("opening")
             codePath=("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
             os.startfile(codePath)
  
         elif'open chrome' in query:
             speak("opening")
             codePath=("C:\\Users\\Alok Thakur\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe")
             os.startfile(codePath) 

         elif'open pad' in query:
             speak("opening")
             codePath=("C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe")
             os.startfile(codePath)  

         elif'open note' in query:
             speak("opening")
             codePath=("C:\\WINDOWS\\system32\\notepad.exe")
             os.startfile(codePath)
                
         elif'hey Saturday'in query or'ok saturday'in query:
             speak("yes,boss")
             goodwish()
             tellday() 

         elif'news' in query:
             speak("Here are some headlines from the Times of India,Happy reading")
             news=webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")

         elif 'who are you' in query or 'what can you do' in query:
            speak('I am saturday version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')


         elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by alok")
            print("I was built by alok") 

         elif"weather" in query:
             speak('the weather is')
             query=query.replace('weather', 'weather')  
             webbrowser.open_new_tab("https://www.accuweather.com/en/in/india-weather")

         elif'tell me joke' in query:
             speak(pyjokes.get_joke())
            
         elif 'what is' in query:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question=takeCommand()
            app_id="116520373733101470833 "
            client = console.cloud.google.Client('f0c89df3c839521e2b9ef6b0ac0c2f7afe4b1f2f')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)    


         elif "good bye" in query or "ok bye" in query or "ok quit" in query or 'let drink water' in query or 'time to eat' in query:
             goodwish()
             speak('your desktop  assistant saturday is shutting down,ok bye')
             print('your desktop assistant saturday is shutting down,ok bye')
             break      

         
			   





        



    
  
