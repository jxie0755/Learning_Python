"""
https://leetcode.com/problems/combination-sum-ii/
P040 Combination Sum II
Medium

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:
    All numbers (including target) will be positive integers.
    The difference between the P039 and P040 is that the candidates can be duplicated in P040 but not in P039
    The solution set must not contain duplicate combinations.
"""

from itertools import combinations
from typing import *


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        pass


if __name__ == "__main__":
    testCase = Solution()

    candidates = [10, 1, 2, 7, 6, 1, 5]
    assert testCase.combinationSum2(candidates, 8) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]], "Example 1"

    candidates = [2, 5, 2, 1, 2]
    assert testCase.combinationSum2(candidates, 5) == [[1, 2, 2], [5]], "Example 2"

    print("all passed")
