import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv(r"C:\Users\alext\Desktop\mohan 1\FOD\sales_data.csv")

plt.figure(figsize=(10, 6)) 
plt.plot(sales_data['month'], sales_data['sales'], marker='*', linestyle='--')  
plt.title('Monthly Sales Data') 
plt.xlabel('Month')  
plt.ylabel('Sales')  
plt.grid(True)  
plt.xticks(rotation=45)  
plt.tight_layout() 
plt.show() 

plt.figure(figsize=(10, 6))  
plt.bar(sales_data['month'], sales_data['sales'], color='skyblue')  
plt.title('Monthly Sales Data')  
plt.xlabel('Month')  
plt.ylabel('Sales') 
plt.grid(axis='y')
plt.xticks(rotation=45)  
plt.tight_layout() 
plt.show() 

