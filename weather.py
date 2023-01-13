import requests
import json
from datetime import datetime 

from flask import Flask
from flask import render_template

app = Flask(__name__)

# From OpenWeatherMap https://home.openweathermap.org/api_keys
# Add your own API key
api_key = ""

#lat and lon of Bristol, UK
lat = "51.454514"
lon = "-2.587910"

# API URL (f strings wouldn't work?)
weather_url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=imperial".format(lat, lon, api_key)

response = requests.get(weather_url)
weather_info = response.json()

@app.route("/")
def bristol_weather():
    if weather_info["cod"] == 200:
        celcius = (weather_info["main"]["temp"] - 32) * 5/9
        weather = "The weather, right now in Bristol, is {} F and {} C".format(weather_info["main"]["temp"], celcius)
        return "<p>{}</p>".format(weather)
        # return render_template('weather.html', weather=weather)