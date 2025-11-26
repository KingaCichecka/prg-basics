numbers = [-15, 8, -31, 47, -2, 19]

min_val = numbers[0]
max_val = numbers[0]

for x in numbers[1:]:
    if x < min_val:
        min_val = x
    if x > max_val:
        max_val = x

print("Array:", numbers)
print("Minimum:", min_val)
print("Maximum:", max_val)
