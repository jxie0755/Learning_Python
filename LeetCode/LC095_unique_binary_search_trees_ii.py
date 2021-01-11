# P095 Unique Binary Search Trees II
# Medium

# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
# TODO after learning BST

from typing import *
from a0_TreeNode import *


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        data = list(range(1, n))


if __name__ == "__main__":
    assert Solution().generateTrees(3) == [
        genTree([1, None, 3, None, None, 2, None]),
        genTree([3, 2, None, 1, None, None, None]),
        genTree([3, 1, None, None, 2, None, None]),
        genTree([2, 1, 3]),
        genTree([1, None, 2, None, None, None, 3]),
    ], "Example 1"

    print("all passed")
