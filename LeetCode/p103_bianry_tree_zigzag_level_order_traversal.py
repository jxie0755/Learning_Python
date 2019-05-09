# P103 Binary Tree Zigzag Level Order Traversal
# Medium


# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

from typing import *

# Definition for a binary tree node.
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

    ### Similar to Leetcode P107, use the showLayer (modified version) to solve the problem
    def showLayer_zigzag(self, root):
        """show layers of tree"""
        if root is None:
            return []

        result = []
        layer = [root]
        REV = False
        while layer:
            vals = []
            new_layer = []

            for i in layer:
                if i and i.val is not None:
                    vals.append(i.val)
                if i.left:
                    new_layer.append(i.left)
                if i.right:
                    new_layer.append(i.right)
            if REV:
                result.append(vals[::-1])
            else:
                result.append(vals)
            REV = not REV

            layer = new_layer

        return result

    ### This needs some modification of showLayer Method
    def zigzagLevelOrder(self, root: TreeNode):
        return self.showLayer_zigzag(root)



if __name__ == '__main__':
    A = None
    assert Solution().zigzagLevelOrder(A) == [], 'Edge 0'

    A = genTree([1])
    assert Solution().zigzagLevelOrder(A) == [[1]], 'Edge 1'

    A = genTree([3, 9, 20, None, None, 15, 7])
    assert Solution().zigzagLevelOrder(A) == [
        [3],
        [20, 9],
        [15, 7],
    ], 'Example 1'

    A = genTree([
        0,
        2, 4,
        1, None, 3, -1,
        5, 1, None, 6, None, 8, None, None])

    assert Solution().zigzagLevelOrder(A) == [
        [0],
        [4, 2],
        [1, 3, -1],
        [8, 6, 1, 5],
    ], 'Additional'

    print('All passed')
