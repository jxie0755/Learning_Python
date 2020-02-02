# P437 Path Sum III
# Easy


# You are given a binary tree in which each node contains an integer value.

# Find the number of paths that sum to a given value.

# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.


from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):

    # STD ans
    # Time:  O(n^2)
    # Space: O(h)
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def pathSumHelper(root, prev, sum):
            if root is None:
                return 0

            curr = prev + root.val
            return int(curr == sum) + \
                   pathSumHelper(root.left, curr, sum) + \
                   pathSumHelper(root.right, curr, sum)

        if root is None:
            return 0

        return pathSumHelper(root, 0, sum) + \
               self.pathSum(root.left, sum) + \
               self.pathSum(root.right, sum)


if __name__ == "__main__":
    assert Solution().pathSum(None, 1) == 0, "Edge 0"

    A = genTree([
        10,
        5, -3,
        3, 2, None, 11,
        3, -2, None, 1, None, None, None, None
    ])

    assert Solution().pathSum(A, 8) == 3, "Example 1"

    print("all passed")
