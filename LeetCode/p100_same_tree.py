# p100 Same Tree
# Easy


# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Note:
# Mirrored trees are considered not the same


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

    def __eq__(self, other):
        return str(self) == str(other)


def genTree(lst):
    """
    generate a binary tree according to a non-empty list of values
    The lst must be all filled, even the branch is empty, then use None to suggest the empty treeNode
    """
    LLL = log(len(lst)+1,2)
    if int(LLL) != LLL:
        print("List length is not complete, it must be 2^n - 1")
        raise ZeroDivisionError

    layers = []
    i, L = 0, 1

    while i != len(lst):
        layers.append(lst[i:i + L])
        i += L
        L *= 2
    pre_root = [TreeNode(i) for i in layers[0]]
    root_to_return = pre_root[0]

    for k in range(1, len(layers)):
        cur = [TreeNode(i) for i in layers[k]]
        for j in range(len(cur)):
            rt_idx, brc_side = divmod(j, 2)
            if brc_side == 0:
                pre_root[rt_idx].left = cur[j]
            else:
                pre_root[rt_idx].right = cur[j]
        pre_root = cur

    return root_to_return


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
