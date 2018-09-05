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
        if c == ' ':
            continue
        voice_sound = sounds[alphabet.index(c)]
        ch = pygame.mixer.find_channel(True)
        print(ch)
        ch.play(voice_sound)
        time.sleep(.1)

playAnimal('hello there listener   welcome to animal crossing radio')


