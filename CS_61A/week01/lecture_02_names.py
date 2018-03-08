# Imports
from math import pi
print(pi * 71 / 223)
from math import sin
print(sin)
sin(pi/2)

# Assignment
print()
radius = 10
print(2 * radius)
area, circ = pi * radius * radius, 2 * pi * radius
radius = 20

# Function values
print()
print(max)
print(max(3, 4))
f = max
print(f)
print(f(3, 4))
max = 7
print(f(3, 4))
print(f(3, max))
f = 2
# f(3, 4)
import builtins
max = builtins.max

# User-defined functions
print()
from operator import add, mul
def square(x):
    return mul(x, x)

print(square(21))
print(square(add(2, 5)))
print(square(square(3)))

def sum_squares(x, y):
    return add(square(x), square(y))
print(sum_squares(3, 4))
print(sum_squares(5, 12))

# this = that
def this():
    return that
# this()
that = 100
print(this())

# Name conflicts
def square(square):
    return mul(square, square)
print(square(4))

# Little quiz
print()
a = min(max(2, min(max(1, 5), 3)), 4)  # answer in front to avoid conflict

f = min
f = max
g, h = min, max
max = g
b = max(f(2, g(h(1, 5), 3)), 4)
print(a == b)
# This can be easily solved the environment diagrams
