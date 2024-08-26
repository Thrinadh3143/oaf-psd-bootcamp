Weather Data Analysis Project

Overview

This project fetches and stores daily temperature data from the Open-Meteo API, processes the data, and provides a set of visualization tools to analyze the weather data over the last three months. The project is structured to be modular and easily extendable, using the Factory and Abstract Factory design patterns.

Features

  •	Fetch daily minimum and maximum temperatures for a specific location.
  
  •	Store weather data in a SQLite3 database.
  
  •	Visualize weather data using various plots:
  
	•	Line Chart for daily minimum and maximum temperatures.
	•	Temperature Range Plot.
	•	Rolling Average Plot for temperature trends.
	•	Histogram of temperature distribution.
	•	Scatter Plot of minimum vs. maximum temperatures.
	•	Box Plot and Violin Plot for temperature distributions.
 What I Learned

	•	Python Programming: Enhanced my skills in Python programming, particularly in working with APIs, data processing, and visualization.
	•	Data Management: Learned how to efficiently store and retrieve data using SQLite3, and how to manage database connections.
	•	Data Visualization: Gained experience in creating various types of plots using Matplotlib and Seaborn to interpret weather data.
	•	Software Design: Improved understanding of software design principles, including abstraction and interface design with the use of abstract classes and factory patterns.
	•	Error Handling and Robustness: Implemented retry mechanisms and caching to handle API requests more robustly.
	•	Git & GitHub: Learned how to use Git for version control and GitHub for managing and collaborating on projects. I practiced committing changes, creating branches, and handling pull requests.


Setup Instructions

Prerequisites

	•	Python 3.7 or above.
	•	SQLite3 installed on your machine.
	•	Required Python packages: pandas, matplotlib, seaborn, sqlite3, openmeteo_requests, requests_cache, retry_requests.

Installation

1.	Clone the repository:
git clone https://github.com/Thrinadh3143/oaf-psd-bootcamp.git

Configuration

  •	The script uses the Open-Meteo API to fetch weather data. The API URL is preconfigured in the ApiWeatherService class.
  
  •	You can change the location for fetching the weather data by modifying the latitude and longitude values in the main execution block.

Usage
1.	Run the main script to fetch weather data for the last 92 days and store it in the SQLite3 database:

          python weather_daily.py


2.	This script will create a database named weather_data_storage.db and store the fetched weather data in it.
3.	Run the visualization script to generate various plots: “python visualize_weather_data.py”

          python visualize_weather_data.py

4.	This script will read the data from the SQLite3 database and generate the following visualizations:
   
         •	Line Chart: Shows daily minimum and maximum temperatures.
         •	Temperature Range Plot: Displays the range between daily minimum and maximum temperatures.
  	     •	Rolling Average Plot: Displays the 7-day rolling average of temperatures.
  	     •	Temperature Histogram: Shows the distribution of temperature data.
  	     •	Scatter Plot: Compares daily minimum vs. maximum temperatures.
  	     •	Box Plot: Visualizes the distribution of minimum and maximum temperatures.
  	     •	Violin Plot: Another way to visualize the distribution of temperatures.
  	
Extending the Project

•	Database Layer: The project uses an abstract class AbstractWeatherDatabase which you can implement for other types of databases if needed.

•	API Layer: You can easily swap the weather service by implementing the AbstractWeatherService interface for a different weather API.

•	Mocking: You can implement a mock weather service for testing purposes by adding a MockWeatherService class.



Project Structure

  weather-data-analysis
  
├weather_daily.py            # Main script to fetch and store weather data

├visualize_weather_data.py   # Script to generate and display visualizations

├README.md                   # Project documentation

Contributing

Contributions are welcome! If you’d like to contribute, please fork the repository and use a feature branch. Pull requests are also welcome.


![image](https://github.com/user-attachments/assets/c6166a2f-4507-4751-8a89-812381fd25e3)
