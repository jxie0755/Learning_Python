# CSM01 Tree Recursion and Data Abstraction

# Q1
# Write a function is_sorted that takes in an integer n and returns true if the digits of that number are increasing from right to left.

def is_sorted(n):
    """
    >>> is_sorted(2)
    True
    >>> is_sorted(22222)
    True
    >>> is_sorted(9876543210)
    True
    >>> is_sorted(9087654321)
    False
    """
    # result = []
    # while n > 0:
    #     result.append(n % 10)
    #     n = n // 10

    # check, is_sort = result[0], True
    # for i in result:
    #     if i >= check:
    #         check = i
    #     else:
    #         is_sort = False
    # return is_sort

    # recursion way
    right_digit, rest = n % 10, n // 10
    if rest == 0:
        return True
    elif right_digit > rest % 10:
        return False
    else:
        return is_sorted(rest)


# Q2
# Mario needs to jump over a series of Piranha plants, represented as a string of 0’s and 1’s.
# Mario only moves forward and can either step (move forward one space) or jump (move forward two spaces) from each position.
# How many different ways can Mario traverse a level without stepping or jumping into a Piranha plant?

def mario_number(level):
    """
    Return the number of ways that Mario can traverse the
    level, where Mario can either hop by one digit or two
    digits each turn. A level is defined as being an integer
    with digits where a 1 is something Mario can step on and 0
    is
    something Mario cannot step on.
    >>> mario_number(10101)
    1
    >>> mario_number(11101)
    2
    >>> mario_number(100101)
    0
    """
    if level == 1:
        return 1
    elif level % 10 == 0:
        return 0
    else:
        return mario_number(level//10) + mario_number(level//100)


# Q3

def make_change(n):
    """Write a function, make_change that takes in an integer amount, n, and returns the minimum number of coins we can use to make change for that n, using 1-cent, 3-cent, and 4-cent coins.
    Look at the doctests for more examples.
    >>> make_change(5)
    2
    >>> make_change(6) # tricky! Not 4 + 1 + 1 but 3 + 3
    2
    """
    # if n == 0:
    #     return 0
    # elif n <= 2:
    #     return 1 + make_change(n-1)
    # elif n == 3 or n == 6 or n == 9:
    #     return 1 + make_change(n-3)
    # else:
    #     return 1 + make_change(n-4)

    if n == 0:
        return 0
    elif n < 3:
        return 1 + make_change(n - 1) # (return n) is also fine
    elif n < 4:
        return 1 + make_change(n - 3)
    else:
        use_3 = 1 + make_change(n - 3)
        use_4 = 1 + make_change(n - 4)
        return min(use_3, use_4)

# my own version (simpler but not as clear)
# but mathmatically should be right
def make_change_2(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1 + make_change(n-1)
    elif n == 3 or n == 6 or n == 9:
        return 1 + make_change(n-3)
    else:
        return 1 + make_change(n-4)

# 通用方式
def make_change_x(n, a, b):
    """n为需要找的钱, ab分别为两个面值, 且1<a<b
    需要返回最少找几张钱

    注意: 手上必有1块的面值, 为确保能找得开
    """
    # your code:
    if n == 0:
        return 0
    elif n < a:
        return 1 + make_change(n-1, a, b)
    elif n < b:
        return 1 + make_change(n-a, a, b)
    else:
        use_a = 1 + make_change(n-a, a, b)
        use_b = 1 + make_change(n-b, a, b)
        return min(use_a, use_b)

# test unit
if __name__ == '__main__':
    for i in range(0, 33):
        if make_change(i) != make_change_2(i):
            print('Whoops!')
    print('done')