"""
https://leetcode.com/problems/unique-binary-search-trees-ii/
P095 Unique Binary Search Trees II
Medium

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
TODO after learning BST
"""

from typing import *
from a0_TreeNode import *


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        data = list(range(1, n))


if __name__ == "__main__":
    testCase = Solution()

    t1 = testCase.generateTrees(3)
    a1 = [
        genTree([1, None, 3, None, None, 2, None]),
        genTree([3, 2, None, 1, None, None, None]),
        genTree([3, 1, None, None, 2, None, None]),
        genTree([2, 1, 3]),
        genTree([1, None, 2, None, None, None, 3]),
    ]
    m1 = 0
    for trees in t1:
        for checks in a1:
            if trees == checks:
                m1 += 1
    assert len(t1) == len(a1) == m1, "Example 1"  # verify without sorted

    print("All passed")
