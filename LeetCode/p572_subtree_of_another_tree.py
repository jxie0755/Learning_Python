# P572 Subtree of Another Tree
# Easy


# Given two non-empty binary trees s and t
# check whether tree t has exactly the same structure and node values with a subtree of s.
# A subtree of s is a tree consists of a node in s and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.


from typing import *

# Definition for a binary tree node.
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

class Solution:
    def sameTree(self, s, t):
        if s is t is None:
            return True
        elif (not s and t) or (s and not t):
            return False
        else:
            return s.val == t.val and self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s and s.val == t.val:
            return self.sameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        elif s and s.val != t.val:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        else:
            return False

class Solution:

    def traverse(self, t):
        """return a flat list of the binary tree including None"""
        if not t:
            return [None]
        return [t.val] + self.traverse(t.left) + self.traverse(t.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """check if traverse(t) is a sublist of traverse(s)"""
        list_s, list_t = self.traverse(s), self.traverse(t)
        len_s, len_t = len(list_s), len(list_t)
        for i in range(0, len_s - len_t + 1):
            if list_s[i:i+len_t] == list_t:
                return True
        return False



if __name__ == '__main__':

    E1 = genTree([
        3,
        4, 5,
        1, 2, None, None
    ])

    E2 = genTree([
        4,
        1, 2
    ])

    assert Solution().isSubtree(E1, E2), 'Example 1'

    E1 = genTree([
        3,
        4,5,
        1,2,None, None,
        None, None, 0, None, None, None, None, None
    ])

    E2 = genTree([
        4,
        1,2
    ])

    assert not Solution().isSubtree(E1, E2), 'Example 2'

    E3 = genTree([
        3,
        None,9,
        None,None,4,None,None,
        None,None,None,1,2,None,None,
        None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
    ])

    E4 = genTree([
        4,
        1,2
    ])

    assert Solution().isSubtree(E3, E4), 'Addtional 1'

    print('all passed!')
