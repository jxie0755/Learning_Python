"""CS61A Discussion 04: Nonlocals & Mutation"""


# Nonlocal

def stepper(num):
    def step():
        nonlocal num
        num = num + 1
        return num
    return step

s = stepper(3)
print(s()) # >>> 4
print(s()) # >>> 5


lamb = "da"
def da(da):
    def lamb(lamb):
        nonlocal da
        def da(nk):
            da = nk + ["da"]
            da.append(nk[0:2])
            return nk.pop()
    da(lamb)
    return da([[1], 2]) + 3

print(da(lambda da: da(lamb)))
# >>>
# 2 + 3 = 5

# Write a function that takes in a value x and updates and prints the result based on input functions

def memory(n):
    """
    >>> f = memory(10)
    >>> f = f(lambda x: x * 2)
    20
    >>> f = f(lambda x: x - 7)
    13
    >>> f = f(lambda x: x > 5)
    True
    """
    def f(fn):
        nonlocal n
        n = fn(n)
        print(n)
        return f
    return f


# Mutable Lists

lst1 = [1,2,3]
lst2 = [1,2,3]
print(lst1 == lst2) # >>> True  (equal)
print(lst1 is lst2) # >>> False (not the same object)

lst2 = lst1
lst1.append(4)
print(lst1) # >>> [1,2,3,4]
print(lst2) # >>> [1,2,3,4]

lst1 = lst1 + [5]  # this is a new list generated, covered the old lst1, therefore a different object

print(lst2)
print(lst1 == lst2) # >>> True  (because lst2 will always = lst1)
print(lst2 is lst1) # >>> False


# Write a function that takes in a value x, a value el, and a list
# and adds as many el's to the end of the list as there are x's.
# Make sure to modify the original list using list mutation techniques.

def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs
    in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    count = 0
    for i in lst:
        if i == x:
            count += 1
    while count != 0:
        lst.append(el)
        count -= 1

# Write a function that takes in a list and reverses it in place,
# i.e. mutate the given list itself, instead of returning a new list

def reverse(lst):
    """ Reverses lst in place.
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse(x)
    >>> x
    [1, 5, 4, 2, 3]
    """
    # for i in range(-1, -len(lst)-1, -1):
    #     lst.append(lst.pop(i))
    # this is risky because it changed the list while iteration
    # but the length remained the same, so it worked,

    # a swapping method is much better
    L = len(lst)
    for i in range(L//2):
        # lst[i], lst[L-i-1] = lst[L-i-1], lst[i]
        lst[i], lst[-i - 1] = lst[-i - 1], lst[i] # better way to index


# Dictionaries


# Write a function that takes in a sequence s and a function fn and returns a dictionary.
# The values of the dictionary are lists of elements from s.
# Each element e in a list should be constructed such that fn(e) is the same for all elements in
# that list.
# Finally, the key for each value should be fn(e).

def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    result = {}
    for i in s:
        if fn(i) not in result:
            result[fn(i)] = [i]
        else:
            result[fn(i)].append(i)
    return result


# Write a function that takes in a deep dictionary d and replace all occurences of x as a value (not a key) with y.
# Hint: You will need to combine iteration and recursion.
# Also, for a dictionary z, type(z) == dict will evaluate to True.

def replace_all_deep(d, x, y):
    """
    >>> d = {1: {2: "x", "x": 4}, 2: {4: 4, 5: "x"}}
    >>> replace_all_deep(d, "x", "y")
    >>> d
    {1: {2: "y", "x": 4}, 2: {4: 4, 5: "y"}}
    """
    for k, v in d.items():
        if type(v) == dict:
            replace_all_deep(v, x, y)
        else:
            if v == x:
                d[k] = y
