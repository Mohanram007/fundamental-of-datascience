import numpy as np

fuel_efficiency_data = np.array([25, 30, 20, 28, 32])  

average_fuel_efficiency = np.mean(fuel_efficiency_data)

fuel_efficiency_model_A = fuel_efficiency_data[0]
fuel_efficiency_model_B = fuel_efficiency_data[1]

percentage_improvement = ((fuel_efficiency_model_B - fuel_efficiency_model_A) / fuel_efficiency_model_A) * 100

print("Average fuel efficiency across all car models:", average_fuel_efficiency)
print("Percentage improvement in fuel efficiency between car model A and car model B:", percentage_improvement, "%")
