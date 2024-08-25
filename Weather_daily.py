import pandas as pd
from abc import ABC, abstractmethod
import openmeteo_requests
import requests_cache
from retry_requests import retry
import sqlite3

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Data Source Class
class DailyTemperature:
    def __init__(self, min_temperatures: list, max_temperatures: list, dates: list):
        self.min_temperatures = min_temperatures
        self.max_temperatures = max_temperatures
        self.dates = dates

    def to_dataframe(self):
        return pd.DataFrame({
            "Date": self.dates,
            "Min Temperature": self.min_temperatures,
            "Max Temperature": self.max_temperatures
        })

# Abstract Service Class
class AbstractWeatherService(ABC):
    @abstractmethod
    def fetch_daily_temperature(self, latitude: float, longitude: float) -> DailyTemperature:
        pass

# API Weather Service Class
class ApiWeatherService(AbstractWeatherService):
    def __init__(self, api_url: str):
        self.api_url = api_url

    def fetch_daily_temperature(self, latitude: float, longitude: float) -> DailyTemperature:
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "daily": ["temperature_2m_max", "temperature_2m_min"],
            "past_days": 92  # Fetch past 92 days (approximately 3 months)
        }
        responses = openmeteo.weather_api(self.api_url, params=params)
        response = responses[0]

        daily = response.Daily()
        daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
        daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()

        daily_data = {
            "date": pd.date_range(
                start=pd.to_datetime(daily.Time(), unit="s", utc=True),
                end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
                freq=pd.Timedelta(seconds=daily.Interval()),
                inclusive="left"
            ),
            "temperature_2m_max": daily_temperature_2m_max,
            "temperature_2m_min": daily_temperature_2m_min
        }

        return DailyTemperature(
            min_temperatures=daily_temperature_2m_min,
            max_temperatures=daily_temperature_2m_max,
            dates=daily_data["date"]
        )

# Abstract Database Class
class AbstractWeatherDatabase(ABC):
    @abstractmethod
    def insert_data(self, df: pd.DataFrame):
        pass

    @abstractmethod
    def fetch_data(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def close(self):
        pass

# SQLite3 Database Implementation
class WeatherDatabase(AbstractWeatherDatabase):
    def __init__(self, db_name='weather_data_storage.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS DailyTemperature (
                Date TEXT PRIMARY KEY,
                MinTemperature REAL,
                MaxTemperature REAL
            )
        ''')
        self.conn.commit()

    def insert_data(self, df: pd.DataFrame):
        cursor = self.conn.cursor()
        df['Date'] = df['Date'].astype(str)
        for _, row in df.iterrows():
            cursor.execute('''
                INSERT OR REPLACE INTO DailyTemperature (Date, MinTemperature, MaxTemperature)
                VALUES (?, ?, ?)
            ''', (row['Date'], row['Min Temperature'], row['Max Temperature']))
        self.conn.commit()

    def fetch_data(self) -> pd.DataFrame:
        df = pd.read_sql_query("SELECT * FROM DailyTemperature", self.conn)
        return df

    def close(self):
        self.conn.close()

# Factory Class for Weather Services
class WeatherServiceFactory:
    @staticmethod
    def create_service(service_type: str, api_url: str = None) -> AbstractWeatherService:
        if service_type == 'api':
            return ApiWeatherService(api_url)
        elif service_type == 'mock':
            return MockWeatherService()  # Assuming a MockWeatherService is implemented
        else:
            raise ValueError(f"Unknown service type: {service_type}")

# Main execution
if __name__ == "__main__":
    api_url = "https://api.open-meteo.com/v1/forecast"
    
    # Use the factory to create the appropriate service
    weather_service = WeatherServiceFactory.create_service('api', api_url)
    
    daily_temperature = weather_service.fetch_daily_temperature(latitude=52.52, longitude=13.41)
    
    # Convert data to DataFrame
    df = daily_temperature.to_dataframe()
    
    # Store data in SQLite3
    db = WeatherDatabase()
    db.insert_data(df)
    
    # Fetch and display the stored data from the database
    stored_df = db.fetch_data()
    print(stored_df)
    
    # Close the database connection
    db.close()