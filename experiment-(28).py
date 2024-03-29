import numpy as np
from scipy import stats

design_A_conversions = 120  
design_A_visitors = 1000   

design_B_conversions = 150  
design_B_visitors = 1100   

conversion_rate_A = design_A_conversions / design_A_visitors
conversion_rate_B = design_B_conversions / design_B_visitors

z_stat, p_value = stats.norm.sf(abs((conversion_rate_A - conversion_rate_B) / np.sqrt((conversion_rate_A * (1 - conversion_rate_A)) / design_A_visitors + (conversion_rate_B * (1 - conversion_rate_B)) / design_B_visitors)))*2

print("Conversion Rate for Design A:", conversion_rate_A)
print("Conversion Rate for Design B:", conversion_rate_B)
print("\nHypothesis Test Results:")
print("Z-statistic:", z_stat)
print("P-value:", p_value)

alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis. There is a statistically significant difference in the mean conversion rates between the two website designs.")
else:
    print("Fail to reject the null hypothesis. There is no statistically significant difference in the mean conversion rates between the two website designs.")
