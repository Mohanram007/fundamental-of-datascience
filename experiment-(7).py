import numpy as np

house_data = np.genfromtxt(r"C:\Users\alext\Desktop\mohan 1\FOD\hourse_data.csv", delimiter=',', skip_header=1)  


houses_more_than_four_bedrooms = house_data[house_data[:, 0] > 4]  

sale_prices_more_than_four_bedrooms = houses_more_than_four_bedrooms[:, -1]  

average_sale_price_more_than_four_bedrooms = np.mean(sale_prices_more_than_four_bedrooms)

print("Average sale price of houses with more than four bedrooms:", average_sale_price_more_than_four_bedrooms)
