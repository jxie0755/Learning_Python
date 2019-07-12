# CS61A CSM 03: Mutation and Nonlocal

# Mutation
# Q1 What would python display?

a = [1, 2]
a.append([3, 4])
print(a)
# >>> [1, 2, [3, 4]]

b = list(a)
a[0] = 5  # [5, 2, [3, 4]]
a[2][0] = 6 # [5, 2, [6, 4]]
print(b)
# >>> [1, 2, [6, 4]]
# Pay attention: modification of item inside the list will change b because it is a pointer.

a.extend([7])
a += [8] # [5, 2, [6, 4], 8]
# a += 9  # error
print(a)
# >>> [5, 2, [6, 4], 8]
print(b)
# >>> [1, 2, [6, 4]]

# Challenge:
b[2][1] = a[2:]
# [1, 2, [6, [[[6, 4], 8]]]]

print(a[2][1][0][0])
# >>> 6

# Q2

a = [1, 2, [3]]
def mystery(s, t):
    s.pop(1)
    t.append(s)
    print(t)

b = a
a += [b[0]]
# a = [1, 2, [3], 1], b same
print(a == b)

mystery(b, a[1:]) # a slice is a new list
# b = [1, 2, [3], 1]
# a[1:] = [2, [3], 1]

# s.pop(1) -- b = [1, [3], 1], same as a

# >>>[2, [3], 1, [1, [3], 1]]


# Q3
# Given some list lst, possibly a deep list, mutate lst to have the accumulated sum of all elements so far in the list. If there is a nested list
#  mutate it to similarly reflect the accumulated sum of all elements so far in the nested list.
# Return the total sum of lst

def accumulate(lst):
    """
    >>> l = [1, 5, 13, 4]
    >>> accumulate(l)
    23
    >>> l
    [1, 6, 19, 23]
    >>> deep_l = [3, 7, [2, 5, 6], 9]
    >>> accumulate(deep_l)
    32
    >>> deep_l
    [3, 10, [2, 7, 13], 32]
    """
    sum_so_far = 0
    for i in range(len(lst)):
        elem = lst[i]
        if isinstance(elem, list):
            inside = accumulate(elem)
            sum_so_far += inside
        else:
            sum_so_far += elem
            lst[i] = sum_so_far
    return sum_so_far


# Non Local
# Q1 Nonlocal Kale

eggplant = 8
def vegetable(kale):
    def eggplant(spinach):
        nonlocal eggplant
        nonlocal kale
        kale = 9
        eggplant = spinach
        print(eggplant, kale)
    eggplant(kale)
    return eggplant

spinach = vegetable("kale")

print(spinach)
# >>>
# kale 9
# when execute eggplant(kale), eggplant = "kale", kale = 9 (changed locally)

# eggplant changed to spinach, which was "kale"
# >>> kale


# Q2 Pingpong again
# The ping-pong sequence counts up starting from 1 and is always either counting up or counting down.
# At element k, the direction switches if k is a multiple of 7 or contains the digit 7.

# The first 30 elements of the ping-pong sequence are listed below,
# with direction swaps marked using brackets at the 7th, 14th, 17th, 21st, 27th, and 28th elements:
# 1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6

# Implement a function make_pingpong_tracker that returns the next value in the pingpong sequence each time it is called.
#  You may use assignment statements

def has_seven(k): # Use this function for your answer below
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def make_pingpong_tracker():
    """ Returns a function that returns the next value in the
    pingpong sequence each time it is called.
    >>> output = []
    >>> x = make_pingpong_tracker()
    >>> for _ in range(9):
    ...    output += [x()]
    >>> output
    [1, 2, 3, 4, 5, 6, 7, 6, 5]
    """
    index, current, add = 1, 0, True
    def pingpong_tracker():
        nonlocal index, current, add
        if add:
            current = current + 1
        else:
            current = current - 1
        if has_seven(current) or index % 7 == 0:
            add = not add
        index += 1
        return current
    return pingpong_tracker
