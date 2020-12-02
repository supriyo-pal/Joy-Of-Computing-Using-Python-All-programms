# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:48:35 2020

@author: Supriyo
"""

import speech_recognition as sr
Audio_file=("Uska Hi Banana.wav")
#use audio file as the source 
r=sr.Recognizer()#initialize the recognizer
with sr.AudioFile(Audio_file)as source:
    audio=r.record(source)
    #read the sudio file
try:
    print("Audio file contains"+r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google speechh recogition coud nor uderstand audio")
except sr.RequestError:
    print("could not get the results from google speech recognition")
    