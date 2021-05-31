# LC129 Sum Root to Leaf Numbers
# Medium


# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.
# Note: A leaf is a node with no children.

from typing import *
from A02_TreeNode import *


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        pass


if __name__ == "__main__":
    A = genTree([
        1,
        2, 3
    ])
    assert Solution().sumNumbers(A) == 25, "Example 1, 12 + 13 = 25"

    A = genTree([
        4,
        9, 0,
        5, 1, None, None
    ])
    assert Solution().sumNumbers(A) == 1026, "Example 2, 495 + 491 + 40 = 1036"
    print("All passed")



