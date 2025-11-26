numbers = [15, 8, 31, 47, 2, 19]

print("existed array:", *numbers)

reverse = []
for i in range(len(numbers) - 1, -1, -1):
    reverse.append(numbers[i])

print("reverse array:", *reverse)
