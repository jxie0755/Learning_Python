"""
https://leetcode.com/problems/merge-intervals/
P056 Merge Intervals
Medium

Given a collection of intervals, merge all overlapping intervals.
"""

from typing import *

# NOTE: input types have been changed on April 15, 2019.
# Please reset to default code definition to get new method signature.
#
# Helper: Definition for an interval.
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
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    testCase = Solution()

    lst = [[0, 1]]
    assert testCase.merge(lst) == [[0, 1]], "Edge 1"

    lst = [[1, 3], [2, 6], [8, 10], [15, 18]]
    assert testCase.merge(lst) == [[1, 6], [8, 10], [15, 18]], "Example 1"

    lst = [[15, 18], [1, 3], [8, 10], [2, 6]]
    assert testCase.merge(lst) == [[1, 6], [8, 10], [15, 18]], "Example 1 unsorted"

    lst = [[1, 4], [4, 5]]
    assert testCase.merge(lst) == [[1, 5]], "Example 2"

    print("all passed")

