"""
https: // leetcode.com / problems / symmetric - tree /
P101 Symmetric Tree
Easy

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
"""

from typing import *
from a0_TreeNode import *


class Solution_A:
    def isSymmetric(self, root: TreeNode) -> bool:
        pass


if __name__ == "__main__":
    testCase = Solution_A()

    T0 = None
    assert testCase.isSymmetric(T0), "Edge 0"

    T00 = TreeNode(1)
    assert testCase.isSymmetric(T00), "Edge 1"

    T1 = genTree([
        1,
        2, 2,
        3, 4, 4, 3
    ])
    assert testCase.isSymmetric(T1), "Example 1"

    T2 = genTree([
        1,
        2, 2,
        None, 3, None, 3
    ])
    assert not testCase.isSymmetric(T2), "Example 2"

    T3 = genTree([
        1,
        0, None
    ])
    assert not testCase.isSymmetric(T3), "Example 3"

    print("All passed")
