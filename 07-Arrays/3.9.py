def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True

arrays = [
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2])
]

for idx, (a1, a2) in enumerate(arrays, start=1):
    print(f"{idx}. Array1:", *a1)
    print(f"   Array2:", *a2)
    are_same = compare(a1, a2)
    if are_same:
        print("   Comparison: arrays are the same")
    else:
        print("   Comparison: arrays are different")
    print()
