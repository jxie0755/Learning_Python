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

print(sum_largest(2018, 2))
