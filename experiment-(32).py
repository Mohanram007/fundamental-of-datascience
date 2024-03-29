import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

data = pd.read_csv("medical_data.csv")

X = data.drop(columns=['TreatmentOutcome'])
y = data['TreatmentOutcome']

label_encoder = LabelEncoder()
X['Gender'] = label_encoder.fit_transform(X['Gender'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

k = 5

knn = KNeighborsClassifier(n_neighbors=k)

knn.fit(X_train_scaled, y_train)

y_pred = knn.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label='Good')
recall = recall_score(y_test, y_pred, pos_label='Good')
f1 = f1_score(y_test, y_pred, pos_label='Good')

print("Model Performance:")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("\nPredictions on the test set:")
print(results)
