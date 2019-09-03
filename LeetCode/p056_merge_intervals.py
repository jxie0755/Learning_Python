"""
https://leetcode.com/problems/merge-intervals/
P056 Merge Intervals
Medium

Given a collection of intervals, merge all overlapping intervals.
"""

from typing import *

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
        """
        Version A
        Sort first, then connect the two neighbored interval if possible
        """
        intervals.sort()
        if len(intervals) >= 2:
            i = 0
            while i != len(intervals) - 1:
                first, second = intervals[i], intervals[i + 1]
                if first[1] >= second[0]:
                    first[1] = max(first[1], second[1])
                    intervals.pop(i + 1)
                else:
                    i += 1
        return intervals


if __name__ == "__main__":
    E0 = [0, 1]
    lst = [E0]
    assert Solution().merge(lst) == [E0], "Edge 1"

    A1 = [1, 3]
    A2 = [2, 6]
    A3 = [8, 10]
    A4 = [15, 18]
    lst = [A1, A2, A3, A4]

    assert Solution().merge(lst) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ], "Example 1"

    B1 = [1, 4]
    B2 = [4, 5]
    lst = [B1, B2]
    assert Solution().merge(lst) == [
        [1, 5],
    ], "Example 2"

    print("all passed")
