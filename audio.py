import pyaudio
import wave
import speech_recognition as sr
import subprocess
from gtts import gTTS as gt
import os
import pygame
from commands import Commander

running = True


def say(text):
    my_tts = text
    tts = gt(text=my_tts, lang='en', slow=False)
    tts.save("./audio/file.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("./audio/file.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    # subprocess.call('echo ' + text, shell=True)


def play_notification():
    pygame.mixer.init()
    pygame.mixer.music.load("./audio/appointed.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()


r = sr.Recognizer()
cmd = Commander()


def initSpeech():
    play_notification()
    print("Listening....")
    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)

    play_notification()
    # play_audio("./audio/sms-alert-1-daniel_simon.wav")
    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't understand you.")

    print("Your command:")
    print(command)
    if command in ["quit", "exit", "bye", "goodbye"]:
        global running
        running = False
    else:
        cmd.discover(command)
    # say(command)


while running == True:
    initSpeech()
