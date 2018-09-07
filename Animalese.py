#Proof of concept for an Animalese TTS feature

import time
import wave
import pygame

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sound_files = ['006', '003', '020', '004', '073', '013', '026', '044', '005', '025', '027', '033', '031', '030', '042', '049', '046', '045', '007', '047', '012', '014', '032', '055', '057', '058', '059', '060', '061', '062', '063' ,'064' ,'065', '066', '067', '068']
sounds = []

frame_test = wave.open('./Voice/069.wav', 'rb').getframerate()

pygame.mixer.init(frequency = frame_test, buffer=512)

for x in sound_files:
    fileName = './Voice/' + x +'.wav' 
    sounds.append(pygame.mixer.Sound(fileName))

def playAnimal(s):
    global current_channel
    for c in s:
        if c.lower() in alphabet:
            voice_sound = sounds[alphabet.index(c.lower())]
            ch = pygame.mixer.find_channel(True)
            ch.play(voice_sound)
        print(c, end="", flush=True)
        time.sleep(.05)
    print("")

playAnimal('Hello there listener.   Welcome to animal crossing radio!  ')
playAnimal("It's currently 7:32 pm. It's a cool cloudy night outside. Here's some nice relaxing music for your evening.")

