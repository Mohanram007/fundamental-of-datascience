import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("customer_reviews.csv")

category = "your_chosen_category"
category_reviews = df[df['categories'] == category]['reviews rating']

mean_rating = category_reviews.mean()
std_dev = category_reviews.std()

n = len(category_reviews)
sem = std_dev / np.sqrt(n)

confidence_level = 0.95

margin_of_error = stats.t.ppf((1 + confidence_level) / 2, n - 1) * sem

ci_lower = mean_rating - margin_of_error
ci_upper = mean_rating + margin_of_error

print("Product Category:", category)
print("Mean Rating:", mean_rating)
print("Standard Deviation:", std_dev)
print("Confidence Intervals ({}%): ({}, {})".format(confidence_level * 100, ci_lower, ci_upper))
