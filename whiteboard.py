"""
https://leetcode.com/problems/container-with-most-water/
P011 Container with Most Water
Medium

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0)
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note:
    You may not slant the container and n is at least 2.
"""

from typing import *


class Solution:
    def maxArea(self, height: List[int]) -> int:
        pass





if __name__ == "__main__":
    testCase = Solution()
    assert testCase.maxArea([0, 0]) == 0, "Edge 1"
    assert testCase.maxArea([0, 0, 0]) == 0, "Edge 2"

    assert testCase.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49, "Example 1"
    assert testCase.maxArea([2, 3, 0, 0, 3, 0, 0, 0, 0, 2]) == 18, "Example 2"
    assert testCase.maxArea([2, 3, 4, 5, 6, 7, 8, 9, 100, 100]) == 100, "Example 3"
    assert testCase.maxArea([1, 1, 1, 1, 1, 10, 10, 1, 1, 1, 1, 1]) == 11, "Example 4"
    assert testCase.maxArea([1, 1, 4, 1, 5, 5, 4, 1, 1, 1]) == 16, "Example 5"

    print("All passed")
