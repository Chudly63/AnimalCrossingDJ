#Proof of concept for an Animalese TTS feature

import time
import wave
import pygame

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sounds = []

frame_test = wave.open('./Voice/069.wav', 'rb').getframerate()

pygame.mixer.init(frequency = frame_test, buffer=512)

for x in range(69, 94):
    fileName = './Voice/0' + str(x) +'.wav' 
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

playAnimal('Hello there listener.   Welcome to animal crossing radio!')
playAnimal("It's a lovely day for some music. Don't you agree?")

