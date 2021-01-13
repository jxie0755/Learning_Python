"""
https://leetcode.com/problems/largest-rectangle-in-histogram/
P084 Largest Rectangle in Histogram
Hard

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
"""

from typing import *


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pass


if __name__ == "__main__":
    testCase = Solution()
    assert testCase.largestRectangleArea([]) == 0, "Empty 1"
    assert testCase.largestRectangleArea([2]) == 2, "Edge 1"
    assert testCase.largestRectangleArea([1, 2]) == 2, "Edge 2"

    assert testCase.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10, "Example 1"

    assert testCase.largestRectangleArea([4, 2, 0, 3, 2, 4, 3, 4]) == 10, "Additional 1"
    assert testCase.largestRectangleArea([0, 2, 0]) == 2, "Additional 2"

    additional = list(range(0, 30)) + list(range(30, 60, 2)) + list(range(60, 30, 3))
    assert testCase.largestRectangleArea(additional) == 506, "Extra Long 1"

    additional = list(range(0, 2000))
    assert testCase.largestRectangleArea(additional) == 1000000, "Extra Long 2"

    print("All passed")
