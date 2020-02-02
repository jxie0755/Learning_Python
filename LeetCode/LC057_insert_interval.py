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
        insert the new interval at the right location of already sorted intervals
        then skip the sorting and just merge
        """
        i = 0
        while i != len(intervals):
            if newInterval[0] < intervals[i][0]:
                intervals.insert(i, newInterval)
                break
            i += 1
        else:
            intervals.append(newInterval)

        return self.merge(intervals)


    def merge(self, intervals):
        """
        Helper B modified from leetcode p056
        """
        if len(intervals) < 2:
            return intervals
        # intervals.sort()  No need for sorting
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

    lst = [[1, 2], [3, 7], [4, 6], [8, 10], [12, 16]]
    assert testCase.insert(lst, [4, 8]) == [
        [1, 2],
        [3, 10],
        [12, 16]
    ], "Example 2 extended"

    print("all passed")
