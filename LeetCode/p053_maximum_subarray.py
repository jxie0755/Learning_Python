"""
https://leetcode.com/problems/maximum-subarray/
p053 Maximum Subarray
Easy

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
"""

from typing import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Version A
        O(n^2), Time Limit Exceeded, for large input size
        """
        result = []
        for length in range(1, len(nums) + 1):
            for start in range(0, len(nums) - length + 1):
                result.append(sum(nums[start:start + length]))
        return max(result)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Version B
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
    assert Solution().maxSubArray([1, 2, 3, 4]) == 10, "All positives"
    assert Solution().maxSubArray([-1, -2, -3, -4]) == -1, "All negatives"
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, "mixed positive and negative"
    assert Solution().maxSubArray([2, 2, 0, -1]) == 4, "with zero"
    assert Solution().maxSubArray([-2, -1, -1, -1, -1, -1, -1, -1, 1]) == 1, "a lot of negatives"
    assert Solution().maxSubArray([0, 0, -3, 1]) == 1, "group of zeros"
    assert Solution().maxSubArray([1]) == 1, "just 1"
    assert Solution().maxSubArray([-1]) == -1, "just -1"
    assert Solution().maxSubArray([0]) == 0, "just 0"
    assert Solution().maxSubArray([0, -1, -1, 0, 0, 0, -1, -2, -3]) == 0, "only one zero"
    assert Solution().maxSubArray([0, 0, 0, 0, 0, 0]) == 0, "all zeros"
    print("all passed")
