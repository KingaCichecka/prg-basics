numbers = [2, 6, 4, 9, 7]

def star(n):
    result = ""
    for i in range(n):
        result += "*"
    return result

for n in numbers:
    print(f"{n}: {star(n)}")
