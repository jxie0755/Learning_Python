# P103 Binary Tree Zigzag Level Order Traversal
# Medium


# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution:

    ### Similar to Leetcode P107, use the showLayers (modified version) to solve the problem
    def showLayers_zigzag(self, root):
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
                if i:
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

    ### This needs some modification of showLayers Method
    def zigzagLevelOrder(self, root: TreeNode):
        return self.showLayers_zigzag(root)



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
        5, 1, None, None, 6, None, 8, None])

    assert Solution().zigzagLevelOrder(A) == [
        [0],
        [4, 2],
        [1, 3, -1],
        [8, 6, 1, 5],
    ], 'Additional'

    print('All passed')
