from gtts import gTTS as textToSpeech
from playsound import playsound
import os


def convert(word):
    language = 'en'
    speech = textToSpeech(text=word, lang=language, slow=False)
    # Saving, playing and deleting the audio file.
    speech.save("play.mp3")
    playsound('play.mp3')
    os.remove("play.mp3")
