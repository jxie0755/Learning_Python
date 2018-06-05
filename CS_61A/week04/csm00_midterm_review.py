# CSM00 Mideterm 1 Review

# Q1
apple = 4
def orange(apple):
    apple = 5
    def plum(x):
        return lambda plum: plum * 2
    return plum

print(orange(apple)("hiii")(4))
# >>> 8


# Q2
def bar(f):
    def g(x):
        return f(x-1)
    return g
f = 4
print(bar(lambda x: x + f)(2))
# >>> 5


# Q3
inception = lambda secret: lambda: secret
print(inception(5)())
# >>> 5


# High order function
def mystery(f, x):
    """
    >>> from operator import add, mul
    >>> a = mystery(add, 3)
    >>> a(4) # add(3, 4)
    7
    >>> a(12)
    15
    >>> b = mystery(mul, 5)
    >>> b(7) # mul(5, 7)
    35
    >>> b(1)
    5
    >>> c = mystery(lambda x, y: x * x + y, 4)
    >>> c(5)
    21
    >>> c(7)
    23
    """

    def g(y):
        return f(x, y)
    return g

    # on-liner
    return lambda y: f(x, y)


# What would python display:
square = lambda x: x**2
foo = mystery(lambda a, b: a(b), lambda c: 5 + square(c))
print(foo(-2))
# >>> 9


# cannot use for or while loop.
# use recursion in repeat
# cannot use string operation except '+' operation
def fox_says(start, middle, end, num):
    """
    >>> fox_says('wa', 'pa', 'pow', 3)
    'wa-pa-pa-pa-pow'
    >>> fox_says('fraka', 'kaka', 'kow', 4)
    'fraka-kaka-kaka-kaka-kaka-kow'
    """
    def repeat(k):