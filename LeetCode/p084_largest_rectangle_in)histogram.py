# P084 Largest Rectangle in Histogram
# Hard


# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


from typing import *


class Solution:
    # Worked, but exceeded maximum recursion depth
    # O(2N), maixmum depth reached at N > 999.
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
    # TODO to be reviewed
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

if __name__ == "__main__":
    assert Solution().largestRectangleArea([]) == 0, "Edge 1"
    assert Solution().largestRectangleArea([2]) == 2, "Edge 2"
    assert Solution().largestRectangleArea([1, 2]) == 2, "Edge 3"

    assert Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10, "Example 1"

    assert Solution().largestRectangleArea([4, 2, 0, 3, 2, 4, 3, 4]) == 10, "Additional 1"
    assert Solution().largestRectangleArea([0, 2, 0]) == 2, "Additional 2"

    additional = list(range(0, 30)) + list(range(30, 60, 2)) + list(range(60, 30, 3))
    print(Solution().largestRectangleArea(additional))

    additional = list(range(0, 2000))
    print(Solution().largestRectangleArea(additional))

    print("all passed")
