# CS61A Discusion 02 Environment DIagrams & Recursion

from operator import add
six = 1
def ty(one, a):
    fall = one(a, six)
    return fall

six = ty(add, 6)
# >>> 7

fall = ty(add, 6)
# >>> 13

def curry2(h):
    def f(x):
        def g(y):
            return h(x, y)
        return g
    return f

make_adder = curry2(lambda x, y: x + y)
# >>> fucntion

add_three = make_adder(3)
# >>> function

five = add_three(2)
# >>> 5

n = 7
def f(x):
    n = 8
    return x + 1

def g(x):
    n = 9
    def h():
        return x + 1
    return h

def f(f, x):
    return f(x + n)

f = f(g, n)
# >>> function

g = (lambda y: y())(f)
# >>> 15

y = "y"
h = y
def y(y):
    h = "h"
    if y == h:
        return y + "i"
    y = lambda y: y(h)
    return lambda h: y(h)

y = y(y)(y)
# >>> hi


# Recursion
def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    else:
        return m + multiply(m, n - 1)

def countdown(n):
    """
    >>> countdown(3)
    3
    2
    1
    """
    if n <= 0:
        return
    print(n)
    countdown(n - 1)

def sum_digits(n):
    """
    >>> sum_digits(7)
    7
    >>> sum_digits(30)
    3
    >>> sum_digits(228)
    12
    """
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)
