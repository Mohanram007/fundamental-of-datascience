import numpy as np
import matplotlib.pyplot as plt

# Generate example exam scores (replace with your actual data)
np.random.seed(0)
exam_scores = np.random.randint(40, 101, size=50)

# Plot histogram
plt.hist(exam_scores, bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Exam Scores')
plt.ylabel('Frequency')
plt.title('Distribution of Exam Scores')
plt.grid(True)
plt.show()
