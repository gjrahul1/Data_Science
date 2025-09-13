from services.BaseWeatherProvider import WeatherProvider
from config.weatherapi_config import WEATHERAPI_BASE_URL
import os
import sys
from dotenv import load_dotenv
import requests

class WeatherAPIProvider(WeatherProvider):
    """
    Sending request to Weather API endpoint
    """

    def __init__(self):
        load_dotenv()
        self.URL = WEATHERAPI_BASE_URL
        self.WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    
    def get_weather(self, city_name):
        payload = {
            'q': city_name,
            'key': self.WEATHER_API_KEY
        }

        try:

            response = requests.get(f"{self.URL}/current.json", params = payload)

            response.raise_for_status()

            #print(f"{response.status_code}")
            if response.status_code == 200:
                return response.json()

        except requests.exceptions.HTTPError:
            raise 
        except requests.exceptions.ConnectionError:
            raise
        except requests.exceptions.Timeout:
            raise
        except requests.exceptions.JSONDecodeError:
            raise
        except Exception:
            raise
        



