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


    print("all passed")
