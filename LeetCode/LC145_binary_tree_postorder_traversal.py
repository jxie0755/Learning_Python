# LC145 Binary Tree Postorder Traversal
# Hard


# Given a binary tree, return the postorder traversal of its nodes' values.
# Follow up: Recursive solution is trivial, could you do it iteratively?


from typing import *
from a0_TreeNode import *


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

    B = genTree([
        1,
        2, 3,
        4, 5, 6, 7
    ])

    assert Solution().postorderTraversal(B) == [4, 5, 2, 6, 7, 3, 1], "Additional 1"

    C = genTree([
        1,
        2, 3,
        4, 5, 6, 7,
        8,9,10,11,12,13,14,15
    ])
    assert Solution().postorderTraversal(C) == [8, 9, 4, 10, 11, 5, 2, 12, 13, 6, 14, 15, 7, 3, 1], "Additional 2"

    print("All passed")
