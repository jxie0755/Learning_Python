# CS61A spring 2018 midterm exam 1

# --------------------------------------------------------------------
# Q1 Frame of Thrones
# --------------------------------------------------------------------
from operator import add, sub
def winterfell(a, b):
    a
    b
    return b(a+1, b(a))

da, ny = 20, 18

while da > ny:
    da = ny
    da, ny = ny + 1, da + 3

def tar(gar, yen):
    if print(yen):
        print(yen + 1)
    return gar(yen)

def st(ar, k=None):
    return lambda a, y: ar(y, a)

night = st(sub)
king = st(st(pow))

def jon(sn, ow):
    print(ow)
    jon = sn(ow)
    print(ow)
    return jon

def snow(ow):
    def tarly(snow):
        return ow + snow
    ow += 2
    return tarly

# What would python show:
print((print(2) or 3) // (0 or 1))
# >>>
# 2
# 3
print(winterfell(2, print))
# >>>
# 2
# 3 None
# None
print(ny)
# >>>
# 21
print(tar(lambda x: x-7, 8))
# >>>
# 8 (from if condition)
# 1
print(night(king(2, 3), 4))
# >>>
# -4
print(jon(snow(5), 2))
# >>>
# 2
# 2
# 9


# --------------------------------------------------------------------
# Q2 Stranger Frames
# --------------------------------------------------------------------
def lucas(mike):
    return will

def dustin(lucas):
    will = 1
    def dustin(mike):
        will = 2
        return lucas
    return lambda mad: dustin(3)(will)

will = 5 + 6
lucas = dustin(lucas)
print(lucas(max))
# >>>
# 11
# lucas global is a fucntion dustin(lucase) which is lambda(mad) return dustin(3)(will)

# so lucase(max), which max is mad, is to return dustin(3)(will)

# dustin(3) is in the second frame, which return lucas, which is a global function lucase(mike) to return will no matter what mike is. in this case, mike=3, but it does not matter

# eventually it will just return will, which is 11.


# --------------------------------------------------------------------
# Q3 Choose Wisely
# --------------------------------------------------------------------

# a
def sum_some(n, p):
    """Return the sum of the digits of N for which P returns a true value.
    >>> even = lambda d: d % 2 == 0
    >>> big = lambda d: d > 5
    >>> sum_some(124567, even) # Sum the even digits: 2 + 4 + 6
    12
    >>> sum_some(124567, big) # Sum the big digits: 6 + 7
    13
    """
    total = 0
    while n != 0:
        if p(n%10):
            total += n%10
        n = n // 10
    return total

# b
def sum_largest(n, k):
    """Return the sum of the K largest digits of N.
    >>> sum_largest(2018, 2) # 2 and 8 are the two largest digits (larger than 0 and 1).
    10
    >>> sum_largest(12345, 10) # There are only five digits, so all are included in the sum.
    15
    """
    if k == 0 or n == 0:
        return 0
    a = n % 10 + sum_largest(n//10, k - 1)
    b = sum_largest(n // 10, k)
    print(a, b)
    return max(a, b)

# c
X = (lambda a, x: x + (lambda y: lambda z: y+z+1000)(1000)(10))(5, (lambda: 8)())
print('X is', X)


# --------------------------------------------------------------------
# Q4 Editor
# --------------------------------------------------------------------
