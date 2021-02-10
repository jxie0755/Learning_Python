"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
P103 Binary Tree Zigzag Level Order Traversal
Medium


Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
"""

from a0_TreeNode import *


class Solution_A:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        pass




if __name__ == "__main__":
    testCase = Solution_A()

    A = None
    assert testCase.zigzagLevelOrder(A) == [

    ], "Edge 0"

    A = genTree([1])
    assert testCase.zigzagLevelOrder(A) == [
        [1]
    ], "Edge 1"

    A = genTree([3, 9, 20, None, None, 15, 7])
    assert testCase.zigzagLevelOrder(A) == [
        [3],
        [20, 9],
        [15, 7],
    ], "Example 1"

    A = genTree([
        0,
        2, 4,
        1, None, 3, -1,
        5, 1, None, None, 6, None, 8, None])

    assert testCase.zigzagLevelOrder(A) == [
        [0],
        [4, 2],
        [1, 3, -1],
        [8, 6, 1, 5],
    ], "Additional 1"

    print("All passed")
