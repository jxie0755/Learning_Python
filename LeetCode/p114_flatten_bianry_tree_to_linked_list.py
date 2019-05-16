# P114 Flatten Binary Tree to Linked List
# Medium

# Given a binary tree, flatten it to a linked list in-place.
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

def genTree(lst):
    """
    generate a binary tree according to a non-empty list of values
    The lst must be all filled, even the branch is empty, then use None to suggest the empty treeNode
    """
    if not lst:
        return None

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
        cur = []
        for i in layers[k]:
            if i is not None:
                cur.append(TreeNode(i))
            else:
                cur.append(None)

        for j in range(len(cur)):
            rt_idx, brc_side = divmod(j, 2)
            if brc_side == 0 and cur[j] is not None:
                pre_root[rt_idx].left = cur[j]
            elif brc_side != 0 and cur[j] is not None:
                pre_root[rt_idx].right = cur[j]
        pre_root = cur

    return root_to_return


class Solution:
    def traverse(self, root):
        if not root:
            return []
        return [root.val] + self.traverse(root.left) + self.traverse(root.right)

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        travel = self.traverse(root)
        if len(travel) > 1:
            i = 1
            root.left = None
            while i != len(travel):
                new = TreeNode(travel[i])
                root.right = new
                root = new
                i += 1


if __name__ == '__main__':
    A = None
    Solution().flatten(A)
    assert not A, 'Edge 0'

    A = TreeNode(0)
    Solution().flatten(A)
    assert A == A, 'Edge 1'

    A = TreeNode(1)
    Solution().flatten(A)
    assert A == A, 'Edge 2'

    A = genTree([
        1,
        2,5,
        3,4,None,6
    ])
    Solution().flatten(A)
    assert A == genTree([
        1,
        None, 2,
        None, None, None, 3,
        None, None, None, None,
        None, None, None, 4,
        None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, 5,
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 6
    ]), 'Example 1'

    print('all passed')
