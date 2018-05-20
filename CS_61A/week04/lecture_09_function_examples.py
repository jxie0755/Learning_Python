# CS61A Lecture 09 Function examples
# Test-driven development


# 仍然是递归法的思路来解决问题,思路还是辗转相除法,只是用减法来实现,步数更多
def gcd(m, n):
    """Return the largest k that evenly divides both m and n.

    k, m, and n are all positive integers.

    >>> gcd(12, 8)
    4
    >>> gcd(16, 12)
    4
    >>> gcd(16, 8)
    8
    >>> gcd(2, 16)
    2
    >>> gcd(24, 42)
    6
    >>> gcd(5, 5)
    5
    >>> gcd(0, 0)
    0
    """
    if m == n:
        return m
    elif m < n:
        return gcd(n, m)
    else:
        return gcd(m-n, n)


# Decorators

def trace1(fn):
    """Return a function equivalent to fn that also prints trace output.

    fn -- a function of one argument.
    """
    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return traced

@trace1
def square(x):
    return x*x

print(square(5))
# >>>
# Calling <function square at 0x00000203F0989158> on argument 5
# 25

@trace1
def sum_squares_up_to(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + square(k), k + 1
    return total

print(sum_squares_up_to(5))
# >>>
# Calling <function sum_squares_up_to at 0x000001BECBE292F0> on argument 5
# Calling <function square at 0x000001BECBE29158> on argument 1
# Calling <function square at 0x000001BECBE29158> on argument 2
# Calling <function square at 0x000001BECBE29158> on argument 3
# Calling <function square at 0x000001BECBE29158> on argument 4
# Calling <function square at 0x000001BECBE29158> on argument 5
