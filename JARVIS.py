# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:05:52 2020
@author: GD
"""
try:
    #Imorting all the libraries required
    import win32com.client as wincl
    import speech_recognition as sr
    from googlesearch import search
    from playsound import playsound
    #import pywhatkit as kit
    from Trainaries_v1 import *
    import serial
    import datetime
    import wikipedia
    import webbrowser
    import argparse
    import smtplib
    import requests
    import random
    import imutils
    import pyjokes
    import pyglet
    import cv2
    import os
    import tkinter as tk
    from time import sleep
except Exception as e:
    print(e)


#Instalizing datetime
try:
    cur = datetime.datetime.now()
    Dt = ("day",cur.day,'month ',cur.month,"and year is",cur.year)
    Tm = (cur.hour,"hours",cur.minute,"minutes and ",cur.second,"seconds")
    hr=(cur.hour)
    mn=(cur.minute)
except Exception as e:
    print(e)
#Instalizing Speech Engine

speak=wincl.Dispatch("Sapi.SpVoice")


#Defining to check the Network Connection
def isconnected():
    output("Checking Network...")
    url="http://www.kite.com"
    try:
        requests.get(url, timeout=5)
        output("Connected")
    except (requests.exceptions.ConnectionError, requests.Timeout) as exception:
        output("Check your internet connection , I am designed to run online")

#Definig wikipedia to think an give answer
def find_and_say(a):
    try:
        #print("🤔")
        speak.speak("Thinking..")
        x=wikipedia.summary(a,sentences=1)
        output(x)
    except Exception as e:
        print(str(e))
        speak.speak(str(e))
        
#Defining voive recognizing engine
def recognize(o):
    if voico == 'T':
        r=sr.Recognizer()
        with sr.Microphone() as source:
            if o==0:
                try:
                    print("........")
                    audio = r.listen(source)
                    print('...')
                    text = r.recognize_google(audio)
                    x = '{}'.format(text)
                    print("You : ",x)
                    y=x.lower()
                    return y
                except Exception:
                    pass
            else:
                try:
                    playsound('process/sounds/gun.wav')
                    print("Listening...")
                    audio = r.listen(source)
                    print('Recognizing...')
                    text = r.recognize_google(audio)
                    x = '{}'.format(text)
                    print("You : ",x)
                    y=x.lower()
                    return y
                except Exception:
                    output("I didnt get you , please try again!")
                    pass
    else:
        x=str(input("cmd: "))
        y = x.lower()
        return y

#Instalizing Speech Engine
speak=wincl.Dispatch("Sapi.SpVoice")

#Defining the output
def output(o):
    global render
    render=o
    print(o)
    speak.speak(o)



#Instalizing Google
def google():
    output("Connecting Google...")
    output("What is the query that i have to search in google for?")
    query = recognize(1)
    output("Enter the number of querries to search!")
    no=int(input("Enter : "))
    #print("🧐")
    output("Searching..")
    
    i=1    
    for j in search(query,tld='com',num=no,stop=no,pause=2):
        print('[',i,']',j)
        i+=1
    output("These are the top results")

#Instalizing Vide Stream
def stereo(o):    
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", type=str, default="",
    	help="path to (optional) input video file")
    ap.add_argument("-o", "--output", type=str, default="",
    	help="path to (optional) output video file")
    ap.add_argument("-d", "--display", type=int, default=1,
    	help="whether or not output frame should be displayed")
    args = vars(ap.parse_args())
    
    
    # initialize the video stream and pointer to output video file
    #print("[INFO] accessing video stream...")
    vs = cv2.VideoCapture(args["input"] if args["input"] else 0)
    writer = None
    
    while True:
    	(grabbed, frame) = vs.read()
    
    	if not grabbed:
    		break
    
    	
    	frame = imutils.resize(frame, width=500)
    
    
    	
    	violate = str(o)
    	text = "JARVIS: {}".format(violate)
    	cv2.putText(frame, text, (10, frame.shape[0] - 25),
    		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0, 255), 2)
    
    	if args["display"] > 0:
    		cv2.imshow("Processor", frame)
    		key = cv2.waitKey(1) & 0xFF
    		if key == ord("q"):
    			break
    
    	if args["output"] != "" and writer is None:
    		fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    		writer = cv2.VideoWriter(args["output"], fourcc, 25,
    			(frame.shape[1], frame.shape[0]), True)
    
    	
    	if writer is not None:
    		writer.write(frame)
            
#Instalizing password generator
def pswrg_genrtr():
    global render
    lower="abcdefghijklmnopqrstuvwxyz"
    upper =lower.upper()
    numbers="1234567890"
    symbols="!@#$%^&*_-+=|\}]{[;<>,./?"
    
    all1=lower+upper+numbers+symbols
    all2=numbers
    speak.speak("Enter 0 for pin type password and 1 for general type password!!")
    d=int(input("Enter 0 for pins and 1 for general password: "))
    if d==0:
        all=all2
    else:
        all=all1
    speak.speak("Enter the length of the password to be generated")
    length=int(input("Enter the length: "))
    password="".join(random.sample(all,length))
    speak.speak("This can be on of the strongest passwords in the world")
    render=password
    print("Password: ",password)
            
#Instalizing Brain Processor
def neuron():
    
    output("This funtion is temperorally unaivailable sir..")
    
   #(animation = pyglet.image.load_animation(r'process/AI Processing.gif')
    #animSprite = pyglet.sprite.Sprite(animation)
    
  #  w = animSprite.width
  #  h = animSprite.height
    
  #  window = pyglet.window.Window(width=w,height=h)
    
  #  r,g,b,alpha = 0.5,0.5,0.8,0.5
    
    
  #  pyglet.gl.glClearColor(r,g,b,alpha)
    
  #  @window.event
  #  def on_draw():
  #      window.clear()
  #      animSprite.draw()
        
  #  pyglet.app.run())

#Instalizing mailing stream
def email():
    output("Connecting Email Service at port 5 8 7 ")
    try:
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        output("I Require Password for security reasons...!!")
        panni=input("Enter the password: ")
        frome='gsnish25255@gmail.com'
        s.login(frome,panni)
        to=input("Enter the gamil id of the reciever")
        if to == 'me':
            to='sollamudiyathu0000@gmail.com'
        else:
            pass   
    except Exception:
        output("Make sure that this device is connected to stable network")
        isconnected()
        output("if this error continues , sir , I recommend you to enable insecure app access in your mailing platform")
        output("and i always encrypt the mail before sending for security and im secure...")
    
    output("What is the message..")
    message = recognize(1)
    message = message + '      This is from JARVIS , A [GD™ Projet]'

    s.sendmail(frome,to, message)
    
    output("Mail sent Sucessfully..")

    s.quit()

#Terminating the skin with a funtion
def terskin():
    os.chdir('Customisation')
    os.system('cmd/c"taskkill /im Rainmeter.exe /t /f"')

#Conditional Activities
def intelligence():
    global render
    global auto
    global voico
    
    #Intro
    output("Calibrating and Analyzing the Code Process..")
    output("Booting Up my system...")
    playsound('process/sounds/boot.wav')
    isconnected()
    auto=False
    output("Hello . I am Jarvis , An AI system.")
    output("Now I am Online!!")

    #getting info to continue with voice or text
    while True:

        output("Should I take your voice command or text input?")
        inputo=str(input("Voice or Text :")).lower()
        if inputo == 'voice':
            voico='T'
            output("Alright Sir..")
            break
        elif inputo == 'text':
            voico='F'
            output("Alright")
            break
        else:
            output("Sir, just say me [text] or [voice] ")
            pass

    #Categorizing the querries
    ##Void Loop
    i,w = 1,0
    while i == 1:

        call=recognize(0)
        if call in calls:
            playsound('process/sounds/attention.wav')
            output(l1[random.randint(0,(len(l1)-1))])
            
            q=recognize(1)
                
            if q in l2:
                output("I am an artificial intelligence")
                #print("😎")

            elif q == 'enable home automation':
                if auto == False:
                    output("Alright sir! , Establishing serial Connection!")
                    com=str(input("Enter COM3: "))
                    noo=int('9600')
                    try:
                        ser = serial.Serial(com,noo,timeout=1)
                        auto=True
                        output("Home automation enabled..!")
                    except:
                        output("Error establishing the serial connetcion..")
                else:
                    output("Home Automation Enabled..!")

            elif q == 'diable home automation':
                auto = False
                output("Home automation disabled..")

            elif q in l19:
                if auto==True:
                    ser.write(b'H')
                    output("Done Sir!!")
                else:
                    output("Home automation is disabled !!")

            elif q in l20:
                if auto==True:
                    ser.write(b'L')
                    output("Done Sir!!")
                else:
                    output("Home automation is disabled !!")

            elif q in l21:
                if auto == True:
                    ser.write(b'1')
                    output("Done Sir !!")
                else:
                    output("Home Automation is not enabled sir!")
           
            elif q in l22:
                if auto == True:
                    ser.write(b'0')
                    output("Done Sir !!")
                else:
                    output("Home automation not enabled sir!")

            elif q in l23:
                if auto == True:
                    ser.write(b'A')
                    output("Done Sir!")
                else:
                    output("Home automation is disabled sir!")

            elif q in l24:
                if auto == True:
                    ser.write(b'Z')
                    output("Done Sir!")
                else:
                    output("Home automation is disabled sir!")
                
            elif q in l16 :
                output('''As of now! i can ineract with your questions , access your camera , check your network status ,
                    give you the date and time , open websites , make google searches , Generate strong passwords , 
                    Send whatsapp messages , show you my brain processor as an animation and read news from the news station''')
            
            elif q in l3:
                #print("👋")
                output("Alright , Terminateing!")
                output("Close the interface window to quit!")
                output("See you soon!")
                #playsound('process/sounds/gun.wav')
                terskin()
                quit()
                
            elif q in l6:
                output(l6[random.randint(0,len(l6)-1)])
                
            elif q in l4:
                output("Hmm!")
                            
            elif q in l7:
                isconnected()
                w=0
                    
            elif q in l8:
                render=Dt
                print(Dt)
                speak.speak("Today's date is printed")
                w=0
                    
            elif q in l9:
                render=Dt
                print(Tm)
                speak.speak("Time now is printed")
                w=0
                
            elif q in l10:
                google()
                w=0
                
            elif q in l11:
                output("Enter an url to open")
                url=str(input("ENTER: "))
                webbrowser.open(url)
                #print("👍")
                output("Entered website is opened!")
                w=0
                
            elif q in l12:
                output("Accessing Camera Stream..")
                #print("😉👌")
                stereo("Press q to stop")
                w=0
                
            elif q in l13:
                output("Loading my brain into an animation")
                neuron()
                w=0
                
            elif q in l5:
                output(pyjokes.get_joke())
                #print("😆")
                output('Ha Ha Ha!')
                
                i=1
                
                while i==1:
                    output("Want an another joke?")
                    r=recognize(1)
                    
                    if r=='yes':
                        output("Alright")
                        output(pyjokes.get_joke())
                        output('He He He!')
                        #print("😂")
                    
                    elif r=='no':
                        output('Okay, Hope you got your mood back!!')
                        output("Whatelse!?")
                        break
                    
                    else:
                        output("I want you to tell Yes or No!!")
                    pass
            
            elif q in l15:
                #print("👍")
                output('Alright')
                speak.speak("Enter the number of the reciever..")
                num=input("Enter the number of the reciever: ")
                speak.speak("Enter your message..")
                msg=input("Enter your message: ")
                output("Accessing Whatsapp..")
                try:
                    kit.sendwhatmsg(num,msg,hr,mn+2)
                    pass
                except Exception:
                    output("An unknown error occured!!")
                    output("Whatelse..?")
                    pass
                
            elif q in l17:
                output(q)
                i=1
                while i==1:
                    eco=recognize(1)
                    if eco=='stop it':
                        output("Okay Okay , he he he")
                        break
                    elif eco==None:
                        pass
                    else:
                        output(eco)
                        
            elif q in l14:
                output("Alright..")
                pswrg_genrtr()

            elif q in l18:
                email()

            elif q in detect:
                os.chdir('Process\Object_Reco')
                os.system('cmd/c"video_detection.py"')

            elif q in stdetect:

                os.chdir('Process\\Object_Reco\\')
                os.system('cmd/c"taskkill /im video_detection.py /t /f"')
            
            elif q==None:
                pass
            
            else:
                find_and_say(q)

        elif call in l3:
               output("Terminating !!")
               output("See you soon...")
               #playsound('process/sounds/gun.wav')
               terskin()
               quit()
        
        else:
            pass





    