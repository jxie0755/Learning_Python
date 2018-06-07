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
    """Return all of LEFT's digits followed by all of RIGHT's digits."""
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
        return combine(n % 10 , reverse(n // 10))


def remove(n, digit):
    """Return all digits of N that are not DIGIT, for DIGIT less than 10.
    >>> remove(243132, 3)
    2412
    >>> remove(remove(243132, 1), 2)
    433
    """
    removed = 0
    while n != 0:
        sample, n = n % 10, n // 10
        if sample != digit:
            removed = combine(sample, removed)
    return reverse(removed)
