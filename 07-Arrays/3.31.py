numbers = [
    [-38, 19],
    [5, 40],
    [-7, 11],
    [29, 16]
]

min_val = numbers[0][0]
max_val = numbers[0][0]
min_pos = (0, 0)
max_pos = (0, 0)

for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        val = numbers[i][j]
        if val < min_val:
            min_val = val
            min_pos = (i, j)
        if val > max_val:
            max_val = val
            max_pos = (i, j)

print("Array:")
for row in numbers:
    print(row)

print("Minimum:", min_val, "at row", min_pos[0], "column", min_pos[1])
print("Maximum:", max_val, "at row", max_pos[0], "column", max_pos[1])
