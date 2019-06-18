# P385 Mini Parser
# Medium


# Given a nested list of integers represented as a string, implement a parser to deserialize it.

# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# Note: You may assume that the string is well-formed:
# String is non-empty.
# String does not contain white spaces.
# String contains only digits 0-9, [, - ,, ].

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:

    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        self.lst = []
        self.val = value

    def __str__(self):
        if self.isInteger():
            return str(self.val)
        else:
            return '[' + str(self.val) + ',' + str(self.lst) + ']'

    def __repr__(self):
        return str(self)

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return self.val is not None and len(self.lst) == 0

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        self.lst.append(NestedInteger(elem))

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        self.val = value
        self.lst = []

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        if self.isInteger():
            return self.val
        else:
            return None

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        if self.isInteger():
            return None
        else:
            return self.lst



def deserialize(self, s: str) -> NestedInteger:
    pass













if not __name__ == '__main__':
    A = Solution().deserialize('324')
    B = Solution().deserialize("[123,[456,[789]]]")
    print('all passed')
