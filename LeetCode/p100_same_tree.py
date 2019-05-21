# p100 Same Tree
# Easy


# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Note:
# Mirrored trees are considered not the same
# Circular trees can not be tested


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
    if not lst:
        return None

    N = len(lst)
    if i > N:
        return None

    val = lst[i-1]
    node = TreeNode(val)
    if val is not None:
        node.left = genTree(lst, i*2)
        node.right = genTree(lst, i*2+1)
        return node


class Solution:
    # def isSameTree(self, p, q):
    #     """
    #     :type p: TreeNode
    #     :type q: TreeNode
    #     :rtype: bool
    #     """
    #     if not p and not q:
    #         return True
    #     elif not p or not q:
    #         return False
    #     elif p.left and q.left and p.right and q.right:
    #         return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    #     elif p.left and q.left:
    #         return p.val == q.val and self.isSameTree(p.left, q.left) and not p.right and not q.right
    #     elif p.right and q.right:
    #         return p.val == q.val and self.isSameTree(p.right, q.right) and not p.left and not q.left
    #     else:
    #         return p.val == q.val and not p.left and not q.left and not p.right and not q.right

        def isSameTree(self, p, q):
            """
            :type p: TreeNode
            :type q: TreeNode
            :rtype: bool
            """
            if not p and not q:
                return True
            elif not p or not q:
                return False
            else:
                return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    T10 = genTree([
        1,
        2, 3
    ])
    T20 = genTree([
        1,
        2, 3
    ])

    assert Solution().isSameTree(T10, T20) == True, 'T1'

    T10 = genTree([
        1,
        2, 3,
        4, None, None, None
    ])
    T20 = genTree([
        1,
        3, 2,
        4, None, None, None
    ])

    assert Solution().isSameTree(T10, T20) == False, 'T2'

    print('all passed')
