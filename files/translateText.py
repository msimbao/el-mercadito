#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from langdetect import detect
from translate import Translator

def detectLanguage(text):
    return detect(text)

def translateToSpanish(text):
    translator= Translator(to_lang="Spanish")
    translation = translator.translate(text)
    return translation

def translateToEnglish(text):
    translator= Translator(from_lang="spanish",to_lang="english")
    translation = translator.translate(text)
    return translation

# print(translateToSpanish("Good Morning"))
# print(translateToEnglish("¡Buenos días!"))