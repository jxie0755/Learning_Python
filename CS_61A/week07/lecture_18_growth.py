"""CS61A Lecture 18 Growth"""


def fib(n):
    """The nth Fibonacci number.

    >>> fib(20)
    6765
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

# Time

def count(f):
    """Return a counted version of f with a call_count attribute."""
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

# if __name__ == "__main__":
#     fib = count(fib)  # Must use the same name
#     print(fib(20))        # >>> 6765
#     print(fib.call_count) # >>> 21891

# Memoization

def memo(f):
    """Memoize f."""
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

if __name__ == "__main__":
    fib = count(fib)
    counted_fib = fib
    fib = memo(fib)
    fib = count(fib)
    print(fib(20))        # >>> 6765
    print(fib.call_count) # >>> 39 (some from cache dict some from direct call, therefore more called)
    print(counted_fib.call_count) # >>> 21 (from 20 to 0, total of 21 times)

# Space

def count_frames(f):
    """Return a counted version of f with a max_count attribute.
    """
    def counted(n):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(n)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted

if __name__ == "__main__":
    def fib(n):
        if n == 0 or n == 1:
            return n
        else:
            return fib(n-2) + fib(n-1)
    fib = count_frames(fib)
    print(fib(20))        # >>> 6765
    print(fib.open_count) # >>> 0
    print(fib.max_count)  # >>> 20
    print(fib(25))        # >>> 75025
    print(fib.max_count)  # >>> 25       # Longest chain of the tree



# Order of growth

from math import sqrt


def divides(k, n):
    """Return whether k evenly divides n."""
    return n % k == 0

# Time O(n), space O(1)
def factors(n):
    """Count the positive integers that evenly divide n."""
    total = 0
    for k in range(1, n+1):
        if divides(k, n):
            total += 1
    return total

# Time O(n^1/2), space O(1)
def factors_fast(n):
    """Count the positive integers that evenly divide n.

    >>> factors_fast(576)
    21
    """
    sqrt_n = sqrt(n)
    k, total = 1, 0
    while k < sqrt_n:
        if divides(k, n):
            total += 2
        k += 1
    if k * k == n:
        total += 1
    return total

if __name__ == "__main__":
    divides = count(divides)
    print(factors(576))       # >>> 21
    print(divides.call_count) # >>> 576  # O(1)

    divides = count(divides)
    print(factors_fast(576))       # >>> 21
    print(divides.call_count)      # >>> 23  # O(n^1/2)


# Exponentiation

# time O(n), space O(n)
def exp(b, n):
    """Return b to the n.

    >>> exp(2, 10)
    1024
    """
    if n == 0:
        return 1
    else:
        return b * exp(b, n-1)

def square(x):
    return x*x

# O(log(n), space O(log(n))
def exp_fast(b, n):
    """Return b to the n.

    >>> exp_fast(2, 10)
    1024
    """
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(exp_fast(b, n//2))  # this saves time (use n^b = n^1/2b^2)
    else:
        return b * exp_fast(b, n-1)


# Overlap

def overlap(a, b):
    """Count the number of items that appear in both a and b.

    >>> overlap([1, 3, 2, 2, 5, 1], [5, 4, 2])
    3
    """
    count = 0
    for item in a:
        if item in b:
            count += 1
    return count
