# CS61A Lecture 04: Higher-Order Functions

# DRY principle (Don't repeat yourself)

def same_length(a, b):
    """Return whether positive integers a and b have the same number of digits.

    >>> same_length(50, 70)
    True
    >>> same_length(50, 100)
    False
    >>> same_length(1000, 100000)
    False
    """
    return digits(a) == digits(b)
    # a_digits = 0
    # while a > 0:
    #     last, a = a % 10, a // 10
    #     a_digits = a_digits + 1
    # b_digits = 0
    # while b > 0:
    #     last, b = b % 10, b // 10
    #     b_digits = b_digits + 1
    # return a_digits == b_digits

def digits(a):
    a_digits = 0
    while a > 0:
        a, last = a // 10, a % 10
        a_digits = a_digits + 1
    return a_digits

# instead of writing the same type of code blocks twice, better to create a function to specifically count the number of digits. Then apply it to both a and b and compare.


# Generalizing patterns using arguments

from math import pi, sqrt

def area_square(r):
    """Return the area of a square with side length R."""
    return r * r

def area_circle(r):
    """Return the area of a circle with radius R."""
    return r * r * pi

def area_hexagon(r):
    """Return the area of a regular hexagon with side length R."""
    return r * r * 3 * sqrt(3) / 2

# need to assert that the length is posive by
# adding a line assert r > 0 in every function
# That will be repeating

# So a better way is to create a way to create a function as a genreal method

def area(r, shape_constant):
    """Return the area of a shape from length measurement R."""
    assert r > 0, "A length must be positive"
    return r * r * shape_constant

def area_square(r):
    return area(r, 1)

def area_circle(r):
    return area(r, pi)

def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)

# Then define the 3 shape function differently in a different way that separates the constant part and the side of length.of


# Functions as arguments

def sum_naturals(n):
    """Sum the first N natural numbers.

    >>> sum_naturals(5)
    15
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

def sum_cubes(n):
    """Sum the first N cubes of natural numbers.

    >>> sum_cubes(5)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total

# New way of using function as argument

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Sum the first N terms of a sequence.

    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def sum_naturals(n):
    """Sum the first N natural numbers.

    >>> sum_naturals(5)
    15
    """
    return summation(n, identity)
def sum_cubes(n):
    """Sum the first N cubes of natural numbers.

    >>> sum_cubes(5)
    225
    """
    return summation(n, cube)

from operator import mul

def pi_term(k):
    return 8 / mul(k * 4 - 3, k * 4 - 1)

print(summation(1000000, pi_term))


# A third example

def make_adder(n):
    """Return a function that takes one argument K and returns K + N.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

add_three = make_adder(3)
print(add_three(4))

print(make_adder(4)(9))  # >>> 13



# My practice, create the map function in python in my own way
def mapX(func, iterable):
    for i in iterable:
        yield func(i)

print(list(mapX(lambda x:x*2, [1,2,3,4])))
# >>> [2, 4, 6, 8]


# Lambda expression
square = lambda x:x*x
print(square(4))

def square(x):
    return x*x

# try multiple arugments
adder = lambda x, y: x+y
print(adder(3,4))
