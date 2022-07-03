import eel
import pyowm
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
# API from openwheathermap.org
owm = pyowm.OWM(API_KEY)


@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    return f'В городе {place} сейчас {temp} градусов.'


eel.init('web')
eel.start('main.html', size=(700, 400))
