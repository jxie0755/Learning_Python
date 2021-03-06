"""CS61A Exam Prep 02: Recursion & Lamda Functions"""

# Express yourself
def kbonacci(n, k):
    """Return element N of a K-bonacci sequence.
    >>> kbonacci(3, 4)
    1
    >>> kbonacci(9, 4)
    29
    >>> kbonacci(4, 2)
    3
    >>> kbonacci(8, 2)
    21
    """
    if n < k - 1:
        return 0
    elif n == k - 1:
        return 1
    else:
        total = 0
        i = n - k
        while i < n:
            total = total + kbonacci(i, k)
            i = i + 1
    return total

    # Non recursion version
    # if n < k - 1:
    #     return 0
    # elif n == k - 1:
    #     return 1
    # else:
    #     result = [0] * (k - 1) + [1]
    #     for i in range(0, n-k+1):
    #         temp = sum([result[x] for x in range(-1*k, 0)])
    #         result.append(temp)
    #     return result[-1]




# Combine Reverse and Remove
def combine(left, right):
    """Return all of LEFT"s digits followed by all of RIGHT"s digits."""
    factor = 1
    while factor <= right:
        factor = factor * 10
    return left * factor + right

def reverse(n):
    """Return the digits of N in reverse.
    >>> reverse(122543)
    345221
    """
    if n < 10:
        return n
    else:
        return combine(n % 10, reverse(n // 10))


def remove(n, digit):
    """Return all digits of N that are not DIGIT, for DIGIT less than 10.
    >>> remove(243132, 3)
    2412
    >>> remove(remove(243132, 1), 2)
    433
    """
    # removed = 0
    # while n != 0:
    #     sample, n = n % 10, n // 10
    #     if sample != digit:
    #         removed = removed * 10 +  sample
    # return reverse(removed)

    # optional and better:
    removed = 0
    while n != 0:
        sample, n = n % 10, n // 10
        if sample != digit:
            removed = combine(sample, removed)  # use combine to reverse on the run
    return removed  # then no need to reverse the whole thing again


# You complete Me
# (a)
square = lambda x: x * x
double = lambda x: 2 * x
def memory(x, f):
    """Return a higher-order function that prints its
    memories.
    >>> f = memory(3, lambda x: x)
    >>> f = f(square)
    3
    >>> f = f(double)
    9
    >>> f = f(print)
    6
    >>> f = f(square)
    3
    None
    """
    def g(h):
        print(f(x))
        return memory(x, h)
    return g

# # (b)
# Add parentheses and single-digit integers in the blanks below so that the expression on the second line evaluates to 2015
lamb = lambda lamb: lambda: lamb + lamb
X = lamb(1000)() + (lambda b, c: b() * b() - c)(lamb(2), 1)
assert(X == 2015)


# Frog goes Croak
def mouse(n):
    if n >= 10:
        squeak = n // 100
        n = frog(squeak) + n % 10
    return n

def frog(croak):
    if croak == 0:
        return 1
    else:
        return 10 * mouse(croak + 1)

print(mouse(357))
# >>> 47


# If (s)he can wield the Hammer...
# # what would python show:

from operator import add
avengers = 6

def vision(avengers):
    print(avengers)
    return avengers + 1

def hawkeye(thor, hulk):
    love = lambda black_widow: add(black_widow, hulk)
    return thor(love)

def hammer(worthy, stone):
    if worthy(stone) < stone:
        return stone
    elif worthy(stone) > stone:
        return -stone
    return 0

capt = lambda iron_man: iron_man(avengers)

print(capt(vision))
