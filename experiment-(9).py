def calculate_total_cost(prices, quantities, discount_rate, tax_rate):
 
    subtotal = sum(price * quantity for price, quantity in zip(prices, quantities))
    discount = subtotal * (discount_rate / 100)
    total_after_discount = subtotal - discount


    tax = total_after_discount * (tax_rate / 100)
    total_cost = total_after_discount + tax
    
    return total_cost

item_prices = [2.5, 3, 1.25, 5.75]  
quantities = [3, 2, 4, 1]           
discount_rate = 10                 
tax_rate = 8                         

total_cost = calculate_total_cost(item_prices, quantities, discount_rate, tax_rate)
print("Total cost for the customer's purchase: $", total_cost)
