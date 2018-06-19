# CS61A Lecture 11 Containers

# Lists

odds = [41, 43, 47, 49]
# print(len(odds)) # >>> 4
# print(odds[1]) # >>> 43
# print(odds[0] - odds[3] + len(odds)) # >>> -4
# print(odds[odds[3]-odds[2]]) # >>> 47

# Containers

digits = [1, 8, 2, 8]
# print(1 in digits) # >>> True
# print('1' in digits) # >>> False
# print([1, 8] in digits) # >>> False
# print([1, 2] in [[1, 2], 3]) # >>> True


# Statement

def count_while(s, value):
    """Count the number of occurrences of value in sequence s.

    >>> count_while(digits, 8)
    2
    """
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total = total + 1
        index = index + 1
    return total

def count_for(s, value):
    """Count the number of occurrences of value in sequence s.

    >>> count_for(digits, 8)
    2
    """
    total = 0
    for elem in s:  # evaluate s first, then bind elem to each element in s
        if elem == value:
            total = total + 1
    return total


def count_same(pairs):
    """Return how many pairs have the same element repeated.

    >>> pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
    >>> count_same(pairs)
    2
    """
    same_count = 0
    for x, y in pairs: # unpacking
        if x == y:
            same_count = same_count + 1
    return same_count

# Ranges

list(range(5, 8))
list(range(4))
len(range(4))

def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total

def cheer():
    for _ in range(3):
        print('Go Bears!')


# List comprehensions

odds = [1, 3, 5, 7, 9]
[x+1 for x in odds]
[x for x in odds if 25 % x == 0]

def divisors(n):
    """Return the integers that evenly divide n.

    >>> divisors(4)
    [1, 2]
    >>> divisors(12)
    [1, 2, 3, 4, 6]
    >>> [n for n in range(1, 1000) if sum(divisors(n)) == n]
    [6, 28, 496]
    """
    return [x for x in range(1, n) if n % x == 0]

# Dicts
# (unordered!)

def dict_demos():
    numerals = {'I': 1, 'V': 5, 'X': 10}
    numerals['X']
    numerals.values()
    list(numerals.values())
    sum(numerals.values())
    dict([(3, 9), (4, 16), (5, 25)])
    numerals.get('X', 0)
    numerals.get('X-ray', 0)  # second parameter as the default value if not in the dict
    {x: x*x for x in range(3,6)}

    {1: 2, 1: 3} # throw out the lower value elements
    {[1]: 2} # unhashable keys not allowed
    {1: [2]}
