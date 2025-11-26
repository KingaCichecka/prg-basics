# "Module" MyArrays – zestaw funkcji do tablic liczb

def second_largest(array):
    # własne sortowanie (bubble sort)
    arr = array[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr[-2]

def difference_max_min(array):
    # bez wbudowanych funkcji
    min_val = array[0]
    max_val = array[0]
    for x in array[1:]:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    return max_val - min_val

def median(array):
    # sortowanie bez built-in
    arr = array[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    mid = n // 2
    if n % 2 == 1:
        return arr[mid]
    else:
        return (arr[mid - 1] + arr[mid]) / 2

def min_max(array):
    min_val = array[0]
    max_val = array[0]
    for x in array[1:]:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    return [min_val, max_val]

def to_string_minus(array):
    result = ""
    for i in range(len(array)):
        result += str(array[i])
        if i != len(array) - 1:
            result += "-"
    return result

# Program wykorzystujący MyArrays
numbers = [7, 3, 8, 5, 2]

print("Numbers:", ",".join(str(x) for x in numbers))
print("Second largest number:", second_largest(numbers))
print("Median:", median(numbers))

mm = min_max(numbers)
print("Smallest and largest number:", f"{mm[0]},{mm[1]}")
print("Numbers as a string:", to_string_minus(numbers))
