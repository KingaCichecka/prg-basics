N = int(input("How many prime numbers to print? "))

def is_prime(x: int) -> bool:
    if x < 2:
        return False
    if x in (2, 3):
        return True
    if x % 2 == 0:
        return False
    d = 3
    while d * d <= x:
        if x % d == 0:
            return False
        d += 2
    return True

count = 0
num = 2
primes = []

while count < N:
    if is_prime(num):
        primes.append(str(num))
        count += 1
    num += 1

print("Prime numbers:", " ".join(primes))