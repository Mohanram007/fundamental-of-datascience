def most_common_disease(disease_data):
    frequency = {}
    for i in range(0, len(disease_data), 2):
        disease_name = disease_data[i]
        patients_diagnosed = disease_data[i + 1]
        if disease_name in frequency:
            frequency[disease_name] += patients_diagnosed
        else:
            frequency[disease_name] = patients_diagnosed
    
    max_frequency = max(frequency.values())
    most_common = [disease for disease, freq in frequency.items() if freq == max_frequency]
    
    return most_common


disease_data = [
    "Common Cold", 320,
    "Diabetes", 120,
    "Bronchitis", 100,
    "Influenza", 150,
    "Kidney Stones", 6
]

most_common = most_common_disease(disease_data)
print("The most common disease is:", most_common[0])
