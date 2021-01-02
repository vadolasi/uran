import pyaudio
import pyttsx3
import json
from vosk import Model, KaldiRecognizer

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000
)
stream.start_stream()

while True:
    data = stream.read(8000)

    if rec.AcceptWaveform(data):
        text = json.loads(rec.Result())['text']

        if text:
            speak(text)
