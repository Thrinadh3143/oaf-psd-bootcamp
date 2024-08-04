import requests

# Data Source Class
class HourlyTemperature:
    def __init__(self, temperatures: list):
        self.temperatures = temperatures

# Service Class
class WeatherService:
    def __init__(self, api_url: str):
        self.api_url = api_url

    def get_hourly_temperature(self, latitude: float, longitude: float) -> HourlyTemperature:
        params = {
            'latitude': latitude,
            'longitude': longitude,
            'hourly': 'temperature_2m'
        }
        response = requests.get(self.api_url, params=params)
        response.raise_for_status()
        data = response.json()
        temperatures = data.get('hourly', {}).get('temperature_2m', [])
        return HourlyTemperature(temperatures=temperatures)

# Handler Class
class WeatherHandler:
    def __init__(self, weather_service: WeatherService):
        self.weather_service = weather_service

    def get_hourly_temperatures(self, latitude: float, longitude: float):
        hourly_temperature = self.weather_service.get_hourly_temperature(latitude, longitude)
        return {
            'temperatures': hourly_temperature.temperatures
        }

# Factory Function
def create_weather_service(api_url: str) -> WeatherService:
    return WeatherService(api_url)

# Main Functionality
def main():
    API_URL = 'https://api.open-meteo.com/v1/forecast'
    weather_service = create_weather_service(API_URL)
    weather_handler = WeatherHandler(weather_service)

    # Example usage
    print(weather_handler.get_hourly_temperatures(53.52, 13.41))

if __name__ == '__main__':
    main()
