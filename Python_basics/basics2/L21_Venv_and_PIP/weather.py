import requests
import os
from dotenv import load_dotenv
from pprint import pprint
load_dotenv()

def get_currentWeather():
    print("** Getting Current Weather **")
    city = input("Please enter you City name : ")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'
    #print(request_url)

    weather_data = requests.get(request_url).json()
    #pprint(weather_data)
    print(f"Current weather for '{weather_data["name"]}' :\n")
    print(f"The temp now is {weather_data["main"]["temp"]}°")
    print(f"Feels like  {weather_data["main"]["feels_like"]}°")
    print(f"The weather condition : {weather_data['weather'][0]['description']}")

get_currentWeather()