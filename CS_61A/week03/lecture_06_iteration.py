# CS61A Lecture 06 Iteration


# A fibonacci Sequence using while loop
def fib(n):
    k, kth, difference = 0, 0, 1
    while k < n:
        kth, difference = kth + difference, kth
        k += 1
    return kth

if __name__ == '__main__':
    assert fib(0) == 0, 'regular'
    assert fib(8) == 21, '8th'


# Return
def end(n, d):
    """Print the final digits of N in reverse order until D is found.

    >>> end(34567, 5)
    7
    6
    5
    """
    while n > 0:
        last, n = n % 10, n // 10
        print(last)
        if d == last:
            return None

def search(f):
    """Return the smallest non-negative integer x for which f(x) is a true value."""
    x = 0
    while not f(x):
        x += 1
    return x

def is_three(x):
    return x == 3

def square(x):
    return x * x

def positive(x):
    return max(0, square(x) - 100)

def inverse(f):
    """Return g(y) such that g(f(x)) -> x."""
    return lambda y: search(lambda x: f(x) == y)


if __name__ == '__main__':
    print(search(is_three)) # >>> 3
    print(search(positive)) # >>> 11, as 11^2 = 121 - 100 = 21 as the first positive value
    sqrt = inverse(square)
    print(square(16)) # >>> 256
    print(sqrt(256)) # >>> 16


# Self reference
def print_all(x):
    print(x)
    return print_all

def print_sum(x):
    print(x)
    def next_sum(y):
        return print_sum(x+y)
    return next_sum


if __name__ == '__main__':
    print_all(1)(3)(5)   # keep adding argument as it return a function of itself
    # >>>
    # 1
    # 3
    # 5

    print_sum(1)(3)(5)
    # >>>
    # 1
    # 4
    # 9



