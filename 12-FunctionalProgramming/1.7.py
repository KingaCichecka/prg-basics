is_even = lambda number: number % 2 == 0

n = int(input("Enter a number: "))
print("Even" if is_even(n) else "Odd")
