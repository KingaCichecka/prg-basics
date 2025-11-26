numbers = [34, 7, 19, 4, 21, 8]

i = 0
even_count = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        even_count += 1
    i += 1

print("Array:", numbers)
print("Number of even values:", even_count)
