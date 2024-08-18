import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Set Seaborn style for better aesthetics
sns.set(style="whitegrid")

def fetch_data_from_db(db_name='weather_data_storage.db'):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query("SELECT * FROM DailyTemperature", conn)
    conn.close()
    
    # Convert the Date column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.date
    
    # Filter data to get only the last 3 months
    three_months_ago = datetime.datetime.now().date() - datetime.timedelta(days=92)
    df = df[df['Date'] >= three_months_ago]
    
    return df

def plot_line_chart(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['MinTemperature'], label='Min Temperature', marker='o', color='dodgerblue', linewidth=2)
    plt.plot(df['Date'], df['MaxTemperature'], label='Max Temperature', marker='o', color='darkorange', linewidth=2)
    plt.fill_between(df['Date'], df['MinTemperature'], df['MaxTemperature'], color='lightgray', alpha=0.3)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Temperature (°C)', fontsize=14)
    plt.title('Daily Min and Max Temperatures (Last 3 Months)', fontsize=16)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_temperature_range(df):
    plt.figure(figsize=(12, 6))
    df['TemperatureRange'] = df['MaxTemperature'] - df['MinTemperature']
    plt.plot(df['Date'], df['TemperatureRange'], label='Temperature Range', color='purple', marker='o', linestyle='--', linewidth=2)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Temperature Range (°C)', fontsize=14)
    plt.title('Daily Temperature Range (Last 3 Months)', fontsize=16)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_rolling_average(df, window=7):
    plt.figure(figsize=(12, 6))
    df['MinTempRollingAvg'] = df['MinTemperature'].rolling(window=window).mean()
    df['MaxTempRollingAvg'] = df['MaxTemperature'].rolling(window=window).mean()
    plt.plot(df['Date'], df['MinTempRollingAvg'], label=f'Min Temp {window}-Day Avg', marker='o', color='teal', linewidth=2)
    plt.plot(df['Date'], df['MaxTempRollingAvg'], label=f'Max Temp {window}-Day Avg', marker='o', color='tomato', linewidth=2)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Temperature (°C)', fontsize=14)
    plt.title(f'{window}-Day Rolling Average of Min and Max Temperatures (Last 3 Months)', fontsize=16)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_temperature_histogram(df):
    plt.figure(figsize=(12, 6))
    plt.hist(df['MinTemperature'], bins=15, alpha=0.7, label='Min Temperature', color='cornflowerblue', edgecolor='black')
    plt.hist(df['MaxTemperature'], bins=15, alpha=0.7, label='Max Temperature', color='salmon', edgecolor='black')
    plt.xlabel('Temperature (°C)', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.title('Histogram of Temperature Distribution (Last 3 Months)', fontsize=16)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_min_vs_max_scatter(df):
    plt.figure(figsize=(12, 6))
    plt.scatter(df['MinTemperature'], df['MaxTemperature'], alpha=0.7, color='mediumseagreen', edgecolor='black', s=100)
    plt.xlabel('Min Temperature (°C)', fontsize=14)
    plt.ylabel('Max Temperature (°C)', fontsize=14)
    plt.title('Scatter Plot of Min vs Max Temperatures (Last 3 Months)', fontsize=16)
    plt.tight_layout()
    plt.show()

def plot_temperature_boxplot(df):
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=[df['MinTemperature'], df['MaxTemperature']], palette=['lightblue', 'lightcoral'])
    plt.xticks([0, 1], ['Min Temperature', 'Max Temperature'], fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=14)
    plt.title('Box Plot of Min and Max Temperatures (Last 3 Months)', fontsize=16)
    plt.tight_layout()
    plt.show()

def plot_temperature_violinplot(df):
    plt.figure(figsize=(12, 6))
    sns.violinplot(data=df[['MinTemperature', 'MaxTemperature']], palette=['skyblue', 'pink'])
    plt.xticks([0, 1], ['Min Temperature', 'Max Temperature'], fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=14)
    plt.title('Violin Plot of Min and Max Temperatures (Last 3 Months)', fontsize=16)
    plt.tight_layout()
    plt.show()

def visualize_data():
    db_name = 'weather_data_storage.db'
    df = fetch_data_from_db(db_name)
    
    # Call plot functions
    plot_line_chart(df)
    plot_temperature_range(df)
    plot_rolling_average(df, window=7)
    plot_temperature_histogram(df)
    plot_min_vs_max_scatter(df)
    plot_temperature_boxplot(df)
    plot_temperature_violinplot(df)

if __name__ == "__main__":
    visualize_data()
