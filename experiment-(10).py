import pandas as pd

order_data = pd.read_csv(r"C:\Users\alext\Desktop\mohan 1\FOD\order_data.csv")

orders_per_customer = order_data.groupby('Customer ID').size()
print("Total number of orders made by each customer:")
print(orders_per_customer)

average_order_quantity_per_product = order_data.groupby('Product Name')['Order Quantity'].mean()
print("\nAverage order quantity for each product:")
print(average_order_quantity_per_product)

earliest_order_date = order_data['Order Date'].min()
latest_order_date = order_data['Order Date'].max()
print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
