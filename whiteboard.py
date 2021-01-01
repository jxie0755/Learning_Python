"""
https://leetcode.com/problems/subsets/
P078 Subsets
Medium

Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
"""

from typing import *


class Solution_A:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    testCase = Solution_A()
    assert sorted(testCase.subsets([])) == [[]], "Edge empty"
    assert sorted(testCase.subsets([1])) == [[], [1]], "Edge 1"
    assert sorted(testCase.subsets([1, 2])) == [[], [1], [1, 2], [2]], "Example 1"
    assert sorted(testCase.subsets([1, 2, 3])) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]], "Example 2"
    print("all passed")
