# CS61A Lecture 17 Representation


def str_repr_demos():
    from fractions import Fraction
    half = Fraction(1, 2)
    half
    print(half)    # >>> 1/2
    str(half)      # >>> '1/2'
    repr(half)     # >>> 'Fraction(1, 2)""

    s = 'hello world'
    str(s)               # >>> 'hello world'
    repr(s)              # >>> "'hellow world'"
    "'hello world'"      # >>> ""'hello world'""
    repr(repr(repr(s)))  # >>> '\'"\\\'hello world\\\'"\''
    eval(eval(eval(repr(repr(repr(s)))))) # >>> 'hello world'
    # Errors: eval('hello world')


# Implementing generic string functions

class Bear:
    """A Bear."""
    def __init__(self):
        self.__repr__ = lambda: 'oski'
        self.__str__ = lambda: 'this bear'

    def __repr__(self):
        return 'Bear()'

    def __str__(self):
        return 'a bear'

def print_bear():
    oski = Bear()
    print(oski)             # a bear    # link to str, use class str method
    print(str(oski))        # a bear    # link to str, use calss str method
    print(repr(oski))       # Bear()    # this use class repr method
    print(oski.__repr__())  # this bear # this use instance repr method
    print(oski.__str__())   # oski      # link to str, use instance str method


# The real duplicate of python repr()
# first get x's class, and use class method on x.
def repr(x):
    return type(x).__repr__(x)

# Same idea
def str(x):
    t = type(x)
    if hasattr(t, '__str__'):
        return t.__str__(x)
    else:
        return repr(x)



# Ratio numbers
from fractions import gcd

class Ratio:
    """A mutable ratio.

    >>> f = Ratio(9, 15)
    >>> f
    Ratio(9, 15)
    >>> print(f)
    9/15

    >>> Ratio(1, 3) + Ratio(1, 6)
    Ratio(1, 2)
    >>> f + 1
    Ratio(8, 5)
    >>> 1 + f
    Ratio(8, 5)
    >>> 1.4 + f
    2.0
    """
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)

    def __add__(self, other):
        if isinstance(other, Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        elif isinstance(other, int):  # 预防 ratio + int
            n = self.numer + self.denom * other
            d = self.denom
        else:
            return float(self) + other
        g = gcd(n, d)
        r = Ratio(n // g, d // g)
        return r

    __radd__ = __add__

    def __float__(self):
        return self.numer / self.denom
