# Print

# Python will show value when a value is inputed
# >>> -2
# -2
# >>> print(-2)
# >>>
# -2
#
# 'Go Bears'
print('Go Bears')
print(1, 2, 3)
# >>> None
# won't show because python does not show None value.

print(None)
# >>> will show

x = -2
# >>> x
# -2
x = print(-2)
# >>> x
# None

# Example of print(), a non-pure function
print(print(1), print(2))
# >>>
# 1
# 2
# None, None

# Addition/Multiplication
print(2 + 3 * 4 + 5)
print((2 + 3) * (4 + 5))

# Division
print(618 / 10)
print(618 // 10)
print(618 % 10)
from operator import truediv, floordiv, mod
print(floordiv(618, 10))
print(truediv(618, 10))
print(mod(618, 10))

# Multiple return values
# same as divmod()
def divide_exact(n, d):
    return n // d, n % d
quotient, remainder = divide_exact(618, 10)
print(quotient, remainder)


# Dostrings, doctests, & default arguments
from operator import floordiv, mod
def divide_exact(n, d=10):
    """Return the quotient and remainder of dividing N by D.

    >>> q, r = divide_exact(618, 10)
    >>> q
    61
    >>> r
    8
    """
    return floordiv(n, d), mod(n, d)

# use command (in the directory of this file):
# python3 -m doctest lecture_03_control.py
# it may bypass the test result output if pass.

# python3 -m doctest -v lecture_03_control.py
# add "-v" will show the actual test case and result


# Conditional expressions
def absolute_value(x):
    """Return the absolute value of X.

    >>> absolute_value(-3)
    3
    >>> absolute_value(0)
    0
    >>> absolute_value(3)
    3
    """
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x

# Summation via while
i, total = 0, 0
while i < 3:
    i = i + 1
    total = total + i
print(total)
