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


class Solution_A:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Add the new interval to the intervals at the end and let it merge
        Merge process will automatically sort and merge
        This could be slow as the sorting is complicated
        """
        return self.merge(intervals + [newInterval])

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Helper A from leetcode P056
        """
        if len(intervals) < 2:
            return intervals

        intervals.sort()
        i = 0
        while i != len(intervals) - 1:
            first, second = intervals[i], intervals[i + 1]
            if first[1] >= second[0]:
                first[1] = max(first[1], second[1])
                intervals.pop(i + 1)
            else:
                i += 1
        return intervals


class Solution_B:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Insert the intervals only according to the first element, so that intervals is still sorted
        Then merge like LC056
        """
        idx = 0
        while idx < len(intervals):
            cur = intervals[idx]
            if newInterval[0] <= cur[0]:
                intervals.insert(idx, newInterval)
                break
            else:
                idx += 1
        else:
            intervals.append(newInterval)

        return self.merge(intervals)


    def merge(self, intervals):
        """
        Helper B modified from leetcode LC056
        intervals already sorted
        """
        if len(intervals) < 2:
            return intervals

        # sorting no longer needed
        # intervals.sort(key=lambda e: e[0])

        idx = 0
        while idx != len(intervals) - 1:
            first, second = intervals[idx], intervals[idx + 1]
            if first[1] >= second[0]:
                first[1] = max(first[1], second[1])
                intervals.pop(idx + 1)
            else:
                idx += 1
        return intervals



if __name__ == "__main__":
    testCase = Solution_B()
    assert testCase.insert([], [1, 2]) == [[1, 2]], "Edge 1"

    assert testCase.insert([[1,5]], [1, 2]) == [[1, 5]], "Edge 2"

    assert testCase.insert([[1,5]], [2, 7]) == [[1, 7]], "Edge 3"

    lst = [[1, 3], [6, 9]]
    assert testCase.insert(lst,[2, 5]) == [
        [1, 5],
        [6, 9]
    ], "Example 1"

    lst = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    assert testCase.insert(lst, [4, 8]) == [
        [1, 2],
        [3, 10],
        [12, 16]
    ], "Example 2"


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
    assert testCase.insert(lst, [11, 12]) == [[1, 4], [7, 10], [11, 12]], "Extra 10"

    print("all passed")
