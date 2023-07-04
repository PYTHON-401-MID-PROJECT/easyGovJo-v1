
import speech_recognition as sr
from bidi.algorithm import get_display
from arabic_reshaper import reshape
from pydub import AudioSegment
from gtts import gTTS
import os

# this function to convert any audio file to .wav
def convert_ogg_to_wav(audio_filename, wav_file):
    sound = AudioSegment.from_file(audio_filename)
    sound.export(wav_file, format="wav")

# this function to convert the audio file to text
def convert_speech_to_text(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = r.record(source)  # read the entire audio file
    try:
        # Use the Google Speech Recognition API for Arabic
        text = r.recognize_google(audio, language='ar-AR')
        reshaped_text = reshape(text) 
        display_text = get_display(reshaped_text)
        print("Recognized text:")
        print(display_text)

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")

    except sr.RequestError:
        print("Sorry, I'm currently experiencing technical issues.")

other_filename="outputs.mp3"
wav_filename="new.wav"
convert_ogg_to_wav(other_filename, wav_filename)
convert_speech_to_text(wav_filename)


# *****
# Convert text to speech
def convert_text_to_speech(text, output_file): 
    tts = gTTS(text, lang='ar')
    tts.save(output_file)

def audio_output(): # to render the output text
    output_file = "neeeeeeeeeew.wav"
    text="مرحبا يا عاصم عاصم عاصم "
    convert_text_to_speech(text, output_file)

audio_output()