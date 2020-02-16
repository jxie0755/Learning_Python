"""
https://leetcode.com/problems/partition-equal-subset-sum/
P416 Partition Equal Subset Sum
Medium

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
    Each of the array element will not exceed 100.
    The array size will not exceed 200.
"""

from typing import *

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        pass


if __name__ == '__main__':
    testCase = Solution()
    assert not testCase.canPartition([1]), "Edge 1"
    assert not testCase.canPartition([1,2]), "Edge 2"
    assert testCase.canPartition([2,2]), "Edge 3"

    assert testCase.canPartition([1,5,11,5]), "Example 1"
    assert not testCase.canPartition([1,2,3,5]), "Example 2"

    assert testCase.canPartition([1,2,3]), "Additional 1"

