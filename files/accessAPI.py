#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import requests
import json
import urllib2

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def downloadRecording():
    #Function that takes no variables and is used to gather the latest recordings from a Twilio User Account

    # Your Account SID from twilio.com/console
    account_sid = "ACfe7c37846656feea2c3d334226894859"
    # Your Auth Token from twilio.com/console
    auth_token  = "4ef967a5bc820cc04dd70745ef5feed1"

    url = "https://api.twilio.com/2010-04-01/Accounts/"+account_sid+"/Recordings.json"

    response = requests.get(url, auth=(account_sid, auth_token))
    # jprint(response.json())

    jsonString=response.json()

    recordings = jsonString["recordings"]

    latestRecording = recordings[0]

    latestSID = latestRecording["sid"]

    # print(latestSID)

    latestWAV = "https://api.twilio.com/2010-04-01/Accounts/"+account_sid+"/Recordings/" + latestSID + ".wav"

    req2 = urllib2.Request(latestWAV)
    response = urllib2.urlopen(req2)

    #grab the data
    data = response.read()

    mp3Name = "record.wav"
    song = open(mp3Name, "w")
    song.write(data)    # was data2
    song.close()

    return latestWAV

def downloadMessage():
    #Function that takes no variables and is used to gather the latest recordings from a Twilio User Account

    # Your Account SID from twilio.com/console
    account_sid = "ACfe7c37846656feea2c3d334226894859"
    # Your Auth Token from twilio.com/console
    auth_token  = "4ef967a5bc820cc04dd70745ef5feed1"

    #https://api.twilio.com/2010-04-01/Accounts/ACfe7c37846656feea2c3d334226894859/Messages.json

    url = "https://api.twilio.com/2010-04-01/Accounts/"+account_sid+"/Messages.json"

    response = requests.get(url, auth=(account_sid, auth_token))
    # jprint(response.json())

    jsonString=response.json()

    messages = jsonString["messages"]

    trialMessage = messages[0]

    if trialMessage["direction"] == "outbound-reply":
        latestMessage = messages[1]
        latestMessage = latestMessage["body"]
    else:
        latestMessage = messages[0]
        latestMessage = latestMessage["body"]

    #direction inbound/outbound-reply

    # print(latestMessage)

    return latestMessage

# downloadMessage()
# downloadRecording()