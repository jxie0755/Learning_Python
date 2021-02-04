"""
https://leetcode.com/problems/unique-binary-search-trees-ii/
P095 Unique Binary Search Trees II
Medium

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
"""

from typing import *
from a0_TreeNode import *


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
        DP method
        create a list, Length = 2^n-1 (maximum possible length)
        Then assign the element at idx to generate tree
        """
        result = []
        L = list(range(1, n+1))
        candidates = [None for i in range(2**n - 1)]






    def genTree(self, lst: List[int], idx: int = 0) -> TreeNode:
        """
        A helper fucntion just like TreeNode.genTree to solve this problem
        """
        if len(lst) >= idx + 1 and lst[idx] is not None:
            node = TreeNode(lst[idx])
            node.left = self.genTree(lst, idx * 2 + 1)
            node.right = self.genTree(lst, idx * 2 + 2)
            return node


Solution().generateTrees(1)

# if __name__ == "__main__":
#     testCase = Solution()
#
#     t1 = testCase.generateTrees(3)
#     a1 = [
#         genTree([1, None, 3, None, None, 2, None]),
#         genTree([3, 2, None, 1, None, None, None]),
#         genTree([3, 1, None, None, 2, None, None]),
#         genTree([2, 1, 3]),
#         genTree([1, None, 2, None, None, None, 3]),
#     ]
#     m1 = 0
#     for trees in t1:
#         for checks in a1:
#             if trees == checks:
#                 m1 += 1
#     assert len(t1) == len(a1) == m1, "Example 1"  # verify without sorted
#
#     print("All passed")
