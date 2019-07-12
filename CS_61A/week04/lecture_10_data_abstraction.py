# CS61A Lecture 10 Data Abstraction

# Rational arithmetic

def add_rational(x, y):
    """The sum of rational numbers X and Y."""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    """The product of rational numbers X and Y."""
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def rationals_are_equal(x, y):
    """True iff rational numbers X and Y are equal."""
    return numer(x) * denom(y) == numer(y) * denom(x)

def print_rational(x):
    """Print rational X."""
    print(numer(x), "/", denom(x))


# Using Pairs
pair = [1, 2] # python built-in type as list
x, y = pair # unpack the list
print(x) # >>> 1
print(y) # >>> 2

# also work with operator module getitem
from operator import getitem
print(getitem(pair, 0)) # >>> 1

# Constructor and selectors

def rational(n, d):
    """A representation of the rational number N/D."""
    return [n, d]

def numer(x):
    """Return the numerator of rational number X."""
    return x[0]

def denom(x):
    """Return the denominator of rational number X."""
    return x[1]

# Improved specification

from fractions import gcd
def rational(n, d):
    """A representation of the rational number N/D."""
    g = gcd(n, d)
    return [n//g, d//g]

def numer(x):
    """Return the numerator of rational number X in lowest terms and having
    the sign of X."""
    return x[0]

def denom(x):
    """Return the denominator of rational number X in lowest terms and positive."""
    return x[1]

# Functional implementation

def rational(n, d):
    """A representation of the rational number N/D."""
    g = gcd(n, d)
    n, d = n//g, d//g
    def select(name):
        if name == "n":
            return n
        elif name == "d":
            return d
    return select
# in this way, the rational number becomes a function instead of a two-element list
# but this won't affect any of the programs outside of the abtraction barrier.

def numer(x):
    """Return the numerator of rational number X in lowest terms and having
    the sign of X."""
    return x("n")

def denom(x):
    """Return the denominator of rational number X in lowest terms and positive."""
    return x("d")
