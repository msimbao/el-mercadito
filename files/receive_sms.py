#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

import accessAPI
import translateText
import saveToFirebase

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message

    initialText = accessAPI.downloadMessage()
    lowerCaseText = initialText.lower()
    smsText = lowerCaseText.split()

    if smsText[1] == "stories":
        smsRespone = saveToFirebase.getLatest(int(smsText[0]))
        resp.message(smsRespone)
    elif smsText[0] == "useful":
        saveToFirebase.pushPositiveFeedback(smsText[2])
        resp.message("Thank your feedback! We hope you are well and if you need assistance with anything, feel free to call us on 1 800 875 7060. Have a good day.")
    elif lowerCaseText == "not useful":
        saveToFirebase.pushNegativeFeedback()
        resp.message("Thank your feedback! We hope you are well and if you need assistance with anything, feel free to call us on 1 800 875 7060. Have a good day.")
    else:
        saveToFirebase.pushMessage(lowerCaseText,lowerCaseText)
        resp.message("Thank you for being a part of our community and sharing your story, your light and motivating and inspiring others. We hope you are well and if you need assistance with anything, feel free to call us on 1 800 875 7060. Have a good day.")
        # encoding = translateText.detectLanguage(smsText)
        # if encoding == "en":
        #     englishText = smsText
        #     spanishText = translateText.translateToSpanish(smsText)
        #     saveToFirebase.pushMessage(spanishText,englishText)
        # else:
        #     englishText = translateText.translateToEnglish(smsText)
        #     spanishText = smsText
        #     saveToFirebase.pushMessage(spanishText,englishText)
        resp.message("Thank you for being a part of our community and sharing your story, your light and motivating and inspiring others. We hope you are well and if you need assistance with anything, feel free to call us on 1 800 875 7060. Have a good day.")
    

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)