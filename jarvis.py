import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import random
import wikipedia as googleScrap
import webbrowser
import pywhatkit
from flask import Flask
import os
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)  
def speak(audio):
	engine.say(audio)
	engine.runAndWait()
def WishMe():
	hour = int(datetime.datetime.now().hour)
	if(hour >=0 and hour < 12):
		speak("Good Morning !")
	elif hour >= 12 and hour <16:
		speak("Good afternoon !")
	elif hour >=16 and hour <24:
		speak("Good evening")
	speak("I am Jarvis Please tell me how may I help you")
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Inside Try") 
            query = r.recognize_google(audio)
           
            print(f"User said :{query}\n")
        
        except:
            print("i didn't get that...")
           
            return "None"
    return query
if __name__ == '__main__':	
	speak("Hello Ameya how are you")
	WishMe()
	while True:
		query = takeCommand().lower()
		
		if 'wikipedia' in query:
			speak('Searching Wikipedia')
			query = query.replace("wikipedia","")
			
			try:
				results = wikipedia.summary(query,sentences = 2)
				print("Searching on Wikipedia. . . ")
				speak(("According to Wikipedia"))
				speak(results)
			
			except:
				speak("didn't found any page please search again")
				S
		elif 'jarvis you there' in query:
			speak("At you service sir")

		elif 'open youtube' in query:
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			webbrowser.open("google.com")
		
		elif 'open shares' in query:
			webbrowser.open("nseindia.com")

		elif 'about yourself' in query:
			speak("I am Jarvis i am a assistant for you,     I was created by Ameya Goonjaari on 22nd januray 2021")
		
		elif 'mail' in query:
			url = 'https://mail.google.com/mail/u/0/?tab=rm&ogbl/inbox'
			webbrowser.open_new_tab(url)
		
		elif 'legs' in query:
			url = 'https://lex.infosysapps.com/en/page/home'
			webbrowser.open_new_tab(url)
		
		elif 'hello jarvis' in query:
			speak("hello sir how can i help you ")
		
		elif 'play' in query: 
			query = query.replace("jarvis","")
			song = query.replace("play","")
			speak("playing"+ song)
			pywhatkit.playonyt(song)
		
		elif 'open javatpoint' in query:
			webbrowser.open("javatpoint.com")

		elif 'playmusic' in query:
			music_dir = 'D:\\songs'
			songs = os.listdir(music_dir)
			Rno = random.choice(len(songs))
			os.startfile(os.path.join(music_dir,songs[1]))	
		
		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"Sir, the time is {strTime}")
		
		elif 'open code' in query:
			Cpath = "C:\\Users\\Ameya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
			os.startfile(Cpath)	
		
		elif 'who is your creator' in query:
			with open("creator.txt","r") as myfile:
				data = myfile.read().splitlines()
				speak(data)		
		
		elif 'goodbye' in query:	
			speak("good bye sir have a great day")
			break
		
		elif 'google' in query:
			query = query.replace("jarvis","")
			query = query.replace("googlesearch","")
			query = query.replace("google","")
			speak("Searching on google")
			pywhatkit.search(query)
			try:
				result = googleScrap.summary(query,2)
				speak(result)
			except:
				speak("")
		elif 'tell me something about' in query:
			query = query.replace("jarvis","")
			query = query.replace("tell me something about","")
			query = query.replace("tell me something about","")
			speak("Searching on google")
			pywhatkit.search(query)
			try:
				result = googleScrap.summary(query,2)
				speak(result)
			except:
				speak("")
	print("Thank you for using Javris...")
		
