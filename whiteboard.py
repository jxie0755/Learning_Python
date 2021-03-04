"""
https://leetcode.com/problems/path-sum-ii/
P113 Path Sum II
Medium


Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
Note: A leaf is a node with no children.

"""
from a0_TreeNode import *


class Solution_A:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        pass


if __name__ == "__main__":
    testCase = Solution_A()

    T0 = None
    assert testCase.pathSum(T0, 0) == [], "Edge 0"

    T1 = genTree([1])
    assert testCase.pathSum(T1, 1) == [
        [1]
    ], "Edge 1"

    T2 = genTree([
        5,
        4, 8,
        11, None, 13, 4,
        7, 2, None, None, None, None, 5, 1
    ])
    assert testCase.pathSum(T2, 22) == [
        [5, 4, 11, 2],
        [5, 8, 4, 5]
    ], "Example 1"

    print("All passed")
