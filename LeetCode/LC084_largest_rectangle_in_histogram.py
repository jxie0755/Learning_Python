"""
https://leetcode.com/problems/largest-rectangle-in-histogram/
P084 Largest Rectangle in Histogram
Hard

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
"""

from typing import *


class Solution_A:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Worked, but exceeded maximum recursion depth
        maximum depth reached at N > 999.
        """

        width = len(heights)
        if width == 0:
            return 0
        elif width == 1:
            return heights[0]
        else:
            lo_height = min(heights)
            lo_idx = heights.index(lo_height)
            area = lo_height * width
            first, second = heights[:lo_idx], heights[lo_idx + 1:]
            return max(area,
                       self.largestRectangleArea(first),
                       self.largestRectangleArea(second)
                       )


class Solution_STD:

    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        堆栈法
        从左到有遍历, 入栈规则:
            如果升高, 则入栈
            如果降低, 则分析此前所有升高的栈,从后往前pop, 直到栈中末尾出现比此更低的值, 然后将其入栈

        关键原理:
            如果持续升高或降低, 则问题比较容易分析
            一旦出现升高后的降低, 则此前所有比这个低的bar的具体高度已经没有意义, 因为从这里开始往后高度都被限制在了这个较矮的bar这里
        """
        increasing, area, i = [], 0, 0
        while i <= len(heights):
            if not increasing or (i < len(heights) and heights[i] > heights[increasing[-1]]):
                increasing.append(i)
                i += 1
            else:
                last = increasing.pop()
                if not increasing:
                    area = max(area, heights[last] * i)
                else:
                    area = max(area, heights[last] * (i - increasing[-1] - 1))
        return area


if __name__ == "__main__":
    testCase = Solution_STD()

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
