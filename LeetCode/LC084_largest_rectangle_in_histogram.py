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
        increasing_idx = []  # 一个栈来记录连续上升的idx
        area, cur_idx = 0, 0
        while cur_idx <= len(heights):
            if not increasing_idx or (cur_idx < len(heights) and heights[cur_idx] > heights[increasing_idx[-1]]):
                # 空栈            whileloop未结束        上升趋势

                # 空栈,或者比栈中最后一个idx高度更高,也就是增高趋势
                increasing_idx.append(cur_idx)  # 入栈
                cur_idx += 1
            else:  # 一旦出现下降趋势,则停止i的变化,把栈依次推空,直到当前height超过栈中最高点
                # 若while loop结束,也做最后一次运算
                last = increasing_idx.pop()  # 依次将栈中最后一个idx退出,也就是
                if not increasing_idx:
                    # 如果没有上升趋势,则这是一个下降趋势,当前i就是最低点,面积就是这个点的高度*i
                    area = max(area, heights[last] * cur_idx)
                else:
                    # 通过记录栈中的idx和当前i的差值纯粹上升趋势中的来计算宽度
                    area = max(area, heights[last] * (cur_idx - increasing_idx[-1] - 1))
        return area


if __name__ == "__main__":
    testCase = Solution_STD()

    assert testCase.largestRectangleArea([]) == 0, "Edge 0"
    assert testCase.largestRectangleArea([2]) == 2, "Edge 1"
    assert testCase.largestRectangleArea([1, 2]) == 2, "Edge 2"

    assert testCase.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10, "Example 1"

    assert testCase.largestRectangleArea([4, 2, 0, 3, 2, 4, 3, 4]) == 10, "Additional 1"
    assert testCase.largestRectangleArea([0, 2, 0]) == 2, "Additional 2"

    additional = list(range(0, 30)) + list(range(30, 60, 2)) + list(range(60, 30, 3))
    assert testCase.largestRectangleArea(additional) == 506, "Additional Long 1"

    additional = list(range(0, 2000))
    assert testCase.largestRectangleArea(additional) == 1000000, "Additional Long 2"

    print("All passed")
