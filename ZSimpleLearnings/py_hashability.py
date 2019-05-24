# This is to find out why a data structure's hasbility can be impacted by some internal methods
# https://stackoverflow.com/q/56298727/8435726


from hashlib import md5

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self.next:
            return "{}->{}".format(self.val, repr(self.next))
        else:
            return "{}".format(self.val)

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

def genNode(*nodes, end=None):
    if len(nodes) == 1 and type(nodes[0]) == list:
        nodes = nodes[0]
    for i in nodes[::-1]:
        n = ListNode(i)
        n.next, end = end, n
    return n if nodes else None


# Notice that I blocked the __eq__ method. Now if I create an instance:
# Then it is hashable, however, I do get different output number everytime I run it.
print(hash('ABC'))

A = ListNode(1)
B = ListNode(2)
C = ListNode(3)
A.next = B
B.next = C
print(hash(A))

# Now if I unblock the __eq__ method, all of sudden it is not hashable anymore. Why?
# It seems that the hash method will use __eq__. And how does it know it is not hashable after __eq__ is enabled?

# Additional: If I write the __eq__ method to just compare the str version of the two linked list (the second __eq__ method), I thought this could solve the problem, because by converting the linked list into a string, it becomes an hashable data, but I still get the unhashable error message


### This is also True with leetcode's binary tree data structure
from math import log

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):

        def layer(T, L=1):
            if T.val is None:
                return 'N'

            s = str(T.val)
            if T.left and T.right:
                return s + '\n' + '  ' * L + layer(T.left, L + 1) + '\n' + '  ' * L + layer(T.right, L + 1)
            elif T.left and not T.right:
                return s + '\n' + '  ' * L + layer(T.left, L + 1) + '\n' + '  ' * L + 'N'
            elif not T.left and T.right:
                return s + '\n' + '  ' * L + 'N' + '\n' + '  ' * L + layer(T.right, L + 1)
            else:
                return s + '\n' + '  ' * L + 'N' + '\n' + '  ' * L + 'N'

        return layer(self)

    def __eq__(self, other):
        return str(self) == str(other)

    def isLeaf(self):
        try:
            leftval = self.left.val
        except AttributeError:
            leftval = None
        try:
            rightval = self.right.val
        except AttributeError:
            rightval = None

        return leftval and rightval

def genTree(lst, i=1):
    """
    To generate a perfect binary tree according to a non-empty list of values
    The lst must be all filled, even the branch is empty, then use None to suggest the empty treeNode
    """
    if lst and i <= len(lst) and lst[i-1] is not None:
        node = TreeNode(lst[i-1])
        node.left = genTree(lst, i*2)
        node.right = genTree(lst, i*2+1)
        return node


A = genTree([1,2,3])
# print(hash(A))


# Best answer: __eq__ will remove the default __hash__ method, so by creating a customized __hash__ method will make it hashable again.

# def __hash__(self):
#     return hash(str(self))

# THis will work
