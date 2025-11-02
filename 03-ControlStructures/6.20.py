
amount = int(input("Enter the amount in PLN: "))

coins_5 = amount // 5
rest   = amount % 5
coins_2 = rest // 2
coins_1 = rest % 2

print(f"The amount of PLN {amount} in coins:")
if coins_5: print(f"5 PLN coins: {coins_5}")
if coins_2: print(f"2 PLN coins: {coins_2}")
if coins_1 or amount == 0: print(f"1 PLN coins: {coins_1}")
