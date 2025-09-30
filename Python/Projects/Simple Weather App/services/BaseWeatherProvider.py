from abc import ABC,abstractmethod

class WeatherProvider(ABC):
    """
    Blueprint for weather APIs
    """

    @abstractmethod
    def get_weather(self,city_name) -> dict:
        pass