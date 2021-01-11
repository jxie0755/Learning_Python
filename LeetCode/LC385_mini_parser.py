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

    def __repr__(self):
        if self.isInteger():
            return "[" + str(self.val) + "]"
        else:
            return "[" + str(self.val) + "," + str(self.getList()[0]) + "]"

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return len(self.lst) == 0

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


if __name__ == "__main__":
    A = NestedInteger(1)
    assert repr(A) == "[1]", "Eaxmple 1"
    assert A.getInteger() == 1, "get integer"
    assert A.isInteger(), "Single integer"
    assert not A.getList(), "Single integer has no list"

    A.add(-2)
    assert repr(A) == "[1,[-2]]", "Add -2"
    assert repr(A.getList()) == "[[-2]]", "nested list"
    assert not A.isInteger()
    assert not A.getInteger()

    A.setInteger(5)
    assert repr(A) == "[5]", "set Integer"

    print("All passed")


class Solution(object):

    # STD ans
    # Not sure what this is
    def deserialize(self, s):
        if not s:
            return NestedInteger()

        if s[0] != "[":
            return NestedInteger(int(s))

        stk = []

        i = 0
        for j in range(len(s)):
            if s[j] == "[":
                stk += NestedInteger(),
                i = j + 1
            elif s[j] in ",]":
                if s[j - 1].isdigit():
                    stk[-1].add(NestedInteger(int(s[i:j])))
                if s[j] == "]" and len(stk) > 1:
                    cur = stk[-1]
                    stk.pop()
                    stk[-1].add(cur)
                i = j + 1

        return stk[-1]
