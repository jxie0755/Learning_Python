# This is to practice mulitple functions learned from OOP
# In this pratice, a superclass Shape is created, together with a few sub-class (Rectangle, Square, Circle)

from math import pi


class Shape(object):
    
    def __lt__(self, other):
        if self.area < other.area:
            return True
        else:
            return False
    
    def __le__(self, other):
        if self.area <= other.area:
            return True
        else:
            return False
    
    def __eq__(self, other):
        if self.area == other.area:
            return True
        else:
            return False


class Rectangle(Shape):
    
    def __init__(self, side1, side2):
        sides = sorted([side1, side2])
        self.width = sides[0]
        self.length = sides[1]
    
    def __str__(self):
        return f"Rectangle, {self.length} * {self.width}"
    
    @ property
    def area(self):
        return self.width * self.length
    
    @ property
    def perimeter(self):
        return 2 * (self.width + self.length)


class Square(Shape):
    
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f"Square, {self.side} * {self.side}"
    
    @ property
    def area(self):
        return self.side**2
    
    @ property
    def perimeter(self):
        return 4 * self.side


class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius
        
    def __str__(self):
        return f"Circle, R={self.radius}"
    
    @ property
    def area(self):
        return pi * self.radius**2
    
    @ property
    def perimeter(self):
        return pi * self.diameter



R1 = Rectangle(2,8)
print(R1.area)
print(R1.perimeter)

R2 = Rectangle(3,4)
print(R2)

S1 = Square(4)
print(S1)
print(S1.area)
print(R1 == S1)
print(R2 <= S1)

C1 = Circle(5)
print(C1)

print(C1.area)
print(C1 < R1)
