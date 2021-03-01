"""
https://leetcode.com/problems/path-sum/
P112 Path Sum
Easy

Given a binary tree and a sum,
determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.
"""

from a0_TreeNode import *


class Solution_A:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        pass


if __name__ == "__main__":
    testCase = Solution_A()

    T0 = None
    assert not testCase.hasPathSum(T0, 0), "Edge 0"

    T1 = genTree([1])
    assert testCase.hasPathSum(T1, 1), "Edge 1"

    T2 = genTree([
        5,
        4, 8,
        11, None, 13, 4,
        7, 2, None, None, None, None, None, 1
    ])
    assert testCase.hasPathSum(T2, 22), "Example 1, 5+4+11+2"

    T3 = genTree([
        1,
        2,3
    ])
    assert not testCase.hasPathSum(T3, 5), "Example 2"

    T4 = genTree([
        1,
        2, None
    ])
    assert not testCase.hasPathSum(T4, 0), "Example 3"

    print("All passed")
