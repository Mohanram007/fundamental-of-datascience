import numpy as np
import matplotlib.pyplot as plt

time_spent = [8, 12, 5, 15, 10, 20, 7, 18, 25, 8, 12, 22, 15, 10, 30, 7, 18, 15, 20, 12]
median_time_spent = np.median(time_spent)

first_quartile = np.percentile(time_spent, 25)
third_quartile = np.percentile(time_spent, 75)
iqr = third_quartile - first_quartile

lower_bound = first_quartile - 1.5 * iqr
upper_bound = third_quartile + 1.5 * iqr
potential_outliers = [x for x in time_spent if x < lower_bound or x > upper_bound]

plt.boxplot(time_spent)
plt.xlabel('Time Spent (minutes)')
plt.ylabel('Frequency')
plt.title('Distribution of Time Spent on Website')
plt.grid(True)
plt.show()
print("Median of time spent on the website:", median_time_spent)
print("Interquartile Range (IQR):", iqr)
print("Potential outliers:", potential_outliers)
