""" Lab 3: Recursion and Midterm Review """
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


# Q1 GCD
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if a < b:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(a % b, b)


# Q2 Hailstone recuision
def hailstone(n, r=0):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """,
    print(n)
    if n == 1:
        return r + 1
    elif n % 2 == 0:
        return hailstone(n // 2, r + 1)
    else:
        return hailstone(n * 3 + 1, r + 1)

print(hailstone(10))


# Midterm Review

# Q3 Call expressions
from operator import add
def double(x):
    return x + x

def square(y):
    return y * y

def f(z):
    add(square(double(z)), 1)

print(f(4))
# >>>
# 65 -- wrong!! did not return anything.
# Nothing

def foo(x, y):
    print("x or y")
    return x or y

a = foo
# >>> Nothing (a is function, but python won't show it)

# b = foo()
# >>> Error (foo calls two parameters)

c = a(print("x"), print("y"))
# >>>
# x    # analyze the end frame first
# y
# x or y

print(c)
# None

def welcome():
    print('welcome to')
    return 'hello'

def cs61a():
    print('cs61a')
    return 'world'

print(welcome(), cs61a())
# >>>
# welcome to
# cs61a
# hello world


# Higher order functions
print('-------------\n')
# Q4 I heard you liked functions....(orginal in lab02, extra)
def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def f(n):
        def g(x):
            i = 0
            while i < n:
                if i % 3 == 0:
                    x = f1(x)
                elif i % 3 == 1:
                    x = f2(x)
                elif i % 3 == 2:
                    x = f3(x)
                i += 1
            return x
        return g
    return f
