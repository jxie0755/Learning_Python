"""
https://leetcode.com/problems/first-missing-positive/
P041 First Missing Positive
Hard

Given an unsorted integer array, find the smallest missing positive integer.

Note:
Your algorithm should run in O(n) time and uses constant extra space.
"""

from typing import *


class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Version A
        O(N), space O(N) (not constant space)
        """

        if not nums:
            return 1
        all_int = list(range(1, len(nums) + 1))
        for i in nums:
            try:
                all_int.remove(i)
            except ValueError:
                pass
        if not all_int:
            return len(nums) + 1
        else:
            return all_int[0]

    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        STD ans
        Avoid use try except block
        """

        nums.append(0)
        n = len(nums)

        for i in range(n):  # delete those useless elements
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0

        for i in range(len(nums)):  # use the index as the hash to record the frequency of each number
            nums[nums[i] % n] += n  # 在每个数上加n, 则不会改变这个数%n的余数

        for i in range(0, len(nums)):
            if nums[i] / n == 0:
                return i
        return n


if __name__ == "__main__":
    assert Solution().firstMissingPositive([]) == 1, "Edge 1"
    assert Solution().firstMissingPositive([1]) == 2, "Edge 2"
    assert Solution().firstMissingPositive([2]) == 1, "Edge 3"
    assert Solution().firstMissingPositive([-1]) == 1, "Edge 4"

    assert Solution().firstMissingPositive([1, 2, 0]) == 3, "Example 1"
    assert Solution().firstMissingPositive([3, 4, -1, 1]) == 2, "Example 2"
    assert Solution().firstMissingPositive([7, 8, 9, 11, 12]) == 1, "Example 3"

    print("all passed")
