# P056 Insert Interval
# Hard



# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
        return f"[{self.start} -> {self.end}]"
    def __eq__(self, other):
        if self.start ==other.start and self.end == other.end:
            return True
        return False


class Solution:
    # From leetcode p056
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x.start)
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            prev, current = result[-1], intervals[i]
            if current.start <= prev.end:
                prev.end = max(prev.end, current.end)
            else:
                result.append(current)
        return result

    # Basically, insert the newInterval into intervals based on start in sorted order, then merge.
    def insert(self, intervals, newInterval):
        i = 0
        inserted = False
        while i != len(intervals):
            if newInterval.start < intervals[0].start:
                intervals.insert(i, newInterval)
                inserted = True
                break
            i += 1
        if not inserted:
            intervals.append(newInterval)

        return self.merge(intervals)




if __name__ == "__main__":
    assert Solution().insert([], Interval(1,2)) == [Interval(1,2)], "Edge 1"


    A1 = Interval(1,3)
    A2 = Interval(6,9)
    lst = [A1, A2]
    assert Solution().insert(lst, Interval(2,5)) == [
        Interval(1,5),
        Interval(6,9)
    ], "Example 1"

    B1 = Interval(1,2)
    B2 = Interval(3,5)
    B3 = Interval(6,7)
    B4 = Interval(8,10)
    B5 = Interval(12,16)
    lst = [B1, B2, B3, B4, B5]
    assert Solution().insert(lst, Interval(4, 8)) == [
        Interval(1, 2),
        Interval(3, 10),
        Interval(12,16)
    ], "Example 2"

    print("all passed")




