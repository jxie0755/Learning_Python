# Colin's notes on recursion

def stairs(n):
    """Give the number of ways to take n steps, given that at each step, you can choose to take 1, 2
    >>> stairs(2)
    2
    >>> stairs(4)
    5
    >>> stairs(1)
    1
    >>> stairs(3)
    3
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return stairs(n-1) + stairs(n-2)

def kstairs(n, k):
    """Give the number of ways to take n steps, given that at each step, you can choose to take 1,2,3,k-2,k-1 or k steps,
    >>> kstairs(5, 2)
    8
    >>> kstairs(5, 5)
    16
    >>> kstairs(10, 5)
    464
    """
    if n == 0:
        return 0
    if n <= k:
        return 2**(n-1)
    return sum([kstairs(n - i, k) for i in range(1, k + 1)])

def permutations(lst):
    """List all permutations of the given list
    enumerate() function might be helpful
    >>> permutations(['angie', 'cat'])
    [['angie', 'cat'], ['cat', 'angie']]
    >>> permutations([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    pass
