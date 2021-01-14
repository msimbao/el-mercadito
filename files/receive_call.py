#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

import accessAPI
# import transcribeCall
import saveToFirebase

#Initialization 
app = Flask(__name__)

#Constants
# audioFile = transcribeCall.AUDIO_FILE 


@app.route("/voice", methods=['GET', 'POST'])
def record():
    """Returns TwiML which prompts the caller to record a message"""
    # Start our TwiML response
    response = VoiceResponse()

    # Use <Say> to give the caller some instructions
    response.say("Hola. Bienvenido al servicio de intercambio de informacion de Pedacito de La Tierra. Por favor, no nos de su nombre ni ninguna informacion confidencial en su historia y al utilizar este servicio, acepta que lo que comparte se haga publico. Despues del pitido, espere unos segundos y luego podra comenzar a grabar. Puede colgar una vez que haya terminado. Gracias por tu tiempo.", language='es-MX')
    response.pause(length=3)
    response.say("Hello. Welcome to Pedacito de La Tierra information sharing service. Please do not give us your name or any confidential information in your story and by using this service you agree to have what you share made public. After the beep, wait for a few seconds then you can start recording. You can Hang up once you are done. Thank you for your time")

    # Use <Record> to record the caller's message
    response.record(action="https://handler.twilio.com/twiml/EH5d4dd437b6a62a4a4413954e680a282a",
                    timeout=7,
                    transcribe=True
                    )

    response.say("Thank you for being a part of our community and sharing your story, your light and motivating and inspiring others. We hope you are well and if you need assistance with anything, feel free to call us on 1 800 875 7060. Have a good day.")

    # End the call with <Hangup>
    response.hangup()

    print("Updating Latest Recording")

    recordURL = accessAPI.downloadRecording()
    # recordText = transcribeCall.transcribeRecording(audioFile)
    recordText = "No Transciption Available Yet"
    saveToFirebase.pushRecording(recordURL,recordText)

    print("Recording Updated")
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)