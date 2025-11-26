def bubblesort(array):
    arr = array[:]          # kopia, żeby nie zmieniać oryginału
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

a1 = [8, 2, 5, 1, 9]
a2 = [4, 36, 12, 28, 9, 44, 5]
a3 = [15, 8, 31, 47, 2, 19]

for arr in (a1, a2, a3):
    print("Original:", arr)
    print("Sorted  :", bubblesort(arr))
    print()
