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
        """
        Recursive compare left and right, inherit root level by + 1
        """
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    testCase = Solution_A()

    T0 = None
    assert testCase.maxDepth(T0) == 0, "Edge 0"

    T1 = TreeNode([1])
    assert testCase.maxDepth(T1) == 1, "Edge 1"

    T2 = genTree([
        3,
        9, 20,
        None, None, 15, None])
    assert testCase.maxDepth(T2) == 3, "Example 1"

    print("All passed")

