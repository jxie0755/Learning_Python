"""

P078 Subsets
Medium

Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
"""

from typing import *

class Solution_A:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        With the help from the combinationSolo from Leetcode P077
        passed but on the slow side
        """
        result = []
        for i in range(0, len(nums) + 1):
            result += self.combinationSolo(nums, i)
        return result

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

if __name__ == "__main__":
    testCase = Solution_A()

    nums = [1,2]
    assert sorted(testCase.subsets(nums)) == sorted([[],[1],[2],[1,2]])

    nums = [1, 2, 3]
    assert sorted(testCase.subsets(nums)) == sorted([
        [3],
        [1],
        [2],
        [1, 2, 3],
        [1, 3],
        [2, 3],
        [1, 2],
        []
    ])
    print("all passed")
