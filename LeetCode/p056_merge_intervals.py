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


class Solution_A:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Sort first, then connect the two neighbored interval if possible
        Needs to pop, not working for array
        """
        if len(intervals) < 2:
            return intervals

        intervals.sort()
        i = 0
        while i != len(intervals) - 1:
            first, second = intervals[i], intervals[i + 1]
            if first[1] >= second[0]:
                first[1] = max(first[1], second[1])  # necessary, because [1,4] will be sorted before [2,3]
                intervals.pop(i + 1)
            else:
                i += 1
        return intervals


if __name__ == "__main__":
    testMethod = Solution_A().merge

    lst = [[0, 1]]
    assert testMethod(lst) == [[0, 1]], "Edge 1"

    lst = [[1, 3], [2, 6], [8, 10], [15, 18]]
    assert testMethod(lst) == [[1, 6], [8, 10], [15, 18]], "Example 1"

    lst = [[15, 18], [1, 3], [8, 10], [2, 6]]
    assert testMethod(lst) == [[1, 6], [8, 10], [15, 18]], "Example 1 unsorted"

    lst = [[1, 4], [4, 5]]
    assert testMethod(lst) == [[1, 5]], "Example 2"

    print("all passed")
