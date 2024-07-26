from abc import ABC, abstractmethod

class WeatherService(ABC):
    """
    Abstract base class for weather services. Defines the interface for fetching and parsing weather data.
    """

    @abstractmethod
    def fetching_data(self, city: str) -> dict:
        """
        Fetch weather data for the given city.

        :param city: Name of the city to fetch weather data for.
        :return: Dictionary containing the fetched weather data.
        """
        pass

    @abstractmethod
    def temperature(self, data: dict) -> float:
        """
        Parse and return the temperature from the fetched data.

        :param data: Dictionary containing the fetched weather data.
        :return: Temperature as a float.
        """
        pass

    @abstractmethod
    def humidity(self, data: dict) -> float:
        """
        Parse and return the humidity from the fetched data.

        :param data: Dictionary containing the fetched weather data.
        :return: Humidity as a float.
        """
        pass

class WebWeatherService(WeatherService):
    """
    Concrete implementation of WeatherService that fetches data from a web URL.
    """

    def fetching_data(self, city: str) -> dict:
        """
        Fetch weather data from a web URL for the given city.

        :param city: Name of the city to fetch weather data for.
        :return: Dictionary containing the fetched weather data.
        """
        pass

    def temperature(self, data: dict) -> float:
        """
        Parse and return the temperature from the fetched data.

        :param data: Dictionary containing the fetched weather data.
        :return: Temperature as a float.
        """
        pass

    def humidity(self, data: dict) -> float:
        """
        Parse and return the humidity from the fetched data.

        :param data: Dictionary containing the fetched weather data.
        :return: Humidity as a float.
        """
        pass

class WeatherApp:
    """
    Weather application that uses a WeatherService to provide weather information for a specified city.
    """

    def __init__(self, service: WeatherService):
        """
        Initialize the WeatherApp with a WeatherService.

        :param service: Instance of a WeatherService to fetch and parse weather data.
        """
        self.service = service

    def get_weather_info(self, city: str) -> dict:
        """
        Get weather information for a given city.

        :param city: Name of the city to get weather information for.
        :return: Dictionary containing the city, temperature, and humidity.
        """
        data = self.service.fetching_data(city)
        temperature = self.service.temperature(data)
        humidity = self.service.humidity(data)
        return {
            "city": city,
            "temperature": temperature,
            "humidity": humidity
        }

# Example usage:
# service = WebWeatherService()
# app = WeatherApp(service)
# weather_info = app.get_weather_info("New York")
# print(weather_info)
