
n = int(input("Enter decimal number: "))

if n == 0:
    binary = "0"
else:
    remainders = []
    x = n
    while x > 0:
        remainders.append(str(x % 2))
        x //= 2
    binary = "".join(reversed(remainders))

print(f"{n}(10) = {binary}(2)")

