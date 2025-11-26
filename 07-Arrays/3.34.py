def identity_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def print_2d_array(arr):
    for row in arr:
        for value in row:
            print(value, end=" ")
        print()
    print()

for size in (3, 5, 8):
    print(f"Identity matrix {size}x{size}")
    m = identity_matrix(size)
    print_2d_array(m)
