# P145 Binary Tree Postorder Traversal
# Hard


# Given a binary tree, return the postorder traversal of its nodes' values.
# Follow up: Recursive solution is trivial, could you do it iteratively?


from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):

    # Version A
    # Recursive method
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


if __name__ == "__main__":
    A = genTree([
        1,
        None, 2,
        None, None, 3, None
    ])

    assert Solution().postorderTraversal(A) == [3, 2, 1], "Example 1"

    print("all passed")
