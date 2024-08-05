import requests
from abc import ABC, abstractmethod

# Data Source Class
class HourlyTemperature:
    def __init__(self, temperatures: list, timestamps: list):
        self.temperatures = temperatures
        self.timestamps = timestamps

# Abstract Service Class
class AbstractWeatherService(ABC):
    @abstractmethod
    def fetch_hourly_temperature(self, latitude: float, longitude: float) -> HourlyTemperature:
        pass

# API Weather Service Class
class ApiWeatherService(AbstractWeatherService):
    def __init__(self, api_url: str):
        self.api_url = api_url

    def fetch_hourly_temperature(self, latitude: float, longitude: float) -> HourlyTemperature:
        params = {'latitude': latitude, 'longitude': longitude, 'hourly': 'temperature_2m'}
        try:
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()
            data = response.json()
            temperatures = data.get('hourly', {}).get('temperature_2m', [])
            timestamps = data.get('hourly', {}).get('time', [])
            return HourlyTemperature(temperatures=temperatures, timestamps=timestamps)
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return HourlyTemperature(temperatures=[], timestamps=[])
        except ValueError as e:
            print(f"Invalid JSON response: {e}")
            return HourlyTemperature(temperatures=[], timestamps=[])
        except KeyError as e:
            print(f"Unexpected data format: {e}")
            return HourlyTemperature(temperatures=[], timestamps=[])

# Mocked Weather Service Class for testing
class MockedWeatherService(AbstractWeatherService):
    def fetch_hourly_temperature(self, latitude: float, longitude: float) -> HourlyTemperature:
        # Return some mocked data
        return HourlyTemperature(
            temperatures=[20, 21, 19, 18],
            timestamps=["2024-08-01T00:00:00Z", "2024-08-01T01:00:00Z", "2024-08-01T02:00:00Z", "2024-08-01T03:00:00Z"]
        )

# Factory Function
def create_weather_service(api_url: str, service_type: str = "api") -> AbstractWeatherService:
    if service_type == "api":
        return ApiWeatherService(api_url)
    elif service_type == "mocked":
        return MockedWeatherService()
    else:
        raise ValueError(f"Unknown service type: {service_type}")

# Example usage
if __name__ == "__main__":
    api_url = "https://api.open-meteo.com/v1/forecast"
    weather_service = create_weather_service(api_url, service_type="api")
    hourly_temperature = weather_service.fetch_hourly_temperature(latitude=52.52, longitude=13.41)
    print(hourly_temperature.temperatures)
    print(hourly_temperature.timestamps)
