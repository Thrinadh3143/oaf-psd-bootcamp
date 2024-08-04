import unittest
from unittest.mock import patch, MagicMock
from weather_app import WeatherService, WeatherHandler, HourlyTemperature

class WeatherServiceTest(unittest.TestCase):
    @patch('requests.get')
    def test_get_hourly_temperature(self, mock_get):
        mock_get.return_value.json.return_value = {
            'hourly': {
                'temperature_2m': [15.0, 16.0, 17.0]
            }
        }
        service = WeatherService('https://api.open-meteo.com/v1/forecast')
        hourly_temp = service.get_hourly_temperature(52.52, 13.41)
        self.assertEqual(hourly_temp.temperatures, [15.0, 16.0, 17.0])

class WeatherHandlerTest(unittest.TestCase):
    def test_get_hourly_temperatures(self):
        mock_service = MagicMock()
        mock_service.get_hourly_temperature.return_value = HourlyTemperature(
            temperatures=[15.0, 16.0, 17.0]
        )
        handler = WeatherHandler(mock_service)
        result = handler.get_hourly_temperatures(52.52, 13.41)
        self.assertEqual(result['temperatures'], [15.0, 16.0, 17.0])

# Run the tests
if __name__ == '__main__':
    unittest.main()
