def create_2d_arr(x, y):
    arr = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(0)
        arr.append(row)
    return arr

array_3x5 = create_2d_arr(3, 5)

for row in array_3x5:
    print(row)
