def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])
    transposed = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(m[i][j])
        transposed.append(new_row)

    return transposed

def print_matrix(m):
    for row in m:
        for value in row:
            print(value, end=" ")
        print()
    print()

m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

m2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

m3 = [
    [5, 6, 7, 8]
]

for idx, m in enumerate((m1, m2, m3), start=1):
    print(f"Matrix {idx}:")
    print_matrix(m)
    print(f"Transposed {idx}:")
    print_matrix(transpose_matrix(m))
