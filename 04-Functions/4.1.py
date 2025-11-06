import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
a = 3
b = 4
c = 5
print(f"The area of ​​a triangle with sides {a},{b},{c} is {triangle_area(a, b, c)}")
a = 5
b = 12
c = 13
print(f"The area of ​​a triangle with sides {a},{b},{c} is {triangle_area(a, b, c)}")
a = 7
b = 24
c = 25
print(f"The area of ​​a triangle with sides {a},{b},{c} is {triangle_area(a, b, c)}")