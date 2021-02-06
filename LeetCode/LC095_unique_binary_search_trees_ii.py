"""
https://leetcode.com/problems/unique-binary-search-trees-ii/
P095 Unique Binary Search Trees II
Medium

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
"""

from typing import *
from a0_TreeNode import *


class Solution:
    def genTree(self, lst: List[int], idx: int = 0) -> TreeNode:
        """
        A helper fucntion just like TreeNode.genTree to solve this problem
        """
        if len(lst) >= idx + 1 and lst[idx] is not None:
            node = TreeNode(lst[idx])
            node.left = self.genTree(lst, idx * 2 + 1)
            node.right = self.genTree(lst, idx * 2 + 2)
            return node

    def generateTrees(self, n: int) -> List[TreeNode]:
        """
        DP method
        create a list, Length = 2^n-1 (maximum possible length)
        Then assign the element at idx to generate tree
        """
        template = [None for _ in range(2 ** n - 1)]
        result = [template]

        L = 1
        idx_list = [0]
        while L != 3:
            new_result = []
            new_rt_idx = []
            for candidate in result:
                for idx in idx_list:
                    new_rt_idx.append(idx * 2 + 1)  # add left to new rt list
                    new_rt_idx.append(idx * 2 + 2)  # add right to new rt list
                    if L == 1:
                        for i in range(1, n + 1):
                            new_candidate = candidate.copy()
                            new_candidate[idx] = i
                            new_result.append(new_candidate)
                    else:
                        # todo 笛卡尔乘积
                        # 把每一层的所有组合凑出来
                        # determine parent root idx
                        direction = idx % 2
                        if direction == 1:  # node on L side
                            prev = (idx - 1) // 2
                            if candidate[prev]:
                                for j in range(1, candidate[prev]):
                                    pass

                        if direction == 0:  # node on R side
                            prev = (idx - 2) // 2
                            if candidate[prev]:
                                for j in range(candidate[prev] + 1, n + 1):
                                    pass

            result = new_result
            idx_list = new_rt_idx
            L += 1


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
