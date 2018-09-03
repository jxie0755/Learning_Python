# From CS61A Week 08 Lecture 19

# Linked list
# a linked list is either empty or a first value and the rest of the linked list
# one link contains a pair of objects: 1. The value 2. another linked list
# At the end, use link.empty as a special instance.

# See also the functional setup in ZCodeSnippets.linked_list.py

class Link:
    """A linked list class"""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        # This is different from type(rest) == Link
        # Check detail from ZSimpleLearnings.py_instance_vs_type.py

        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ', '
            self = self.rest
        return string + str(self.first) + '>'

    @property
    def second(self):
        return self.rest.first

    @second.setter  # Must already exist (means .second should be a property)
    def second(self, value):
        self.rest.first = value


    # Additional functions
    def __len__(self):
        if self.rest:
            return 1 + len(self.rest)
        else:
            return 1

    def convert_to_list(self):
        """convert linked list to a list"""
        if self.rest:
            return [self.first] + self.rest.convert_to_list()
        else:
            return [self.first]

    def getitem(self, idx):
        """mimmic the single item slice function to get value at index numer
        ide is an integer
        return value at the idx
        """
        if idx + 1 <= len(self):
            if idx == 0:
                return self.first
            else:
                return self.rest.getitem(idx-1)
        return None



if __name__ == '__main__':
    s = Link(3, Link(4, Link(5)))
    print(repr(s)) # >>> Link(3, Link(4, Link(5)))

    print(s.first) # >>> 3
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

