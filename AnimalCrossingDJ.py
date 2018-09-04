#Quick script that plays the Animal Crossing New Leaf song based on the current time and weather

from weather import Weather
from datetime import datetime
import pyaudio
import wave

RAIN_CODES = [1, 2, 3, 4, 9, 10, 11, 12, 37, 38, 39, 40, 45, 47]                        #Weather Condition codes that indicate some type of rainy weather
SNOW_CODES = [5, 6, 7, 13, 14, 15, 16, 17, 18, 41, 42, 43, 46]                          #Weather Condition codes that indicate some type of snowy weather
SONGS = ['12AM','1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM',                        #The base of all song names based on the hour
                '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM',              #For rainy versions, append a 'r' to the end of the file name
                '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM']               #For snowy versions, append a 's' to the end of the file name

playMe = SONGS[datetime.now().hour]                                                     #Get the base song for the current hour

weather = Weather()                                                                     #Load the weather class
lookup = weather.lookup_by_location('philadelphia')                                     #Get the philadelphia weather
condition = int(lookup.condition.code)                                                  #Grab the current condition code
print(str(condition) + " : " + lookup.condition.text)

if condition in RAIN_CODES:                                                             #Check for rainy weather
    playMe += "r"
elif condition in SNOW_CODES:                                                           #Check for snowy weather
    playMe += "s"

playMe += ".wav"                                                                        #Append file type
print(playMe)
#This is code to play the selected .wav file. I am a newbie with pyaudio and wave so I don't entirely know how this all works yet.
chunk = 1024

f = wave.open(r'./Songs/'+playMe,'rb')

p = pyaudio.PyAudio()

stream = p.open(format = p.get_format_from_width(f.getsampwidth()), channels = f.getnchannels(), rate = f.getframerate(), output = True)


data = f.readframes(chunk)

while data:
    stream.write(data)
    data = f.readframes(chunk)
    
stream.stop_stream()
stream.close()

p.terminate()