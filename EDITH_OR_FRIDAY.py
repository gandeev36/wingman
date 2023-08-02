import pyttsx3 # to install it: pip install pyttsx3 == text data into speech using python
import datetime 
import speech_recognition as sr # pip install SpeechRecognition in CMD == Speech from mic to text
import smtplib
from secrets import senderemail, epwd, to 
from email.message import EmailMessage
import pyautogui
import webbrowser as web
from time import sleep
import wikipedia
import pywhatkit as py
import requests
from newsapi import NewsApiClient
import clipboard
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import os
import copy
import time as tt
import string
import random
import pyjokes
import cv2
from speedtest import Speedtest
import numpy as np
import PyPDF2
import sys
from tkinter import *
from tkinter import filedialog
import twilio
from flask import Flask , request, Response
from twilio.twiml.voice_response import VoiceResponse

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    #print(voices[1].id)

    if voice == 1:
        engine.setProperty('voice',voices[0].id)
        speak("This is EDITH")

    if voice == 2:
        engine.setProperty('voice',voices[1].id)
        speak("This is FRIDAY")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") # I = hour, M = minutes, S = seconds
    speak(Time)

def Date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
   #speak("The current date is: ")
   #speak(date)
   #speak(month)
   #speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("good morning sir!")
    elif hour >= 12 and hour <18:
        speak("good afternoon sir!")
    elif hour >= 18 and hour < 24:
        speak("good evening sir!")
    else:
        speak("good night sir!") 
def wishme():
    speak("Welcome back sir")
    time()
    Date()
    greeting()
    speak("EDITH at your service, please tell me how can i help you?")

#while True:
#    voice = int(input("Press 1 for male voice\nPress 2 for female voice\n"))
#    speak(audio)
#    getvoices(voice)
#wishme()

def takeCommandCMD():
    query = input("please tell me how can i help you?")
    return query
def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("recognizing...")
        query = r.recognize_google(audio , language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return"None"
    query = query.lower()
    return query

def sendEmail(receiver, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    server.send_message(email)
    server.close()

def sendwhatsmsg(phone_no, message):
    Message = message
    web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('Enter')

def searchgoogle():
    speak('what should i search for?')
    search = takeCommandMic()
    web.open('https://www.google.com/search?q='+search)

def news():
    newsapi = NewsApiClient(api_key ='ca017f40be5a4a58a57b30e2c6ed1173')
    speak('what topic you need news about?')
    topic = takeCommandMic()
    data = newsapi.get_top_headlines(q = topic,
                                    language = 'en',
                                    page_size= 5)
            
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))
    speak("that is for now i'll update you in some time" )


def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)

def covid():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')

    data = r.json()
    covid_data = f'Confirmed cases : {data["cases"]} \n Deaths :{data["deaths"]} \n Recovered {data["recovered"]}'
    print(covid_data)
    speak(covid_data)

def screenshot():
    name_img = tt.time()
    name_img = f'D:\\Gandeev\\MINOR PROJECT\EDITH\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen = 8
    s =[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)
def  TaskExecution():
    pyautogui.press('esc')
    speak("verification successful")
    speak("welcome back gandeev sir")
    wishme()
    getvoices(1)
    
    while True:
        query = takeCommandMic().lower()
 
        if 'time' in query:
          time()
            
        elif 'date' in query:
           Date()

        elif 'email' in query:
            email_list = {
                'test mail':'19211a05j7@bvrit.ac.in'
            }
            try:
                speak('to who woud you like to send mail sir?')
                name = takeCommandMic()
                receiver = email_list[name]
                speak ('what is the subject of the mail?') 
                subject = takeCommandMic()
                speak('What should i say?')
                content = takeCommandMic()
                sendEmail(receiver, subject, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send the email")
        elif "open phone camera" in query:
            import urllib.request
            import cv2 #pip install opencv-python
            import numpy as np #pip install numpy
            import time
            URL= "https://192.168.1.39:8080/shot.jpg"
            while True:
                img_arr = np.array(bytearray(urllib.request.urlopen (URL).read()),dtype=np.uint8)
                img=cv2.imdecode(img_arr, -1)
                cv2.imshow('IPWebcam', img)
                q=cv2.waitKey(1)
                if q == ord("q"):
                    break;
            cv2.destroyAllWindows()
        elif 'message' in query:
            user_name ={
                'yes':'+91 70935 55295'
            }
            try:
                speak('to who woud you like to send whats app message sir?')
                name = takeCommandMic()
                phone_no = user_name[name]
                speak ('what is the message?') 
                message = takeCommandMic()
                sendwhatsmsg(phone_no, message)
                speak("message has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send the message")
        
        elif 'wikipedia' in query:
            speak('Searching on wikipedia...')
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)

        elif 'search' in query:
            searchgoogle()
            
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            mm = int(datetime.datetime.now().minute)
            if nn==14 & mm==52: 
                music_dir = 'D:\\MUSIC'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
        
        elif "internet speed test" in query:
            st = Speedtest()
            print("sir your connection's download speed is:",st.download())
            speak("sir your connection download speed is")
            print("and your connection's upload speed is:",st.upload())
            speak("and your connection's upload speed is:")


        elif "my location" in query:
            print("wait sir, let me check")
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak("sir i am not sure , but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir, due to network issue i am not able to find where we are.")
                pass
        
        elif "volume up" in query:
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")

        elif "volume mute" in query:
            pyautogui.press("volumemute")

        elif 'youtube' in query:
            speak('What should i search on youtube?')
            topic = takeCommandMic()
            py.playonyt(topic)

        elif 'weather' in query:
            url='https://api.openweathermap.org/data/2.5/weather?q=hyderabad&units=imperial&appid=6ec04386fef28f7818162497d98c4789'

            res = requests.get(url)
            data = res.json()

            weather = data['weather'] [0] ['main']
            temp = data['main']['temp']
            desp =data['weather'] [0] ['description']
            temp = round((temp - 32) * 5/9)
            print(weather)
            print(temp)
            print(desp)
            speak ('Temperature : {} degree celcius'.format(temp))
            speak('weather is {}'.format(desp))

        elif 'news' in query:
            news()
        
        elif 'read' in query:
            text2speech()

        elif 'covid' in query:
            covid()            

        elif 'screenshot' in query:
            screenshot()
            
        elif 'open' in query:
            os.system('explorer C://{}'.format(query.replace('Open','')))
        
        elif 'timer' in query or 'stopwatch' in query:
            speak("For how many minutes?")
            timing = takeCommandMic()
            timing =timing.replace('minutes', '')
            timing = timing.replace('minute', '')
            timing = timing.replace('for', '')
            timing = float(timing)
            timing = timing * 60
            speak(f'I will remind you in {timing} seconds')

            sleep(timing)
            speak('Your time has been finished sir')
        
        elif "record screen" in query:
            SCREEN_SIZE =(1920, 1080)
            fourcc = cv2.VideoWriter_fourcc(*"XVID")
            out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))
            while True:
                img = pyautogui.screenshot()
                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                out.write(frame)
                if cv2.waitKey(1) == ord("q"):
                    break
            cv2.destroyAllWindows()
            out.release()

        elif 'open code' in query:
            codepath = 'D:\\Gandeev\\MINOR PROJECT\\EDITH\\Code.exe'
            os.startfile(codepath)

        elif 'remember that' in query:
            speak('what should i remember that')
            data = takeCommandMic()
            speak("you said to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "command prompt" in query:
            os.system("start cmd")

        elif "camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "D:\\MUSIC"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))


        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            
        elif 'pdf reader' in query:
            pdfReader = PyPDF2.PdfFileReader(open('harry_potter_and_the_cursed_chi_-_j.k._rowling.pdf', 'rb'))
            speaker = pyttsx3.init()
            for page_num in range(pdfReader.numPages):
                text = pdfReader.getPage(page_num).sxtractText()
                speaker.say(text)
                speaker.runAndWait()
            speaker.stop()
            speaker.save_to_file(text, 'audio.mp3')
            speaker.runAndWait()

        elif 'do you know anything' in query:
            remember = open('data.txt','r')
            speak("you told me to remember that "+remember.read())
            
        elif 'password' in query:
            passwordgen()

        elif 'offline' in query:
            quit()

if __name__ == "__main__": #main program
    recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
    recognizer.read('trainer/trainer.yml')   #load trained model
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

    font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


    id = 2 #number of persons you want to Recognize


    names = ['','GANDEEV']  #names, leave first empty bcz counter starts from 0


    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
cam.set(3, 640) # set video FrameWidht
cam.set(4, 480) # set video FrameHeight

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

# flag = True

while True:

    ret, img =cam.read() #read the frames using the above created object

    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

    faces = faceCascade.detectMultiScale( 
        converted_image,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

        id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

        # Check if accuracy is less them 100 ==> "0" is perfect match 
        if (accuracy < 100):
            id = names[id]
            accuracy = "  {0}%".format(round(100 - accuracy))
            TaskExecution()

        else:
            id = "unknown"
            accuracy = "  {0}%".format(round(100 - accuracy))
            speak("user authentication is failed")
            
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break;

# Do a bit of cleanup
print("Thanks for using this program, have a good day.")
cam.release()
cv2.destroyAllWindows()

while True:
        permision = takeCommandMic()
        if "wake up" in permision:
            TaskExecution()
        elif "goodbye" in permision:
            speak("thanks for using me sir and have a good day")
            sys.exit()