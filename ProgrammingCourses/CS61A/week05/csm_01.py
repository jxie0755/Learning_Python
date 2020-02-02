"""CS61A CSM01: Tree Recursion and Data Abstraction"""

# Recursion
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


# Tree Recursion
# Q1
# Mario needs to jump over a series of Piranha plants, represented as a string of 0's and 1's.
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
if __name__ == "__main__":
    for i in range(0, 33):
        if make_change(i) != make_change_2(i):
            print("Whoops!")
    print("done")


# Data Abstraction
# Q1
# The following is an Abstract Data Type (ADT) for elephants.
# Each elephant keeps track of its name, age, and whether or not it can fly.
# Given our provided constructor, fill out the selectors

def elephant(name, age, can_fly):
    """
    Takes in a string name, an int age, and a boolean can_fly.
    Constructs an elephant with these attributes.
    >>> dumbo = elephant("Dumbo", 10, True)
    >>> elephant_name(dumbo)
    "Dumbo"
    >>> elephant_age(dumbo)
    10
    >>> elephant_can_fly(dumbo)
    True
    """
    return [name, age, can_fly]


def elephant_name(e):
    return elephant[0]

def elephant_age(e):
    return elephant[1]

def elephant_can_fly(e):
    return elephant[2]

# Q2
# What's wrong?
def elephant_roster(elephants):
    """
    Takes in a list of elephants and returns a list of their
    names.
    """
    # return [elephant[0] for elephant in elephants]  # break abstraction barrier
    return [elephant_name(elephant) for elephant in elephants]

# Q3
def elephant(name, age, can_fly):
    return[[name, age], can_fly]

def elephant_name(e):
    return e[0][0]
def elephant_age(e):
    return e[0][1]
def elephant_can_fly(e):
    return e[1]

# Q4
# How can we write the fixed elephant_roster function for the constructors and
# selectors in the previous question?
def elephant_roster(elephants):
    return [elephant_name(elephant) for elephant in elephants]

# Q5 (optional)
def elephant(name, age, can_fly):
    """
    >>> chris = elephant("Chris Martin", 38, False)
    >>> elephant_name(chris)
    "Chris Martin"
    >>> elephant_age(chris)
    38
    >>> elephant_can_fly(chris)
    False
    """
    def select(command):
        command_dict = {"name":name, "age":age, "can_fly":can_fly}
        return command_dict[command]

    return select


def elephant_name(e):
    return e("name")

def elephant_age(e):
    return e("age")

def elephant_can_fly(e):
    return e("can_fly")
