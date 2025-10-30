###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int(input("Put in the first number: "))
number2 = int(input("Put in the second number: "))
operator = input("Put in the operator: ")

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
else:
    result = number1 / number2


# print result
print(f'{number1} {operator} {number2} = {result}')