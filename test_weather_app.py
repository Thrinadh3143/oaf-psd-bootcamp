import unittest
import requests
from unittest.mock import patch, Mock
from weather_app import create_weather_service, HourlyTemperature

class TestWeatherService(unittest.TestCase):
    @patch('weather_app.requests.get')
    def test_fetch_hourly_temperature_success(self, mock_get):
        # Mock response data
        mock_response_data = {
            'hourly': {
                'temperature_2m': [20, 21, 19, 18],
                'time': ["2024-08-01T00:00:00Z", "2024-08-01T01:00:00Z", "2024-08-01T02:00:00Z", "2024-08-01T03:00:00Z"]
            }
        }

        # Configure the mock to return a response with the JSON data
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Create an instance of the API weather service
        api_url = "https://api.open-meteo.com/v1/forecast"
        weather_service = create_weather_service(api_url, service_type="api")

        # Fetch the hourly temperature data
        hourly_temperature = weather_service.fetch_hourly_temperature(latitude=52.52, longitude=13.41)

        # Assertions
        self.assertEqual(hourly_temperature.temperatures, [20, 21, 19, 18])
        self.assertEqual(hourly_temperature.timestamps, ["2024-08-01T00:00:00Z", "2024-08-01T01:00:00Z", "2024-08-01T02:00:00Z", "2024-08-01T03:00:00Z"])

    @patch('weather_app.requests.get')
    def test_fetch_hourly_temperature_failure(self, mock_get):
        # Configure the mock to return a failed response
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.RequestException("Failed request")
        mock_get.return_value = mock_response

        # Create an instance of the API weather service
        api_url = "https://api.open-meteo.com/v1/forecast"
        weather_service = create_weather_service(api_url, service_type="api")

        # Fetch the hourly temperature data
        hourly_temperature = weather_service.fetch_hourly_temperature(latitude=52.52, longitude=13.41)

        # Assertions
        self.assertEqual(hourly_temperature.temperatures, [])
        self.assertEqual(hourly_temperature.timestamps, [])

    def test_mocked_weather_service(self):
        # Create an instance of the mocked weather service
        weather_service = create_weather_service(api_url="", service_type="mocked")

        # Fetch the hourly temperature data
        hourly_temperature = weather_service.fetch_hourly_temperature(latitude=52.52, longitude=13.41)

        # Assertions
        self.assertEqual(hourly_temperature.temperatures, [20, 21, 19, 18])
        self.assertEqual(hourly_temperature.timestamps, ["2024-08-01T00:00:00Z", "2024-08-01T01:00:00Z", "2024-08-01T02:00:00Z", "2024-08-01T03:00:00Z"])

if __name__ == '__main__':
    unittest.main()
