numbers = [2.5, 7.1, 3.3, 10.0, 5.5, 1.2]

value = float(input("Enter value: "))

count = 0
for x in numbers:
    if x > value:
        count += 1

print("Array:", numbers)
print("Number of elements greater than", value, ":", count)
