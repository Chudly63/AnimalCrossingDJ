#Quick script that plays the Animal Crossing New Leaf song based on the current time and weather

from weather import Weather
from datetime import datetime
import time
import wave
import pygame

weather = Weather()                                                                     #Load the weather class
RAIN_CODES = [1, 2, 3, 4, 9, 10, 11, 12, 37, 38, 39, 40, 45, 47]                        #Weather Condition codes that indicate some type of rainy weather
SNOW_CODES = [5, 6, 7, 13, 14, 15, 16, 17, 18, 41, 42, 43, 46]                          #Weather Condition codes that indicate some type of snowy weather
SONGS = ['12AM','1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM',                        #The base of all song names based on the hour
                '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM',              #For rainy versions, append a 'r' to the end of the file name
                '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM']               #For snowy versions, append a 's' to the end of the file name

while(True):
    playMe = './Songs/' + SONGS[datetime.now().hour]                                        #Get the base song for the current hour

    lookup = weather.lookup_by_location('philadelphia')                                     #Get the philadelphia weather
    condition = int(lookup.condition.code)                                                  #Grab the current condition code
    print(str(condition) + " : " + lookup.condition.text)

    if condition in RAIN_CODES:                                                             #Check for rainy weather
        playMe += "r"
    elif condition in SNOW_CODES:                                                           #Check for snowy weather
        playMe += "s"

    playMe += ".wav"                                                                        #Append file type
    print("Now playing: " + playMe)


    track_file = wave.open(playMe,'rb')                                                     #Get the file data

    pygame.mixer.init(frequency=track_file.getframerate())                                  #Open a pygame sound mixer and set the frequency to the song's framerate
    track = pygame.mixer.Sound(playMe)                                                      #Load the song into the sound mixer

    track.play(loops=-1, fade_ms=4000)                                                      #Play the song
    while pygame.mixer.get_busy():                                                          #Keep the program running while the song is still playing
        if (datetime.now().minute == 59 and datetime.now().second >=30):
            track.fadeout(30000)
        time.sleep(1)
