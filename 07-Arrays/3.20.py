arr = [7, 9, 2, 4, 5, 6]

even = []
odd = []

for x in arr:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

result = even + odd

print("arr =", arr)
print("arr =", result)
