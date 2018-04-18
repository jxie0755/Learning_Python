# Exam Prep 01: Higher-Order Functions & Environment
# Q1
# Implement the longest_increasing_suffix function, which returns the longest
# suffix (end) of a positive integer that consists of strictly increasing digits.

def longest_increasing_suffix(n):
    """Return the longest increasing suffix of a positive
    integer n.
    >>> longest_increasing_suffix(63134)
    134
    >>> longest_increasing_suffix(233)
    3
    >>> longest_increasing_suffix(5689)
    5689
    >>> longest_increasing_suffix(568901)
    1
    """
    m, suffix, k = 10, 0, 1
    while n:
        n, last = n // 10, n % 10
        if last < m:
            m, suffix, k = last, suffix + k * last, 10 * k
        else:
            return suffix
    return suffix


# Q2
# A number n contains a sandwich if a digit in n is surrounded by two identical digits.
# For example, the number 242 contains a sandwich because 4 is surrounded by 2 on both sides.
# 1242 also contains a sandwich, while 12532 does not contain a sandwich.
# Implement the sandwich(n) function, which takes in a nonnegative integer n.
# It returns True if n contains a sandwich and False otherwise. If n has fewer than three digits, it cannot contain a sandwich.

def sandwich(n):
    """Return True if n contains a sandwich and False
    otherwise
    >>> sandwich(416263) # 626
    True
    >>> sandwich(5050) # 505 or 050
    True
    >>> sandwich(4441) # 444
    True
    >>> sandwich(1231)
    False
    >>> sandwich(55)
    False
    >>> sandwich(4456)
    False
    """
    tens, ones = n // 10 % 10, n % 10
    n = n // 100
    while n:
        print(n, tens, ones)
        if n % 10 == ones:
            return True
        else:
            tens, ones = n % 10, tens
            n = n // 10
    return False


# Q3
# Digit Fidget (Fa15 Midterm 1 Q3c)
# Implement luhn_sum. The Luhn sum of a non-negative integer n adds the sum of
# each digit in an even position to the sum of doubling each digit in an odd position.

# If doubling an odd digit results in a two-digit number, those two digits are summed to
# form a single digit. You may not use recursive calls or call find_digit in your solution.

def luhn_sum(n):
    """Return the Luhn sum of n.
    >>> luhn_sum(135) # 1 + 6 + 5
    12
    >>> luhn_sum(185) # 1 + (1+6) + 5
    13
    >>> luhn_sum(138743) # From lecture: 2 + 3 + (1+6) + 7 +
    30
    """

    def luhn_digit(digit):
        x = digit * multiplier
        return x // 10 + x % 10

    total, multiplier = 0, 1
    while n:
        n, last = n // 10, n % 10
        total = total + luhn_digit(last)
        multiplier = 3 - multiplier

    return total
