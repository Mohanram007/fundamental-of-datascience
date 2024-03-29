import pandas as pd

property_data = pd.DataFrame({
    'property_id': [1, 2, 3, 4, 5],
    'location': ['Location A', 'Location B', 'Location A', 'Location C', 'Location B'],
    'bedrooms': [3, 4, 5, 3, 6],
    'area_in_square_feet': [1500, 1800, 2000, 1600, 2200],
    'listing_price': [250000, 300000, 350000, 280000, 400000]
})

avg_price_per_location = property_data.groupby('location')['listing_price'].mean()

print("Average Listing Price of Properties in Each Location:")
print(avg_price_per_location)


num_properties_more_than_four_bedrooms = property_data[property_data['bedrooms'] > 4].shape[0]

print("Number of Properties with More Than Four Bedrooms:", num_properties_more_than_four_bedrooms)
print()

property_largest_area = property_data.loc[property_data['area_in_square_feet'].idxmax()]

print("Property with the Largest Area:")
print(property_largest_area)
