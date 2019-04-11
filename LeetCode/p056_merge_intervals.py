# P056 Merge Intervals
# Medium

# Given a collection of intervals, merge all overlapping intervals.

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        pass



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
        Interval(8, 10),
        Interval(1,18),
    ], 'Example 1'


    B1 = Interval(1,4)
    B2 = Interval(4,5)
    lst = [B1, B2]
    assert Solution().merge(lst) == [
        Interval(1, 5),
    ], 'Example 2'

    print('all passed')
