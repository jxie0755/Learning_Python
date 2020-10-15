"""
https://leetcode.com/problems/jump-game-ii/
P045 Jump Game II
Hard

Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

Note:
    You can assume that you can always reach the last index.
"""

from typing import *


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        total_jump = 0
        end_idx = len(nums) - 1
        i = 0

        while i + nums[i] < end_idx:
            cur_range = nums[i]
            next_i, max_reach = i, 0
            for jump_distance in range(1, cur_range+1):
                can_reach = jump_distance + nums[i+jump_distance]
                if can_reach >= max_reach:
                    next_i, max_reach = i+jump_distance, can_reach

            total_jump += 1
            i = next_i

        return total_jump + 1



if __name__ == "__main__":
    testCase = Solution()
    assert testCase.jump([0]) == 0, "Edge 0"
    assert testCase.jump([2, 1]) == 1, "Edge 1"
    assert testCase.jump([2, 3, 1, 1, 4]) == 2, "Example 1"
    assert testCase.jump(
        [2, 9, 6, 5, 7, 0, 7, 2, 7, 9, 3, 2, 2, 5, 7, 8, 1, 6, 6, 6, 3, 5, 2, 2, 6, 3]) == 5, "Long 1"
        #   1                       2                 3                 4           5
    assert testCase.jump(
        [5, 6, 5, 3, 9, 8, 3, 1, 2, 8, 2, 4, 8, 3, 9, 1, 0, 9, 4, 6, 5, 9, 8, 7, 4, 2, 1, 0, 2]) == 5, "Long 2"
    assert testCase.jump(
        [5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6, 5, 2, 7, 9, 7,
         9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0, 3, 8, 5]) == 5, "Long 3"
    print("all passed")



