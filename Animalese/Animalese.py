#Proof of concept for an Animalese TTS feature

import time
from pygame import mixer


class Animalese(object):

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    sounds = {}
    FRAME_RATE = 8000
    SPEECH_RATE = 0.05

    def __init__(self):

        mixer.init(frequency = self.FRAME_RATE, buffer=512)

        for x in self.alphabet:
            fileName = './Voice/' + x +'.wav' 
            self.sounds[x] = mixer.Sound(fileName)
            
    def setFrameRate(self, _rate):
        if isinstance(_rate, int):
            FRAME_RATE = _rate
            return FRAME_RATE
        else:
            return None
        
    def setSpeechRate(self, _rate):
        if isinstance(_rate, float):
            SPEECH_RATE = _rate
            return SPEECH_RATE
        else:
            return None

    def speakAnimal(self, s):
        global current_channel
        for c in s:
            if c.lower() in self.alphabet:
                voice_sound = self.sounds[c.lower()]
                ch = mixer.find_channel(True)
                ch.play(voice_sound)
            print(c, end="", flush=True)
            time.sleep(self.SPEECH_RATE)
        print("")


#Translator = Animalese()

#Translator.playAnimal('Hello there listener.   Welcome to animal crossing radio!  ')
#Translator.playAnimal("It's currently 7:32 pm. It's a cool cloudy night outside. Here's some nice relaxing music for your evening.")

