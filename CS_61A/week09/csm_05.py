"""CS61A CSM 05: Linked Lists and Midterm Review"""



# Linked list

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.second
    3
    >>> s.first = 5
    >>> s.second = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value


    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ", " + repr(self.rest)
        else:
            rest_repr = ""
        return "Link(" + repr(self.first) + rest_repr + ")"

    def __str__(self):
        string = "<"
        while self.rest is not Link.empty:
            string += str(self.first) + " "
            self = self.rest
        return string + str(self.first) + ">"

# if link is Link.empty:
#     print("This linked list is empty!")


# Q1 What will Python output?
a = Link(1, Link(2, Link(3)))
print(a.first)
# >>> 1

a.first = 5
print(a.first)
# >>> 5

print(a.rest.first)
# >>> 2

# print(a.rest.rest.rest.rest.first)
# >>> error

a.rest.rest.rest = a
print(a.rest.rest.rest.rest.first)
# >>> 2


# Q2
# Write a function skip, which takes in a Link and returns a new Link with every other element skipped.
def skip(lst):
    """
    >>> a = Link(1, Link(2, Link(3, Link(4))))
    >>> a
    Link(1, Link(2, Link(3, Link(4))))
    >>> b = skip(a)
    >>> b
    Link(1, Link(3))
    >>> a
    Link(1, Link(2, Link(3, Link(4))))
    """
    if lst.rest.rest is not Link.empty:
        return Link(lst.first, skip(lst.rest.rest))
    elif lst.rest.rest is Link.empty:
        return Link(lst.first)


# Q3
# Now write function skip by mutating the original list, instead of returning a new list.
# Do NOT call the Link constructor.
def skip(lst):
    """
    >>> a = Link(1, Link(2, Link(3, Link(4))))
    >>> b = skip(a)
    >>> b
    >>> a
    Link(1, Link(3))
    """
    if lst.rest.rest is not Link.empty:
        lst.rest = lst.rest.rest
        skip(lst.rest)
    elif lst.rest.rest is Link.empty:
        lst.rest = Link.empty


# Q4
# Write a function reverse, which takes in a Link and returns a new Link that has the order of the contents reversed.
# Hint: You may want to use a helper function if youâ€™re solving this recursively.

def reverse(lst):
    """
    >>> a = Link(1, Link(2, Link(3)))
    >>> b = reverse(a)
    >>> b
    Link(3, Link(2, Link(1)))
    >>> a
    Link(1, Link(2, Link(3)))
    """
    rev = Link.empty
    while lst is not Link.empty:
        rev = Link(lst.first, rev)
        lst = lst.rest
    return rev


# Midterm Review
# Tree
class Tree:
    def __init__(self, label, branches=[]):
        for c in branches:
            assert isinstance(c, Tree)
        self.label = label
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ", " + repr(self.branches)
        else:
            branches_str = ""
        return "Tree({0}{1})".format(self.label, branches_str)

    def is_leaf(self):
        return not self.branches

    def __eq__(self, other):
        return type(other) is type(self) and self.label == other.label \
               and self.branches == other.branches

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = "  " * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

    def copy_tree(self):
        return Tree(self.label, [b.copy_tree() for b in self.branches])


# Q1
# Write a function that returns true only if there  exists a path from root to leaf that contains at least n instances of elem in a tree t

def contains(elem, n, t):
    """
    >>> t1 = Tree(1, [Tree(1, [Tree(2)])])
    >>> contains(1, 2, t1)
    True
    >>> contains(2, 2, t1)
    False
    >>> contains(2, 1, t1)
    True
    >>> t2 = Tree(1, [Tree(2), Tree(1, [Tree(1), Tree(2)])])
    >>> contains(1, 3, t2)
    True
    >>> contains(2, 2, t2) # Not on a path
    False
    """
    if n == 0:
        return True
    elif t.is_leaf() and n == 1:
        return t.label == elem
    elif t.label == elem:
        return True in [contains(elem, n-1, b) for b in t.branches]
    else:
        return True in [contains(elem, n, b) for b in t.branches]

# Q2
# Define the function factor_tree which returns a factor tree.
# Recall that in a factor tree, multiplying the leaves together is the prime factorization of the root, n.
# See below for an example of a factor tree for n = 20.

def factor_tree(n):
    for i in range(2, n):
        if n % i == 0:
            return Tree(n, [factor_tree(i), factor_tree(n // i)])
    return Tree(n)
