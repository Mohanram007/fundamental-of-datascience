import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv(r"C:\Users\alext\Desktop\mohan 1\FOD\sales_data.csv")

sales_data['date'] = pd.to_datetime(sales_data['date'])

sales_data.set_index('date', inplace=True)

plt.figure(figsize=(10, 6))  
sales_data.resample('M').sum().plot(marker='o', linestyle='-')  
plt.title('Monthly Sales') 
plt.xlabel('Date')  
plt.ylabel('Sales') 
plt.grid(True)  
plt.xticks(rotation=45)  
plt.tight_layout()  
plt.show()  

plt.figure(figsize=(10, 6)) 
plt.scatter(sales_data.index, sales_data['sales'], color='blue', alpha=0.5)  
plt.title('Sales Over Time') 
plt.xlabel('Date')  
plt.ylabel('Sales')  
plt.grid(True)  
plt.xticks(rotation=45)  
plt.tight_layout() 
plt.show()  

plt.figure(figsize=(10, 6)) 
sales_data.resample('M').sum().plot(kind='bar', color='skyblue')  
plt.title('Monthly Sales')  
plt.xlabel('Date')  
plt.ylabel('Sales') 
plt.grid(axis='y') 
plt.xticks(rotation=45)  
plt.tight_layout()  
plt.show() 
