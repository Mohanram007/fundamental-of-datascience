import pandas as pd

sales_data = pd.DataFrame({
    'product': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product A'],
    'quantity_sold': [10, 20, 30, 15, 25, 20]
})

product_sales = sales_data.groupby('product')['quantity_sold'].sum()

top_5_products = product_sales.sort_values(ascending=False).head(5)

print("Top 5 Products Sold in the Past Month:")
print(top_5_products)
