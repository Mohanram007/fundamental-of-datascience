import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt

transaction_data = pd.read_csv("transaction_data.csv")

X = transaction_data[['TotalAmountSpent', 'FrequencyOfVisits']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

n_clusters = 3

kmeans = KMeans(n_clusters=n_clusters, random_state=42)

pipeline = make_pipeline(StandardScaler(), kmeans)

pipeline.fit(X)

transaction_data['Cluster'] = pipeline.predict(X)
\
plt.figure(figsize=(8, 6))
plt.scatter(transaction_data['TotalAmountSpent'], transaction_data['FrequencyOfVisits'], c=transaction_data['Cluster'], cmap='viridis')
plt.title('Customer Segmentation by Spending Patterns')
plt.xlabel('Total Amount Spent')
plt.ylabel('Frequency of Visits')
plt.colorbar(label='Cluster')
plt.show()

cluster_means = transaction_data.groupby('Cluster').mean()
print(cluster_means)
