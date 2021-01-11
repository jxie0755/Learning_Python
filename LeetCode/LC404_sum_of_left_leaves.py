# P404 Sum of Left Leaves
# Easy

# Find the sum of all left leaves in a given binary tree.

from typing import *
from a0_TreeNode import *


class Solution:

    # Version A, Recursive
    # Check one level below
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        if not root or not root.left and not root.right:
            return 0
        else:
            if root.left:
                if root.left.left or root.left.right:
                    left = self.sumOfLeftLeaves(root.left)
                else:
                    left = root.left.val
            else:
                left = 0

            if root.right:
                right = self.sumOfLeftLeaves(root.right)
            else:
                right = 0

        return left + right


class Solution(object):

    # STD ans, with a recursive label helper
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        def sumOfLeftLeavesHelper(root, is_left):

            if not root:
                return 0

            if not root.left and not root.right:  # is_leaf
                return root.val if is_left else 0

            return sumOfLeftLeavesHelper(root.left, True) + sumOfLeftLeavesHelper(root.right, False)

        return sumOfLeftLeavesHelper(root, False)


if __name__ == "__main__":
    assert Solution().sumOfLeftLeaves(None) == 0, "Edge 0"

    assert Solution().sumOfLeftLeaves(TreeNode(5)) == 0, "Edge root"

    A = genTree([
        3,
        9, 20,
        None, None, 15, 7
    ])
    assert Solution().sumOfLeftLeaves(A) == 24, "Example 1"

    A = genTree([
        1,
        2, None
    ])
    assert Solution().sumOfLeftLeaves(A) == 2, "Example 2"

    A = genTree([
        0,
        2, 4,
        1, None, 3, -1,
        5, 1, None, None, None, 6, None, 8
    ])
    assert Solution().sumOfLeftLeaves(A) == 5, "Example 3"

    print("all passed")
