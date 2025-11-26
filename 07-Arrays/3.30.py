table = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

for i in range(5):          # wiersz (1..5)
    for j in range(5):      # kolumna (1..5)
        table[i][j] = (i + 1) * (j + 1)

for row in table:
    for value in row:
        print(value, end=" ")
    print()
