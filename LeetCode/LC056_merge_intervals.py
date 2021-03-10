"""
https://leetcode.com/problems/merge-intervals/
LC056 Merge Intervals
Medium

Given a collection of intervals, merge all overlapping intervals.
"""


# NOTE: input types have been changed on April 15, 2019.
# Please reset to default code definition to get new method signature.

# Helper: Definition for an interval.
# No longer in use

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


from typing import *


class Solution_A:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Sort first, then connect the two neighbored interval if possible
        Needs to pop, not working for array
        This change in-place
        """
        if len(intervals) < 2:
            return intervals

        # sort first
        # this is not python's default sort (because it only comparing first element)
        # so it is actually faster
        intervals.sort(key=lambda e: e[0])

        # merge
        idx = 0
        while idx != len(intervals) - 1:
            first, second = intervals[idx], intervals[idx + 1]
            if first[1] >= second[0]:
                first[1] = max(first[1], second[1])  # necessary, because [1,4] will be sorted before [2,3]
                intervals.pop(idx + 1) # after merge, remove the second element
            else:
                idx += 1
        return intervals


class Solution_B:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Sort first, then connect the two neighbored interval if possible
        This output a new list
        """
        if len(intervals) < 2:
            return intervals

        # sort first
        # this is not python's default sort (because it only comparing first element)
        # so it is actually faster
        intervals.sort(key=lambda e: e[0])

        # merge
        result = [intervals[0]]
        idx = 1
        while idx < len(intervals):
            cur = intervals[idx]
            if result[-1][0] <= cur[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], cur[1])
            else:
                result.append(cur)
            idx += 1
        return result


if __name__ == "__main__":
    testCase = Solution_A()

    lst = []
    assert testCase.merge(lst) == [], "Edge 0"

    lst = [[0, 1]]
    assert testCase.merge(lst) == [[0, 1]], "Edge 1"

    lst = [[1, 3], [2, 6], [8, 10], [15, 18]]
    assert testCase.merge(lst) == [[1, 6], [8, 10], [15, 18]], "Example 1"

    lst = [[15, 18], [1, 3], [8, 10], [2, 6]]
    assert testCase.merge(lst) == [[1, 6], [8, 10], [15, 18]], "Example 1 unsorted"

    lst = [[1, 4], [4, 5]]
    assert testCase.merge(lst) == [[1, 5]], "Example 2"

    print("All passed")
