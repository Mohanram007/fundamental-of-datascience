import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

placebo_group = [82, 75, 80, 78, 79, 85, 88, 70, 72, 76]
treatment_group = [90, 85, 88, 92, 87, 94, 91, 86, 89, 93]

mean_placebo = np.mean(placebo_group)
mean_treatment = np.mean(treatment_group)

t_stat, p_value = stats.ttest_ind(placebo_group, treatment_group)

plt.figure(figsize=(10, 6))
plt.bar([0, 1], [mean_placebo, mean_treatment], color=['blue', 'orange'], alpha=0.7)
plt.xticks([0, 1], ['Placebo', 'Treatment'])
plt.ylabel('Mean Effectiveness')
plt.title('Effectiveness of Treatment vs. Placebo')
plt.grid(axis='y')

plt.text(0.5, max(mean_placebo, mean_treatment) * 0.9, f'P-value = {p_value:.4f}', ha='center', fontsize=12)

plt.show()

print("Hypothesis Test Results:")
print("T-statistic:", t_stat)
print("P-value:", p_value)

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. The new treatment has a statistically significant effect compared to the placebo.")
else:
    print("Fail to reject the null hypothesis. There is no statistically significant effect of the new treatment compared to the placebo.")
