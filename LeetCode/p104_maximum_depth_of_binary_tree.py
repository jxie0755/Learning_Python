# P104 Maximum Depth of Binary Tree
# Easy


# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the
# longest path from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):

        def layer(T, L=1):
            if not T.val:
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


def genTree(lst):
    """
    generate a binary tree according to a non-empty list of values
    The lst must be all filled, even the branch is empty, then use None to suggest the empty treeNode
    """
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
    def maxDepth(self, root: TreeNode) -> int:
        if not root or root.val is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == '__main__':
    A = None
    assert Solution().maxDepth(A) == 0, 'Edge 0'

    A = TreeNode([1])
    assert Solution().maxDepth(A) == 1, 'Edge 1'

    A = genTree([3,9,20,None, None, 15, 7])
    assert Solution().maxDepth(A) == 3, 'Example'

    print('All passed')
