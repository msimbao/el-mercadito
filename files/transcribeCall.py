import speech_recognition as sr
from os import path

AUDIO_FILE = "record.wav"

def transcribeRecording(audioFile):
        #Function That takes no variables and is used to transcribe a recording                                                       

        # use the audio file as the audio source                                        
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
                r.adjust_for_ambient_noise(source)
                audio = r.record(source)  # read the entire audio file   
                recordText = r.recognize_google(audio)               
                # print("Transcription: " + r.recognize_google(audio))
        
        return recordText

recordText = transcribeRecording(AUDIO_FILE)
print(recordText)