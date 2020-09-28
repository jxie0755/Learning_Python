"""
https://leetcode.com/problems/first-missing-positive/
P041 First Missing Positive
Hard

Given an unsorted integer array, find the smallest missing positive integer.

Note:
    Your algorithm should run in O(n) time and uses constant extra space.
"""

from typing import *


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pass






if __name__ == "__main__":
    testCase = Solution()
    assert testCase.firstMissingPositive([]) == 1, "Edge 1"
    assert testCase.firstMissingPositive([1]) == 2, "Edge 2"
    assert testCase.firstMissingPositive([2]) == 1, "Edge 3"
    assert testCase.firstMissingPositive([-1]) == 1, "Edge 4"

    assert testCase.firstMissingPositive([1, 2, 0]) == 3, "Example 1"
    assert testCase.firstMissingPositive([3, 4, -1, 1]) == 2, "Example 2"
    assert testCase.firstMissingPositive([7, 8, 9, 11, 12]) == 1, "Example 3"

    print("all passed")
