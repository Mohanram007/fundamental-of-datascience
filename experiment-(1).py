def most_common_weather(conditions):
    frequency = {}
    
    # Count the frequency of each weather condition
    for condition in conditions:
        frequency[condition] = frequency.get(condition, 0) + 1
    
    # Find the most common weather condition
    max_frequency = 0
    most_common = None
    for condition, freq in frequency.items():
        if freq > max_frequency:
            max_frequency = freq
            most_common = condition
    
    return most_common

# Example data of weather conditions
weather_conditions = [
    'sunny', 'sunny', 'rainy', 'cloudy', 'sunny', 'rainy', 'cloudy', 'cloudy', 'sunny', 'rainy'
]

# Call the function with the example data
most_common = most_common_weather(weather_conditions)

print("The most common weather condition is:", most_common)
