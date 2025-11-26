array1 = [1, 3, 5]
array2 = [1, 2, 3, 4, 5, 6]

is_subset = True

for x in array1:
    found = False
    for y in array2:
        if x == y:
            found = True
            break
    if not found:
        is_subset = False
        break

print("Array1:", array1)
print("Array2:", array2)
print("Array1 is subset of Array2:", is_subset)
