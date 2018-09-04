from weather import Weather, Unit
from datetime import datetime
import pyaudio
import wave

weather = Weather(unit=Unit.CELSIUS)

lookup = weather.lookup_by_location('philadelphia')
condition = lookup.condition
print(condition.text)

SONGS_NORMAL = ['12AM','1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM']

chunk = 1024

f = wave.open(r'./Songs/'+SONGS_NORMAL[20]+'.wav','rb')

p = pyaudio.PyAudio()

stream = p.open(format = p.get_format_from_width(f.getsampwidth()), channels = f.getnchannels(), rate = f.getframerate(), output = True)


data = f.readframes(chunk)

while data:
    stream.write(data)
    data = f.readframes(chunk)
    
stream.stop_stream()
stream.close()

p.terminate()