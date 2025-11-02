###
# Point location in the coordinate system
#
x = float(input("x = "))
y = float(input("y = "))

if x == 0 and y == 0:
    print("Point P(0,0) is at the origin")
elif x == 0:
    print(f"Point P({x},{y}) lies on the Y axis")
elif y == 0:
    print(f"Point P({x},{y}) lies on the X axis")
elif x > 0 and y > 0:
    print(f"Point P({x},{y}) is in the first quadrant")
elif x < 0 and y > 0:
    print(f"Point P({x},{y}) is in the second quadrant")
elif x < 0 and y < 0:
    print(f"Point P({x},{y}) is in the third quadrant")
else:  # x > 0 and y < 0
    print(f"Point P({x},{y}) is in the fourth quadrant")
