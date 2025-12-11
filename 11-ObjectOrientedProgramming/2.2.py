class Square:
   def __init__(self, a):
      self.a = a
   def area(self):
      return self.a * self.a
   def perimeter(self):
      return self.a * 4

square1 = Square(4)
square2 = Square(6)

print('Square with side 4:')
print(f'Area = {square1.area()}, Perimeter = {square1.perimeter()}')
print('Square with side 6:')
print(f'Area = {square2.area()}, Perimeter = {square2.perimeter()}')
...