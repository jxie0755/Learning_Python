"""
Mobile balance from CS61a week05 HW05
A similar structure as tree that use tree as a structure
See the OOP setup in class_tree.py
"""

def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    return tree("mobile", [left, right])

def is_mobile(m):
    return is_tree(m) and label(m) == "mobile"

def sides(m):
    """Select the sides of a mobile."""
    assert is_mobile(m), "must call sides on a mobile"
    return branches(m)

def is_side(m):
    return not is_mobile(m) and not is_weight(m) and type(label(m)) == int

def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    return tree(length, [mobile_or_weight])

def length(s):
    """Select the length of a side."""
    assert is_side(s), "must call length on a side"
    return label(s)

def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    assert is_side(s), "must call end on a side"
    return branches(s)[0]


# Q3 Weights
def weight(size):
    """Construct a weight of some size."""
    assert size > 0
    "*** YOUR CODE HERE ***"
    return tree("weight", [tree(size)])

def size(w):
    """Select the size of a weight."""
    "*** YOUR CODE HERE ***"
    assert is_weight(w)
    return label(branches(w)[0])

def is_weight(w):
    """Whether w is a weight, not a mobile."""
    "*** YOUR CODE HERE ***"
    return is_tree(w) and label(w) == "weight"

def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a weight or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_weight(m):
        return size(m)
    else:
        assert is_mobile(m), "must get total weight of a mobile or a weight"
        return sum([total_weight(end(s)) for s in sides(m)])

def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    "*** YOUR CODE HERE ***"
    if is_mobile(m):
        L, R = sides(m)[0], sides(m)[1]
        M_balance = length(L)* total_weight(end(L)) == length(R)* total_weight(end(R))  # 如果m是一个mobile,必须先要保证mobile两边是平衡的
        L_balance = balanced(end(L))  # 如果mobile的一边接的还是mobile, 必须保证它也是平衡的
        R_balance = balanced(end(R))  # 同上
        return M_balance and L_balance and R_balance

    else:
        return True  # 除非mobile的一边接得是weight,那就不必往下检查

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
