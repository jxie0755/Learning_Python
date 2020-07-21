"""
https://leetcode.com/problems/two-sum/
p001 Two Sum
Easy

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

from typing import *

class Solution_A:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        brutal force, slowest
        this is not very optimized as it request for index
        """
        for i in nums:
            index_i = nums.index(i)
            for j in nums[index_i + 1:]:
                if i + j == target:
                    if i != j:
                        return [index_i, nums.index(j)]
                    else:
                        return [index_i, nums.index(i, index_i + 1)]

class Solution_Ab:
    """
    same as version A but fixed by directly using index
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            cur = nums[i]
            for j in range(i+1, len(nums)):
                addon = nums[j]
                if cur + addon == target:
                    return [i, j]



class Solution_B:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """brutal force, check half first"""
        half = target / 2
        if nums.count(half) == 2:
            indexHalf = nums.index(half)
            return [indexHalf, nums.index(half, indexHalf + 1)]
        for i in nums:
            if i != half:
                if target - i in nums:
                    return [nums.index(i), nums.index(target - i)]

class Solution_C:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        The same method in p167 Two Sum II can be used here
        """
        hashtable = {}
        for idx in range(0, len(nums)):
            if nums[idx] not in hashtable:
                hashtable[target - nums[idx]] = idx  # 这里建立一个需要的另一半的数字作为key, 对应的值是当前的idx
            else:
                return [hashtable[nums[idx]], idx]
                # 当到达一个新的idx,如果对应的数字出现在之前建立的字典的key里,也就是找到了match
                # 这样就把那个key的值(也就是第一个idx)找出来,和新的idx配对


if __name__ == "__main__":
    testCase = Solution_C()
    assert testCase.twoSum([11, 2, 7, 15], 9) == [1, 2], "regular"
    assert testCase.twoSum([11, 7, 2, 15], 9) == [1, 2], "regular revert"
    assert testCase.twoSum([3, 3], 6) == [0, 1], "two identical"
    assert testCase.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4], "negative int"
    assert testCase.twoSum([3, 2, 4], 6) == [1, 2], "struggle with 1/2 target"
    print("all passed")
