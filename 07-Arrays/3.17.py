numbers = (50, 20, 40, 50, 30, 50)
value = 50

count = 0
for x in numbers:
    if x == value:
        count += 1

print("Tuple:", numbers)
print("Value:", value)
print("Number of occurrences:", count)
