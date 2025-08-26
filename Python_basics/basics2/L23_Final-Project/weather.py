from dotenv import load_dotenv
from pprint import  pprint
import requests
import os

load_dotenv() # load api key from another file

def get_weather(city = "Buraidah"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'
    weather_data = requests.get(request_url).json() # requests.get get information for the link on the web as json to python format
    return weather_data
if __name__ == "__main__":
    print("** Getting Current Weather **")

    city = input("Please enter you City name : ")

    # Check for empty strings or string with only spaces

    if not bool(city.strip()):
        city = "Buraidah"
    weather_data = get_weather(city)
    print()
    pprint(weather_data)

