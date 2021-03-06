"""
P094 Binary Tree Inorder Traversal
Medium


Given a binary tree, return the inorder traversal of its nodes' values.
中序遍历就是二叉树的平面投影,从左到右
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

from typing import *
from a0_TreeNode import *


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


if __name__ == "__main__":
    testCase = Solution()

    t0 = None
    assert testCase.inorderTraversal(t0) == []

    t1 = genTree([
        1,
        None, 2,
        None, None, 3, None])
    print(Solution().inorderTraversal(t1))
    assert testCase.inorderTraversal(t1) == [1, 3, 2]

    print("All passed")

