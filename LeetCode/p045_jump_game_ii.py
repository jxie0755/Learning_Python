# P045 Jump Game II
# Hard


# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.

# Note:
# You can assume that you can always reach the last index.
from typing import *

class Solution:
    ### Simple Recursion method that worked but exceed max time limit
    def jump(self, nums: List[int]) -> int:

        def helper(cur_idx, cur_step=0):

            if cur_idx >= last_idx:
                all_ways.append(cur_step)
            else:
                cur_value = nums[cur_idx]
                if cur_value != 0:
                    for i in range(1, cur_value+1):
                        helper(cur_idx + i, cur_step + 1)

        last_idx = len(nums) - 1
        all_ways = []
        helper(0)
        return min(all_ways)


class Solution:
    ### A modified method with hashmap search to reduce repeating calculation
    ### Use memorization method
    def jump(self, nums: List[int]) -> int:

        def helper(cur_idx, cur_step=0):
            cur_value = nums[cur_idx]
            if cur_value >= last_idx - cur_idx:  # further optimize by checking if currently direct jump the the end is possible
                all_ways.append(cur_step + 1)

            elif cur_step < hmp[cur_idx]:
                hmp[cur_idx] = cur_step
                for i in range(1, cur_value+1):
                    helper(cur_idx + i, cur_step + 1)


        hmp = {i: float("inf") for i in range(len(nums))}
        last_idx = len(nums) - 1
        all_ways = []
        if len(nums) == 1:
            return 0
        helper(0)
        return min(all_ways)

class Solution:
    ### Give up on recursion, new method
    def jump(self, nums: List[int]) -> int:

        def find_next_idx(cur_idx):
            cur_value = nums[cur_idx]
            next_idx, next_value = 0, 0
            for idx in range(cur_idx + 1, cur_idx + cur_value + 1):
                idx_value = nums[idx]
                if idx + idx_value >= next_idx + next_value:
                    next_idx, next_value = idx, idx_value
            return next_idx

        if len(nums) == 1:
            return 0

        last_idx = len(nums) - 1
        cur_idx = 0
        cur_value = nums[cur_idx]
        count = 0
        while cur_value < last_idx - cur_idx:
            cur_idx = find_next_idx(cur_idx)
            cur_value = nums[cur_idx]
            count += 1

        return count + 1



if __name__ == '__main__':
    assert Solution().jump([2,1]) == 1, 'Edge 1'
    assert Solution().jump([2,3,1,1,4]) == 2, "Example 1"
    assert Solution().jump([2,9,6,5,7,0,7,2,7,9,3,2,2,5,7,8,1,6,6,6,3,5,2,2,6,3]) == 5, "Long 1"
    assert Solution().jump([5,6,5,3,9,8,3,1,2,8,2,4,8,3,9,1,0,9,4,6,5,9,8,7,4,2,1,0,2]) == 5, "Long 2"
    assert Solution().jump([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]) == 5, "Long 3"
    print('all passed')
