arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Before:")
for row in arr:
    print(row)

rows = len(arr)
cols = len(arr[0])

for i in range(rows):
    arr[i][0], arr[i][cols - 1] = arr[i][cols - 1], arr[i][0]

print("After:")
for row in arr:
    print(row)
