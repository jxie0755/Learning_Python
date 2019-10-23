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

class Solution_B:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        O(n), using local and global max_value to iterate over the elements
        """
        nonePositive = True

        global_max, local_max = 0, 0
        for i in nums:
            if i > 0:
                nonePositive = False
            local_max = max(0, local_max + i)
            global_max = max(global_max, local_max)

        if nonePositive:
            return max(nums)
        else:
            return global_max


if __name__ == "__main__":
    testMethod = Solution_B().maxSubArray
    assert testMethod([1, 2, 3, 4]) == 10, "All positives"
    assert testMethod([-1, -2, -3, -4]) == -1, "All negatives"
    assert testMethod([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, "mixed positive and negative"
    assert testMethod([2, 2, 0, -1]) == 4, "with zero"
    assert testMethod([-2, -1, -1, -1, -1, -1, -1, -1, 1]) == 1, "a lot of negatives"
    assert testMethod([0, 0, -3, 1]) == 1, "group of zeros"
    assert testMethod([1]) == 1, "just 1"
    assert testMethod([-1]) == -1, "just -1"
    assert testMethod([0]) == 0, "just 0"
    assert testMethod([0, -1, -1, 0, 0, 0, -1, -2, -3]) == 0, "only one zero"
    assert testMethod([0, 0, 0, 0, 0, 0]) == 0, "all zeros"
    print("all passed")
