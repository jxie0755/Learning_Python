"""
https://leetcode.com/problems/combinations/
P077 Combinations
Medium

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
"""

import itertools
from typing import *

class Solution_A1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Convert the n into an actual list, then use a helper to recursive run on the list
        """
        nums = list(range(1, n + 1))
        return self.combinationSolo(nums, k)

    def combinationSolo(self, nums: List[int], k: int) -> List[List[int]]:
        """
        Helper for A1
        Change the paramter type from n to list(range(1, n+1))
        """
        if k == 0:
            return [[]]
        elif k == len(nums):
            return [nums]
        elif k == 1:
            return [[i] for i in nums]
        else:
            result = []
            next_list = nums[:]
            head = next_list.pop(0)
            result += [[head] + com for com in self.combinationSolo(next_list, k - 1)] + self.combinationSolo(nums[1:], k)
            return result

class Solution_A2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Direct version of A1, without helper, but the sequence is reversed
        It will still pass Leetcode, and it contains the full combinations
        """
        # this can individually work as a combination of list of elements
        if k == 0:
            return [[]]
        elif k == n:
            return [list(range(1, n + 1))]
        elif k == 1:
            return [[i] for i in range(1, n+1)]
        else:
            return [[n] + com for com in self.combine(n - 1, k - 1)] + self.combine(n-1, k)


if __name__ == "__main__":
    testCase = Solution_A1()

    assert testCase.combine(1, 1) == [
        [1]
    ], "Edge 1"

    assert testCase.combine(4, 4) == [
        [1, 2, 3, 4]
    ], "Edge 2"

    assert sorted([sorted(i) for i in testCase.combine(5, 3)]) == sorted([list(i) for i in itertools.combinations([1, 2, 3, 4, 5], 3)])

    print("all passed")
