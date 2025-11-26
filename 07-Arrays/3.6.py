numbers = [15, 8, 31, 47, 2, 19]

i = 0
total = 0

while i < len(numbers):
    total += numbers[i]
    i += 1

mean = total / len(numbers)

print("Array:", *numbers)
print("Arithmetic mean:", mean)
