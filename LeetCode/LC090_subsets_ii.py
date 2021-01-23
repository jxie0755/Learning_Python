"""
https://leetcode.com/problems/subsets-ii/
P090 Subsets II
Medium


Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
"""

from typing import *


class Solution_A:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        With the help from the combinationSolo from Leetcode P077
        use tuple and set to remove repeat and convert back to list
        """
        result = []
        for i in range(0, len(nums) + 1):
            result += self.combinationSolo(nums, i)
        return result

    def combinationSolo(self, nums: List[int], k: int) -> List[List[int]]:
        """
        Helper for A1, refer to LC077, modify to output in none repeated elements
        """
        nums = sorted(nums)  # make sure the nums is sorted to begin with

        if k == 0:
            return [[]]
        elif k == len(nums):
            return [nums]
        elif k == 1:
            result = []
            for i in nums:
                if [i] not in result:
                    result.append([i])
            return result
        else:
            result = []
            next_list = nums[:]
            tail = next_list.pop()
            result += self.combinationSolo(nums[:len(nums) - 1], k)
            for _ in [com + [tail] for com in self.combinationSolo(next_list, k - 1)]:
                if _ not in result:
                    result.append(_)
            return result

class Solution_B:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        With the help from the combinationSolo from Leetcode P077
        no need to use tuple, direct use list and remove duplicated on the run
        """
        result = []
        for i in range(0, len(nums) + 1):
            result += self.combinationSolo(nums, i)
        return result

    def combinationSolo(self, nums: List[int], k: int) -> List[List[int]]:
        """
        Helper for A1, refer to LC077, modify to output in none repeated elements
        """
        nums = sorted(nums)  # make sure the nums is sorted to begin with

        if k == 0:
            return [[]]
        elif k == len(nums):
            return [nums]
        elif k == 1:
            result = []
            for i in nums:  # remove repeat
                if [i] not in result:
                    result.append([i])
            return result
        else:
            result = []
            next_list = nums[:]
            tail = next_list.pop()
            result += self.combinationSolo(nums[:len(nums) - 1], k) # this must be first to avoid repeat
            # remove repeat
            for _ in [com + [tail] for com in self.combinationSolo(next_list, k - 1)]:
                if _ not in result:
                    result.append(_)
            return result


if __name__ == "__main__":
    testCase = Solution_A()

    assert sorted(testCase.subsetsWithDup([])) == [
        []
    ], "Edge 0"

    assert sorted(testCase.subsetsWithDup([1])) == [
        [],
        [1]
    ], "Edge 1"

    assert sorted(testCase.subsetsWithDup([1, 2])) == [
        [],
        [1],
        [1, 2],
        [2]
    ], "Example 1"

    assert sorted(testCase.subsetsWithDup([1, 2, 2])) == [
        [],
        [1],
        [1, 2],
        [1, 2, 2],
        [2],
        [2, 2]
    ], "Example 2"

    assert sorted(testCase.subsetsWithDup([1, 2, 3])) == [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 3],
        [2],
        [2, 3],
        [3]
    ], "Additional 1"

    assert sorted(testCase.subsetsWithDup([1, 1, 2, 2])) == [
        [],
        [1],
        [1, 1],
        [1, 1, 2],
        [1, 1, 2, 2],
        [1, 2],
        [1, 2, 2],
        [2],
        [2, 2]
    ], "Additional 2"

    assert sorted(testCase.subsetsWithDup([2, 1, 2, 1])) == [
        [],
        [1],
        [1, 1],
        [1, 1, 2],
        [1, 1, 2, 2],
        [1, 2],
        [1, 2, 2],
        [2],
        [2, 2]
    ], "Additional 2 unsorted"

    print(Solution_A().combinationSolo([1,2,2], 2))

    print("All passed")
