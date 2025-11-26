product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

total_value = 0
for i in range(len(product_prices)):
    total_value += product_prices[i] * product_quantities[i]

print("Total value of goods:", total_value)
