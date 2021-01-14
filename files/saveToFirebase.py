#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import datetime
from collections import OrderedDict

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://testimonials-ba470-default-rtdb.firebaseio.com'
})

def pushRecording(recordURL,recordText):
    root = db.reference()
    date = datetime.datetime.now()
    date = date.strftime("%x")
    # Add a new user under /users.
    new_user = root.child('testimonials').push({
        'recordURL' : recordURL, 
        'recordText' : recordText,
        'date' : date,
        'type' : "call"
    })

def pushMessage(spanishText,englishText):
    root = db.reference()
    date = datetime.datetime.now()
    date = date.strftime("%x")
    # Add a new user under /users.
    new_user = root.child('testimonials').push({
        'spanishText' : spanishText,
        'englishText' : englishText,
        'date' : date,
        'type' : "sms"
    })

def pushPositiveFeedback(feedbackType):
    root = db.reference()
    new_user = root.child('feedback')      
    new_user.push({
        'type': feedbackType
    })

def pushNegativeFeedback():
    root = db.reference()
    new_user = root.child('feedback')       
    new_user.push({
        'type': "not useful"
    })

# pushRecording('test1','test2')

def getLatest(number):

    root = db.reference()
    result = root.child("testimonials").order_by_child('type').equal_to("sms").get()

    smsResponse = "Latest Stories: \n"

    for i in range(number):
        item = list(result.items())[i]
        
        smsResponse += "Story Number " + str(i + 1) + '\n'
        smsResponse += 'Spanish: ' + item[1]['spanishText'] + '\n'
        smsResponse += 'English: ' + item[1]['englishText'] + '\n \n'

    return smsResponse

# print(getLatest(1))


