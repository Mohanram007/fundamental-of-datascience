import numpy as np
import matplotlib.pyplot as plt

scores = np.array([85, 78, 92, 89, 67, 76, 94, 82, 91, 88, 75, 81, 96, 90, 79, 83, 77, 85, 98, 72])

mean_score = np.mean(scores)
median_score = np.median(scores)
first_quartile = np.percentile(scores, 25)
third_quartile = np.percentile(scores, 75)

iqr = third_quartile - first_quartile

lower_bound = first_quartile - 1.5 * iqr
upper_bound = third_quartile + 1.5 * iqr
potential_outliers = scores[(scores < lower_bound) | (scores > upper_bound)]

print("Mean Score:", mean_score)
print("Median Score:", median_score)
print("First Quartile (Q1):", first_quartile)
print("Third Quartile (Q3):", third_quartile)
print("Interquartile Range (IQR):", iqr)
print("Potential Outliers:", potential_outliers)


plt.boxplot(scores)
plt.xlabel('Scores')
plt.ylabel('Values')
plt.title('Box Plot of Scores')
plt.grid(True)
plt.show()
