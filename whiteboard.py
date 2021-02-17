"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
P104 Maximum Depth of Binary Tree
Easy


Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the
longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.
"""

from a0_TreeNode import *


class Solution_A:
    def maxDepth(self, root: TreeNode) -> int:
        pass


if __name__ == "__main__":
    testCase = Solution_A()

    A = None
    assert testCase.maxDepth(A) == 0, "Edge 0"

    A = TreeNode([1])
    assert testCase.maxDepth(A) == 1, "Edge 1"

    A = genTree([3, 9, 20, None, None, 15, 7])
    assert testCase.maxDepth(A) == 3, "Example"

    print("All passed")
