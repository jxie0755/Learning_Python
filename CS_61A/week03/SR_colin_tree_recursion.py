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
