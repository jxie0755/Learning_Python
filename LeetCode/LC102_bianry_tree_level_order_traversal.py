"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
P102 Binary Tree Level Order Traversal
Medium


Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
"""

from a0_TreeNode import *


class Solution_A:
    def levelOrder(self, root: TreeNode):
        """
        Show the tree layer by layer from top to bottom
        This will omit None nodes
        """
        if root is None:
            return []

        result, layer = [], [root]
        while layer:
            next_layer, node_vals = [], []

            for node in layer:
                node_vals.append(node.val)

                # omit by checking left tand right None
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)

            layer = next_layer
            result.append(node_vals)

        return result


if __name__ == "__main__":
    testCase = Solution_A()

    A = None
    assert testCase.levelOrder(A) == [

    ], "Edge 0"

    A = genTree([1])
    assert testCase.levelOrder(A) == [
        [1]
    ], "Edge 1"

    A = genTree([3, 9, 20, None, None, 15, 7])
    assert testCase.levelOrder(A) == [
        [3],
        [9, 20],
        [15, 7],
    ], "Example 1"

    A = genTree([
        0,
        2, 4,
        1, None, 3, -1,
        5, 1, None, None, 6, None, 8, None])

    assert testCase.levelOrder(A) == [
        [0],
        [2, 4],
        [1, 3, -1],
        [5, 1, 6, 8],
    ], "Additional 1"

    print("All passed")
