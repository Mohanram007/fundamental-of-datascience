import pandas as pd


customer_demographics = pd.read_csv(r"C:\Users\alext\Desktop\mohan 1\FOD\day1-(5) csv files\customer_demographics.csv")
user_activity_logs = pd.read_csv(r"C:\Users\alext\Desktop\mohan 1\FOD\day1-(5) csv files\User Activity Logs.csv")
customer_support = pd.read_csv(r"C:\Users\alext\Desktop\mohan 1\FOD\day1-(5) csv files\Customer Support Interactions.csv")


merged_data = pd.merge(customer_demographics, user_activity_logs, on='customer_id', how='inner')
merged_data = pd.merge(merged_data, customer_support, on='customer_id', how='left')


print("Consolidated Dataset:")
print(merged_data.head())
