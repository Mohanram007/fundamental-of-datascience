from collections import Counter

weather_data = {
    'sunny': 150,
    'cloudy': 100,
    'rainy': 80,
    'snowy': 20,
    'foggy': 30
}

weather_distribution = Counter(weather_data)

most_common_weather = weather_distribution.most_common(1)[0]

print("The most common weather type is:", most_common_weather[0], "with", most_common_weather[1], "occurrences.")
