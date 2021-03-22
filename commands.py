import subprocess
import os
from gtts import gTTS as gt
import pygame
import requests
from bs4 import BeautifulSoup
from get_answer import Fetcher


class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "don't", "wait", "cancel", "stop"]
        self.my_tts = "Hi"
        self.tts = gt(text=self.my_tts, lang='en', slow=False)

    def discover(self, text):
        if "what" in text and "your name" in text:
            if "my" in text:
                self.respond("You haven't told me your name yet")
            else:
                self.respond("I am virtual assistant . How are you?")
        elif "open" in text:
            app = text.split(" ", 1)[
                -1]  # creating array with two text first is to take off launch or open -1 will only consider the next text
            self.respond("Opening " + app)
            os.system("start " + app + ".exe")
        else:
            f = Fetcher("https://www.google.com/search?q=" + text)
            answer = f.lookup()
            self.respond(answer)

    def say(self, text):
        self.my_tts = text
        self.tts = gt(text=self.my_tts, lang='en', slow=False)
        self.tts.save("./audio/file.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("./audio/file.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

    def respond(self, response):
        print(response)
        self.say(response)
