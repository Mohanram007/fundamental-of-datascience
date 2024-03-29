import numpy as np
from scipy import stats

product1_lifespans = [45, 50, 55, 48, 52]
product2_lifespans = [40, 42, 38, 43, 41]

mean_lifespan_product1 = np.mean(product1_lifespans)
mean_lifespan_product2 = np.mean(product2_lifespans)

sem_product1 = np.std(product1_lifespans) / np.sqrt(len(product1_lifespans))
sem_product2 = np.std(product2_lifespans) / np.sqrt(len(product2_lifespans))

ci_product1 = stats.norm.interval(0.90, loc=mean_lifespan_product1, scale=sem_product1)
ci_product2 = stats.norm.interval(0.90, loc=mean_lifespan_product2, scale=sem_product2)

print("Product Type 1 Mean Lifespan:", mean_lifespan_product1)
print("Product Type 1 90% Confidence Interval:", ci_product1)
print()
print("Product Type 2 Mean Lifespan:", mean_lifespan_product2)
print("Product Type 2 90% Confidence Interval:", ci_product2)

t_stat, p_value = stats.ttest_ind(product1_lifespans, product2_lifespans, equal_var=False)

print("\nHypothesis Test Results:")
print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Reject the null hypothesis. There is a significant difference in lifespans between the two product types.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in lifespans between the two product types.")
