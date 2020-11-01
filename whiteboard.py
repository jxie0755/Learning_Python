"""
https://leetcode.com/problems/maximum-subarray/
p053 Maximum Subarray
Easy

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
"""

from typing import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pass



if __name__ == "__main__":
    testCase = Solution()
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
    print("all passed")
