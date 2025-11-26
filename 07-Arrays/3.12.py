array = [2, 3, 2, 5, 8, 1, 9, 8]

unique = []

for i in range(len(array)):
    value = array[i]
    count = 0
    for j in range(len(array)):
        if array[j] == value:
            count += 1
    if count == 1:
        unique.append(value)

print("Array:", *array)
print("Unique elements:", *unique)
