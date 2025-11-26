def flatten_2d(array2d):
    result = []
    for row in array2d:
        for value in row:
            result.append(value)
    return result

# i.
arr1 = [
    [2, 3],
    [1, 5]
]

# ii.
arr2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

# iii.
arr3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

for idx, arr in enumerate((arr1, arr2, arr3), start=1):
    print(f"2D array {idx}:")
    for row in arr:
        print(row)
    flat = flatten_2d(arr)
    print("1D version:", flat)
    print()
