###
# 25% discount for each item beyond the first two
#
count = int(input("Number of products purchased: "))
price = float(input("Product price: "))

full_price_items = min(count, 2)
discount_items   = max(0, count - 2)

amount = full_price_items * price + discount_items * (0.75 * price)
print(f"Amount to pay: {amount:.2f}")
