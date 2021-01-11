# P144 Binary Tree Preorder Taversal
# Meidum

# Given a binary tree, return the preorder traversal of its nodes' values.
# Follow up: Recursive solution is trivial, could you do it iteratively?

from typing import *
from a0_TreeNode import *


class Solution(object):

    def preorderTraversal(self, root):
        # Recursive method
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


if __name__ == "__main__":
    A = []
    assert not Solution().preorderTraversal(A), "Edge 0"

    A = genTree([
        1,
        None, 2,
        None, None, 3, None
    ])
    assert Solution().preorderTraversal(A) == [1, 2, 3], "Example 1"

    A = genTree([
        1,
        4, 3,
        2
    ])
    assert Solution().preorderTraversal(A) == [1, 4, 2, 3], "Example 2"

    print("all passed")
