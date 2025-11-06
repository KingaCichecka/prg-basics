import math

def sum_digits(number):
    number = abs(number)
    total = 0
    for digit in str(number):
        total += int(digit)
    return total
any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print('The sum of the digits in the number is', result)
