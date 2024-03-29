import pandas as pd
import matplotlib.pyplot as plt

weather_data = pd.read_csv(r"C:\Users\alext\Desktop\mohan 1\FOD\weather_data.csv")

weather_data['date'] = pd.to_datetime(weather_data['date'])

weather_data['year'] = weather_data['date'].dt.year
weather_data['month'] = weather_data['date'].dt.month

monthly_avg_temp = weather_data.groupby('month')['temperature'].mean()

plt.figure(figsize=(10, 6))
monthly_avg_temp.plot(marker='o', color='blue')
plt.title('Average Temperature Trends Over Different Months')
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(weather_data['date'], weather_data['precipitation'], color='green')
plt.title('Precipitation Over Time')
plt.xlabel('Date')
plt.ylabel('Precipitation (mm)')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(weather_data['temperature'], bins=20, color='orange', alpha=0.7)
plt.title('Temperature Distribution')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

extreme_temps = weather_data[(weather_data['temperature'] < 0) | (weather_data['temperature'] > 30)]
plt.figure(figsize=(10, 6))
plt.hist(weather_data['temperature'], bins=20, color='orange', alpha=0.7)
plt.scatter(extreme_temps['date'], extreme_temps['temperature'], color='red', label='Extreme Events')
plt.title('Temperature Distribution with Extreme Events')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()
