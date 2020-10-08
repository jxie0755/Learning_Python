"""
https://leetcode.com/problems/trapping-rain-water/
P042 Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
"""

from typing import *


class Solution:
    def trap(self, height: List[int]) -> int:
        pass




if __name__ == "__main__":
    testCase = Solution()
    assert testCase.trap([]) == 0, "Edge 1"
    assert testCase.trap([0]) == 0, "Edge 2"
    assert testCase.trap([1]) == 0, "Edge 3"
    assert testCase.trap([1, 1]) == 0, "Edge 4"
    assert testCase.trap([2, 2, 2]) == 0, "Edge 5"
    assert testCase.trap([2, 0, 2]) == 2, "Edge 6"

    assert testCase.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6, "Example 1"
    assert testCase.trap([10, 1, 2, 1, 2, 1, 10]) == 43, "Example 2"
    assert testCase.trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6]) == 23, "Example 3"
    assert testCase.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6, "Extra 1"
    print("all passed")
