# P084 Largest Rectangle in Histogram
# Hard


# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


from typing import *

count = 0

class Solution:
    ### Worked, but exceeded maximum recursion depth
    ### O(2N), maixmum depth reached at N > 999.
    def largestRectangleArea(self, heights: List[int]) -> int:
        global count
        count += 1
        print(count)
        N = len(heights)
        if not N:
            return 0
        elif len(set(heights)) == 1:
            return heights[0] * len(heights)
        elif N == 1:
            return heights[0]
        else:
            lowest = min(heights)
            lowest_idx = heights.index(lowest)
            area = lowest * N
            first, second = heights[:lowest_idx], heights[lowest_idx + 1:]
            return max(area, self.largestRectangleArea(first), self.largestRectangleArea(second))

class Solution(object):
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        increasing, area, i = [], 0, 0
        while i <= len(height):
            if not increasing or (i < len(height) and height[i] > height[increasing[-1]]):
                increasing.append(i)
                i += 1
            else:
                last = increasing.pop()

                if not increasing:
                    area = max(area, height[last] * i)
                else:
                    area = max(area, height[last] * (i - increasing[-1] - 1))

        return area

additional = list(range(0, 999))
print(Solution().largestRectangleArea(additional))

if __name__
