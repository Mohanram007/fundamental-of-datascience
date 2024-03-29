import numpy as np
from scipy import stats

group1_scores = [85, 90, 88, 92, 87]
group2_scores = [78, 82, 80, 85, 79]

mean_group1 = np.mean(group1_scores)
mean_group2 = np.mean(group2_scores)

sem_group1 = np.std(group1_scores) / np.sqrt(len(group1_scores))
sem_group2 = np.std(group2_scores) / np.sqrt(len(group2_scores))

ci_group1 = stats.norm.interval(0.95, loc=mean_group1, scale=sem_group1)
ci_group2 = stats.norm.interval(0.95, loc=mean_group2, scale=sem_group2)

print("Group 1 Mean Score:", mean_group1)
print("Group 1 95% Confidence Interval:", ci_group1)
print()
print("Group 2 Mean Score:", mean_group2)
print("Group 2 95% Confidence Interval:", ci_group2)

t_stat, p_value = stats.ttest_ind(group1_scores, group2_scores, equal_var=False)

print("\nHypothesis Test Results:")
print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Reject the null hypothesis. There is a significant difference between the two groups.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference between the two groups.")
