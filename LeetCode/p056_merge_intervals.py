# P056 Merge Intervals
# Medium

# Given a collection of intervals, merge all overlapping intervals.

# Definition for an interval.


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
        return f'[{self.start} -> {self.end}]'
    def __eq__(self, other):
        if self.start ==other.start and self.end == other.end:
            return True
        return False

class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x:x.start)

        if len(intervals) >= 2:
            i = 0
            while i != len(intervals) - 1:
                first, second = intervals[i], intervals[i+1]
                if first.end >= second.end:
                    intervals.pop(i+1)
                elif first.end >= second.start:
                    first.end = second.end
                    intervals.pop(i+1)
                else:
                    i += 1
        return intervals



if __name__ == '__main__':
    E0 = Interval(0,1)
    lst = [E0]
    assert Solution().merge(lst) == [E0], "Edge 1"


    A1 = Interval(1,3)
    A2 = Interval(2,6)
    A3 = Interval(8,10)
    A4 = Interval(15,18)
    lst = [A1, A2, A3, A4]

    assert Solution().merge(lst) == [
        Interval(1,6),
        Interval(8,10),
        Interval(15,18),
    ], 'Example 1'


    B1 = Interval(1,4)
    B2 = Interval(4,5)
    lst = [B1, B2]
    assert Solution().merge(lst) == [
        Interval(1, 5),
    ], 'Example 2'

    print('all passed')
