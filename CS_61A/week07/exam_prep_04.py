# CS61A Exam Prep 04: List Mutation, Dictionaries, & More Trees



# List
# Q1 Lots of lists

a = [1, 2, 3, 4, 5]
a.pop(3)
b = a[:]
print('a', a)
# >>> [1, 2, 3, 5]
print('b', b)
# >>> [1, 2, 3, 5]

a[1] = b
print('a', a)
# >>> [1, [1, 2, 3, 5], 3, 5]
print('b', b) # b is a copy of a as a new object, won't be affected
# >>> [1, 2, 3, 5]

b[0] = a[:]
print('b', b)
# >>> [[1, [1, 2, 3, 5], 3, 5], 2, 3, 5]

b.pop()
b.remove(2)
print('b', b)
# [[1, [1, 2, 3, 5], 3, 5], 3]

c = [].append(b[1])
print('c', c)
# >>> None


a.insert(b.pop(1), a[-3:4:3])
print('a', a)
# >>> [1, [[1, [1, 2, 3, 5], 3, 5], 3], 3, 5]


# Trees
# Q1 Tree Recursion with trees

def about_equal(t1, t2):
    """Returns whether two trees are 'about equal.'
    Two trees are about equal if and only if they contain
    the same labels the same number of times.
    >> x = tree(1, [tree(2), tree(2), tree(3)])
    >> y = tree(3, [tree(2), tree(1), tree(2)])
    >> about_equal(x, y)
    True
    >> z = tree(3, [tree(2), tree(1), tree(2), tree(3)])
    >> about_equal(x, z)
    False
    """
    def label_counts(t):
        if _________________:
            return _________________
    else:
        counts = _________________
        for b in branches(t) + _________________:
            for label, count in _________________:
                if _________________:
                    counts[_________________] = 0
                counts[___________] += _____________
        return counts
    return _________________

