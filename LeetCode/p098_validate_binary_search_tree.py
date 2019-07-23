# P098 Validate Binary Search Tree
# Medium


# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.

# Both the left and right subtrees must also be binary search trees.

from typing import *

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution:

    # Use inorderTraversal to get the list from Leetcode P094
    # Then filter the None out from the list and check if the list is sorted
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            # Must write this way to avoid val=0
            # Do not write "not root.val"
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def isValidBST(self, root: TreeNode) -> bool:
        flat = list(filter(lambda x: x is not None, self.inorderTraversal(root)))

        if not flat:
            return True

        for i in range(1, len(flat)):
            if flat[i] <= flat[i - 1]:
                return False
        return True


if __name__ == "__main__":
    A = genTree([2, 1, 3])
    assert Solution().isValidBST(A), "Example 1"

    A = genTree([
        5,
        1, 4,
        None, None, 3, 6
    ])

    assert not Solution().isValidBST(A), "Example 2"

    A = genTree([
        5,
        1, 6,
        None, None, 3, 7
    ])
    assert not Solution().isValidBST(A), "Additional"

    A = genTree([0, None, -1])
    assert not Solution().isValidBST(A), "Additional"

    print("all passed")
