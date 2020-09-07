"""
https://leetcode.com/problems/combination-sum/
P039 Cobination Sum
Medium

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:
    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.
"""

from typing import *


class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        pass





if __name__ == "__main__":
    testCase = Solution()
    assert testCase.combinationSum([], 1) == [], "Edge 1"
    assert testCase.combinationSum([1], 1) == [[1]], "Edge 2"
    assert testCase.combinationSum([1], 2) == [[1, 1]], "Edge 3"
    assert testCase.combinationSum([2], 1) == [], "Edge 4"
    assert testCase.combinationSum([2], 5) == [], "Edge 5"

    assert testCase.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]], "Example 1"
    assert testCase.combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]], "Example 2"

    assert testCase.combinationSum([2, 4], 10) == [[2, 2, 2, 2, 2], [2, 2, 2, 4], [2, 4, 4]], "Extra 1"

    print("all passed")
