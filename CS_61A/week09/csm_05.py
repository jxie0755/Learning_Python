# CS61A CSM 05: Linked Lists and Midterm Review



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
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

# if link is Link.empty:
#     print('This linked list is empty!')


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
# Hint: You may want to use a helper function if you’re solving this recursively.

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

