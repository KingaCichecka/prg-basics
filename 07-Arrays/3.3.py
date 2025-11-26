numbers = [8, 2, 5, 1, 9]

print("Array:", *numbers)

squared = []
for x in numbers:
    squared.append(x ** 2)

print("2nd power:", *squared)
