import json

import speech_recognition
import pyttsx3

engine = pyttsx3.init()


def tts(text: str):
    engine.say(text)
    engine.runAndWait()


def stt() -> str:
    microfone = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        audio = microfone.listen(source)

    text = json.loads(microfone.recognize_vosk(audio)).get('text')

    if text:
        return text
    else:
        return stt()


while True:
    tts(stt())
