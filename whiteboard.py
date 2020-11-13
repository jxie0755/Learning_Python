"""
https://leetcode.com/problems/insert-interval/
P057 Insert Interval
Hard

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.
"""

from typing import *


# NOTE: input types have been changed on April 15, 2019.
# Please reset to default code definition to get new method signature.
#
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
#
#     def __repr__(self):
#         return f"[{self.start} -> {self.end}]"
#
#     def __eq__(self, other):
#         if self.start == other.start and self.end == other.end:
#             return True
#         return False


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        head_found = False
        end_found = False
        for interval in intervals:
            if interval[0] <= newInterval[0] < interval[1] < newInterval[1]:
                head_found = True
            if head_found and interval[0] <= newInterval[1] < interval[1]:
                end_found = True


if __name__ == "__main__":
    testCase = Solution()
    assert testCase.insert([], [1, 2]) == [[1, 2]], "Edge 1"

    assert testCase.insert([[1, 5]], [1, 2]) == [[1, 5]], "Edge 2"

    assert testCase.insert([[1, 5]], [2, 7]) == [[1, 7]], "Edge 3"

    lst = [[1, 3], [6, 9]]
    assert testCase.insert(lst, [2, 5]) == [
        [1, 5],
        [6, 9]
    ], "Example 1"

    lst = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    assert testCase.insert(lst, [4, 8]) == [
        [1, 2],
        [3, 10],
        [12, 16]
    ], "Example 2"

    lst = [[1, 2], [3, 7], [4, 6], [8, 10], [12, 16]]
    assert testCase.insert(lst, [4, 8]) == [
        [1, 2],
        [3, 10],
        [12, 16]
    ], "Example 2 extended"

    lst = [[1, 4], [7, 10]]
    assert testCase.insert(lst, [1, 2]) == [[1, 4], [7, 10]], "Extra 1"

    lst = [[1, 4], [7, 10]]
    assert testCase.insert(lst, [2, 3]) == [[1, 4], [7, 10]], "Extra 2"

    lst = [[1, 4], [7, 10]]
    assert testCase.insert(lst, [3, 4]) == [[1, 4], [7, 10]], "Extra 3"

    lst = [[1, 4], [7, 10]]
    assert testCase.insert(lst, [4, 5]) == [[1, 5], [7, 10]], "Extra 4"

    lst = [[1, 4], [7, 10]]
    assert testCase.insert(lst, [5, 6]) == [[1, 4], [5, 6], [7, 10]], "Extra 5"

    lst = [[1, 4], [7, 10]]
    assert testCase.insert(lst, [6, 7]) == [[1, 4], [6, 10]], "Extra 6"

    lst = [[1, 4], [7, 10]]
    assert testCase.insert(lst, [7, 8]) == [[1, 4], [7, 10]], "Extra 7"

    lst = [[1, 4], [7, 10]]
    assert testCase.insert(lst, [8, 9]) == [[1, 4], [7, 10]], "Extra 8"

    lst = [[1, 4], [7, 10]]
    assert testCase.insert(lst, [9, 10]) == [[1, 4], [7, 10]], "Extra 9"

    lst = [[1, 4], [7, 10]]
    assert testCase.insert(lst, [10, 11]) == [[1, 4], [7, 11]], "Extra 10"

    lst = [[1, 4], [7, 10]]
    assert testCase.insert(lst, [11, 12]) == [[1, 4], [7, 10], [11,12]], "Extra 10"

    print("all passed")
