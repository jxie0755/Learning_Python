# P110 Balanced Binary Tree
# Easy


# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

from a0_TreeNode import *


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)


if __name__ == "__main__":
    A = None
    assert Solution().isBalanced(A), "Edge 0"

    A = genTree([1])
    assert Solution().isBalanced(A), "Edge 1"

    A = genTree([
        3,
        9, 20,
        None, None, 15, 7])

    assert Solution().isBalanced(A), "Example 1"

    A = genTree([
        1,
        2, 2,
        3, 3, None, None,
        4, 4, None, None, None, None, None, None
    ])

    assert not Solution().isBalanced(A), "Example 2"

    A = genTree([
        1,
        2, 2,
        3, 3, 3, 3,
        4, 4, 4, 4, 4, 4, None, None,
        5, 5, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    ])

    assert Solution().isBalanced(A), "Additional 1"

    A = genTree([
        1,
        None, 2,
        None, None, None, 3
    ])
    assert not Solution().isBalanced(A), "Additional 2"

    print("all passed")
