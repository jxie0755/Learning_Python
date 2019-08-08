"""CS61A Lecture 05 Environments"""

# Functional arguments

# A high order function
def apply_twice(f, x):
    """Return f(f(x))

    >>> apply_twice(square, 2)
    16
    >>> from math import sqrt
    >>> apply_twice(sqrt, 16)
    2.0
    """
    return f(f(x))

def square(x):
    return x * x

result = apply_twice(square, 2)
print(result)  # >>> 16


# Another example
def repeat(f, x):
    while f(x) != x:
        x = f(x)
    return x

def g(y):
    return (y + 5) // 3

print(repeat(g, 5))
# >>> 2

# Nested Definition in a function

def make_adder(n):
    """Return a function that takes one argument k and returns k + n.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

# Lexical scope and returning functions

def f(x, y):
    return g(x)

def g(a):
    return a + y

# This expression causes an error because y is not bound in g.
# f(1, 2)
# when f is called, return g, g's parent frame is global not f
# Only nested function will have the parent relationships



# Composition

def compose1(f, g):
    """Return a function that composes f and g.

    f, g -- functions of a single argument
    """
    def h(x):
        return f(g(x))
    return h

def triple(x):
    return 3 * x

squiple = compose1(square, triple)
print(squiple(5))  # >>> (5*3)**2 -- 225

tripare = compose1(triple, square)
print(tripare(5))  # >>> (5**2)*3 -- 75

squadder = compose1(square, make_adder(2))
print(squadder(5))  # >>> (5+2)**2 -- 49

# Self Reference

def print_all(k):
    """Print all arguments of repeated calls.

    >>> f = print_all(1)(2)(3)(4)(5)
    1
    2
    3
    4
    5
    """
    print(k)
    return print_all

def print_sums(n):
    """Print all sums of arguments of repeated calls."""
    print(n)
    def next_sum(k):
        return print_sums(n+k)
    return next_sum

print_sums(1)(2)(3)(4)(5)
# >>>
# 1
# 3
# 6
# 10
# 15
