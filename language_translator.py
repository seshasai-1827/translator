import speech_recognition
import pyttsx3
from translate import Translator
def Translate(lang,text):
    translator = Translator(to_lang = lang)
    translation = translator.translate(text)
    return translation
def record():
    recognizer = speech_recognition.Recognizer()
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic,duration = 0.1)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            return text
    except speech_recognition.UnknownValueError:
            return "Could not understand ..."


