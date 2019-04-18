# P084 Largest Rectangle in Histogram
# Hard


# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


from typing import *


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pass



if __name__ == '__main__':
    assert Solution().largestRectangleArea([]) == 0, 'Edge 1'
    assert Solution().largestRectangleArea([2]) == 2, 'Edge 2'
    assert Solution().largestRectangleArea([1,2]) == 2, 'Edge 3'

    assert Solution().largestRectangleArea([2,1,5,6,2,3]) == 10, 'Example 1'


