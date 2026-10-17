# Triangle Type Checker

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Sides must be positive")
elif a + b <= c or a + c <= b or b + c <= a:
    print("These sides cannot form a triangle")
elif a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
