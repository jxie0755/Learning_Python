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

class Solution_A:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Luo Ye's recursive method, will exceed time limit
        """
        def helper(local_sum: int, global_sum: int, i: int):
            if local_sum < global_sum//2 and i<len(nums) -1:
                return helper(local_sum + nums[i], global_sum, i + 1) or helper(local_sum, global_sum, i + 1)
            elif local_sum == global_sum//2:
                return True
            else:
                return False

        global_sum = sum(nums)
        if global_sum % 2:
            return False
        nums.sort(reverse=True)
        return helper(0, global_sum, 0)


class Solution_STD_A:
    def build_combinations(self, nums: List[int], index: int, sum_: int, target: int) -> bool:
        """
        A helper to build up combinations check
        # TODO: need lo learn why this works
        """
        sum_ += nums[index]

        if sum_ > target:
            return False
        elif sum_ == target:
            return True
        else:
            for a in range(index+1, len(nums)):
                ret = self.build_combinations(nums, a, sum_, target)
                if ret:
                    return True
        return False

    def canPartition(self, nums: List[int]) -> bool:
        """
        A better recursive method
        """
        nums.sort(reverse=True)
        if sum(nums) % 2:
            return False
        else:
            return self.build_combinations(nums, 0, 0, sum(nums)//2)




if __name__ == '__main__':
    testCase = Solution_STD_A()
    assert not testCase.canPartition([1]), "Edge 1"
    assert not testCase.canPartition([1,2]), "Edge 2"
    assert testCase.canPartition([2,2]), "Edge 3"

    assert testCase.canPartition([1,5,11,5]), "Example 1"
    assert not testCase.canPartition([1,2,3,5]), "Example 2"

    assert testCase.canPartition([1,2,3]), "Additional 1"
    assert not testCase.canPartition([1,2,5]), "Additional 2"

    assert not testCase.canPartition([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100]), "Long"

    print('all passed')
