import pandas as pd
import matplotlib.pyplot as plt

temperature_rainfall_data = pd.read_csv(r"C:\Users\alext\Desktop\mohan 1\FOD\temperature_rainfall_data.csv")

plt.figure(figsize=(10, 6)) 
plt.plot(temperature_rainfall_data['month'], temperature_rainfall_data['temperature'], marker='o', linestyle='-')
plt.title('Monthly Temperature Data')  
plt.xlabel('Month') 
plt.ylabel('Temperature (°C)')  
plt.grid(True)  
plt.xticks(rotation=45)  
plt.tight_layout()  
plt.show()  


plt.figure(figsize=(10, 6))  
plt.scatter(temperature_rainfall_data['month'], temperature_rainfall_data['rainfall'], color='blue', alpha=0.5,linestyle='--')  
plt.title('Monthly Rainfall Data')  
plt.xlabel('Month')  
plt.ylabel('Rainfall (mm)') 
plt.grid(True) 
plt.xticks(rotation=45) 
plt.tight_layout() 
plt.show()  
