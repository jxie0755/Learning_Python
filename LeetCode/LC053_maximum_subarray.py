"""
https://leetcode.com/problems/maximum-subarray/
p053 Maximum Subarray
Easy

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
"""

from typing import *


class Solution_A:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        O(n^2), Time Limit Exceeded, for large input size
        """
        result = []
        for length in range(1, len(nums) + 1):
            for start in range(0, len(nums) - length + 1):
                result.append(sum(nums[start:start + length]))
        return max(result)


class Solution_STD:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        O(n), using local and global max_value to iterate over the elements
        This won't work for all negatives, so add a check-flag for screening.
        """
        nonePositive = True

        global_max, local_max = 0, 0
        for i in nums:
            if i > 0:  # check-flag
                nonePositive = False

            local_max = max(0, local_max + i)
            # here we lock local to be at least >= 0, so if temporarily drop because of a neg number, it continues
            # it will only be reset to 0 if completely goes < 0

            global_max = max(global_max, local_max)
            # here we record global_max in case local max start to drop

        if nonePositive:
            return max(nums)  # this will save the time to iterate all if `nonePositive -= False`
        else:
            return global_max


if __name__ == "__main__":
    testCase = Solution_STD()
    assert testCase.maxSubArray([1, 2, 3, 4]) == 10, "All positives"
    assert testCase.maxSubArray([-1, -2, -3, -4]) == -1, "All negatives"
    assert testCase.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, "mixed positive and negative"
    assert testCase.maxSubArray([2, 2, 0, -1]) == 4, "with zero"
    assert testCase.maxSubArray([-2, -1, -1, -1, -1, -1, -1, -1, 1]) == 1, "a lot of negatives"
    assert testCase.maxSubArray([0, 0, -3, 1]) == 1, "group of zeros"
    assert testCase.maxSubArray([1]) == 1, "just 1"
    assert testCase.maxSubArray([-1]) == -1, "just -1"
    assert testCase.maxSubArray([0]) == 0, "just 0"
    assert testCase.maxSubArray([0, -1, -1, 0, 0, 0, -1, -2, -3]) == 0, "only one zero"
    assert testCase.maxSubArray([0, 0, 0, 0, 0, 0]) == 0, "all zeros"
    assert testCase.maxSubArray([1, 2, 3, -8, 2, 3, 4, -2, 9, -8, 9, -8, -7, -6]) == 17, "extra"
    print("all passed")
