# P107 Binary Tree Level Order Traversal II
# Easy


# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

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
    ### Use the showLayer operation but the maximum time limit is exceeded
    def showLayer(self, root: TreeNode):
        """show Layer of each tree level"""

        result = [[root.val]]
        layer = [root]

        while any([i for i in layer]):
            new_layer = []
            new_layer_val = []
            for i in layer:
                if i:
                    new_layer.append(i.left)
                    new_layer_val.append(i.left.val if i.left else None)
                    new_layer.append(i.right)
                    new_layer_val.append(i.right.val if i.right else None)
                else:
                    new_layer.append(None)
                    new_layer_val.append(None)
                    new_layer.append(None)
                    new_layer_val.append(None)

            result.append(new_layer_val)
            layer = new_layer
        return result

    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []
        elif not root.left and not root.right:
            return [[root.val]]

        result = []
        for i in self.showLayer(root)[::-1]:
            filtered = list(filter(lambda x:x is not None, i))  # Be careful with the t.val == 0
            result.append(filtered)
        return result[1:]


class Solution:
    def levelOrderBottom(self, root):
        ### STD ans
        ### Almost the same way as I tried, but it does not add None to next layer
        ### Use i.left and i.right to screen each node in current layer and only add the branch to next layer if the branch exist
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                if node:
                    vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)

        return result[::-1]


class Solution:
    def levelOrderBottom(self, root):
        ### A more structed stack method accoding to last method
        ### First build up the stack all the way to the bottom to get nodes at each layer
        ### Then extract the values of each node in every layer
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        stack = [[root]]
        current = [root]
        while current:
            next_level= []
            for node in current:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            stack.append(next_level)
            current = next_level

        result = []
        for i in stack[-2::-1]:
            vals = []
            for node in i:
                if node:
                    vals.append(node.val)
            result.append(vals)

        return result



if __name__ == '__main__':
    A = None
    assert Solution().levelOrderBottom(A) == [], 'Edge 0'

    A = genTree([1])
    assert Solution().levelOrderBottom(A) == [[1]], 'Edge 1'

    A = genTree([3, 9, 20, None, None, 15, 7])
    assert Solution().levelOrderBottom(A) == [
        [15,7],
        [9,20],
        [3]
    ], 'Example'

    A = genTree([
        0,
        2, 4,
        1, None, 3, -1,
        5, 1, None, None, 6, None, 8, None])
    assert Solution().levelOrderBottom(A) == [
        [5,1,6,8],
        [1,3,-1],
        [2,4],
        [0]
    ]

    print('All passed')
