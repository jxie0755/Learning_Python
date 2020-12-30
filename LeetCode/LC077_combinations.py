"""
https://leetcode.com/problems/combinations/
P077 Combinations
Medium

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
"""

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
        The method is not naturally returning sorted, but each combination group is sorted
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
            tail = next_list.pop()
            result += self.combinationSolo(nums[:len(nums)-1], k) + [com + [tail] for com in self.combinationSolo(next_list, k - 1)]
            return result

class Solution_A2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Direct version of A1, without helper, but the sequence is reversed
        No need to convert n in to a listm directly use n-1 for recursion
        The method is not naturally returning sorted, but each combination group is sorted
        """
        # this can individually work as a combination of list of elements
        if k == 0:
            return [[]]
        elif k == n:
            return [list(range(1, n + 1))]
        elif k == 1:
            return [[i] for i in range(1, n+1)]
        else:
            return self.combine(n - 1, k) + [com + [n] for com in self.combine(n - 1, k - 1)]


print(Solution_A1().combine(5, 3))


if __name__ == "__main__":
    testCase = Solution_A1()

    assert testCase.combine(1, 1) == [
        [1]
    ], "Edge 1"

    assert testCase.combine(4, 4) == [
        [1, 2, 3, 4]
    ], "Edge 2"

    assert sorted([sorted(i) for i in testCase.combine(5, 3)]) == [
        [1, 2, 3],
        [1, 2, 4],
        [1, 2, 5],
        [1, 3, 4],
        [1, 3, 5],
        [1, 4, 5],
        [2, 3, 4],
        [2, 3, 5],
        [2, 4, 5],
        [3, 4, 5]
    ]

    print("all passed")
