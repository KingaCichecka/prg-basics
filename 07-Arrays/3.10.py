array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]

print("Numbers from first array that do not appear in second array:")

for x in array1:
    found = False
    for y in array2:
        if x == y:
            found = True
            break
    if not found:
        print(x, end=" ")
