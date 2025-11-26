import random

def rand_elem(array):
    index = random.randint(0, len(array) - 1)
    return array[index]

array = [10, 20, 30, 40, 50, 60, 70]

print("Array:", array)
print("Random elements:")
for i in range(5):
    print(rand_elem(array))
