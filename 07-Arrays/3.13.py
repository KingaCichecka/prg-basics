def occurs(number, array):
    for x in array:
        if x == number:
            return True
    return False

array = [15, 38, 7, 23, 14]

number = int(input("Number: "))
print("Array:", *array)

if occurs(number, array):
    print("Result: number", number, "appears in the array")
else:
    print("Result: number", number, "does not appear in the array")
