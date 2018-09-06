# From CS61A Week 08 Lecture 19

# Linked list
# a linked list is either empty or a first value and the rest of the linked list
# one link contains a pair of objects: 1. The value 2. another linked list
# At the end, use link.empty as a special instance.

# See also the functional setup in ZCodeSnippets.linked_list.py

class Link:
    """A linked list class"""
    empty = ()

    def __init__(self, value, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        # This is different from type(rest) == Link
        # Check detail from ZSimpleLearnings.py_instance_vs_type.py

        self.value = value
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.value, rest_str)

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.value) + ', '
            self = self.rest
        return string + str(self.value) + '>'

    @property
    def second(self):
        return self.rest.value

    @second.setter  # Must already exist (means .second should be a property)
    def second(self, value):
        self.rest.value = value


    # Additional functions
    def __len__(self):
        if self.rest:
            return 1 + len(self.rest)
        else:
            return 1

    def convert_to_list(self):
        """convert linked list to a list"""
        if self.rest:
            return [self.value] + self.rest.convert_to_list()
        else:
            return [self.value]

    def getitem(self, idx):
        """mimmic the single item slice function to get value at index numer
        ide is an integer
        return value at the idx
        """
        if idx + 1 <= len(self):
            if idx == 0:
                return self.value
            else:
                return self.rest.getitem(idx-1)
        return None

    def tail(self):
        """return the tail link of a linked list"""
        if self.rest:
            return self.rest.tail()
        else:
            return self

    def copy(self):
        """return a copy of the linked list but a differnt object ID"""
        if self.rest:
            return Link(self.value, self.rest.copy())
        else:
            return Link(self.value)

    def __add__(self, other):
        """to extend the linked list with another linked list"""
        result = self.copy()
        result.tail().rest = other
        return result

    def reverse(self):
        """return a linked list that is reversed from itself in index sequence"""
        lst = self.convert_to_list()[::-1]
        reverse_link = Link(lst[0])
        for i in lst[1:]:
            reverse_link += Link(i)
        return reverse_link

    def remove(self, value):
        """Remove all the nodes containing value.
        Assume there exists some nodes to be removed and the first element is never removed."""

        if self.rest and self.rest.value == value:
            self.rest = self.rest.rest
            self.remove(value)
        elif self.rest == Link.empty and self.value == value:
            self = Link.empty
            self.rest.remove(value)
        else:
            if self.rest:
                self.rest.remove(value)

    def deep_map_mut(self, fn):
        """Mutates a deep link by replacing each item found with the
        result of calling fn on the item.  Does NOT create new Links (so
        no use of Link's constructor)

        Does not return the modlified Link object.
        """
        if not isinstance(self.value, Link):
            self.value = fn(self.value)
        else:
            self.value.deep_map_mut(fn)

        if self.rest:
            self.rest.deep_map_mut(fn)

if __name__ == '__main__':
    s = Link(3, Link(4, Link(5)))
    print(repr(s)) # >>> Link(3, Link(4, Link(5)))

    print(s.value) # >>> 3
    print(s.rest)  # >>> <4, 5>
    print(s) # >>> <3, 4, 5>

    b = Link(8, s.rest)
    print(b) # >>> <8, 4, 5>

    print(s.rest.rest.rest == Link.empty)  # >>> True


    # Test property
    print(b.second)  # >>> 4  (when becomes a property, no need for the function "()" at the end)
    b.second = 9
    print(b)  # >>> <8, 9, 5>

    # Additional functions
    print(len(b))  # >>> 3
    print(b.convert_to_list()) # >>> [8, 9, 5]
    print(b.getitem(2)) # >>> 5
    print(b.getitem(3)) # >>> None (over-index)

    link_1 = Link(3, Link(4, Link(5)))
    link_2 = Link(6, Link(7, Link(8)))

    tl = link_1.tail()
    print(tl)  # >>> <5>
    tl.rest = Link(0, Link(0, Link(0)))
    print(link_1)

    link_3 = Link(3, Link(4, Link(5)))
    link_4 = Link(6, Link(7, Link(8)))
    print(link_3 + link_4) # >>> <3, 4, 5, 6, 7, 8>

    print(link_4.reverse()) # >>> <8, 7, 6>

    l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    print(l1)           # >>> <0, 2, 2, 3, 1, 2, 3>
    l1.remove(2)
    print(l1)           # >>> <0, 3, 1, 3>
    l1.remove(3)
    print(l1)           # >>> <0, 1>

    link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    link1.deep_map_mut(lambda x: x * x)
    print(link1)
