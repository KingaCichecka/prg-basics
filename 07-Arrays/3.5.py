numbers = [15, 8, 31, 47, 2, 19]

total = 0
for x in numbers:
    total += x

mean = total / len(numbers)

print("Array:", *numbers)
print("Arithmetic mean:", mean)
