"""
https://leetcode.com/problems/jump-game/
P055 Jump Game
Medium

Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
"""

from typing import *


class Solution_A:
    def canJump(self, nums: List[int]) -> bool:
        """
        Very similar to LC045 jump game ii, version B
        Add an additional check if can't not find the best_next_idx, directly return False
        """

        last_idx = len(nums) - 1
        cur_idx = 0

        while cur_idx + nums[cur_idx] < last_idx:
            jump_range = nums[cur_idx]
            best_next_idx, best_reach = cur_idx, 0
            for jump_distance in range(1, jump_range + 1):
                can_reach = jump_distance + nums[cur_idx + jump_distance]
                if can_reach >= best_reach:
                    best_next_idx, best_reach = cur_idx + jump_distance, can_reach

            if best_next_idx == cur_idx:  # if after evaluating, the best_next_idx never changed from cur_idx
                return False
            else:
                cur_idx = best_next_idx

        return True


class Solution_STD:

    def canJump(self, nums: List[int]) -> bool:
        max_reachable_idx = 0  # 定义一个当前能走到的最远的位置

        for idx, jump_range in enumerate(nums):  # 利用enum提取idx和对应的nums[idx]
            if idx > max_reachable_idx:
                return False  # 如果到了一个idx, 发现之前最远idx都走不到这,就表示走不通
            max_reachable_idx = max(max_reachable_idx, idx + jump_range)  # 对每个idx检查, 保留最大值

        return True


if __name__ == "__main__":
    testCase = Solution_STD()
    assert testCase.canJump([0]), "Edge 1"
    assert not testCase.canJump([0, 0]), "Edge 2"
    assert testCase.canJump([1, 0]), "Edge 3"
    assert not testCase.canJump([1, 0, 0, 0]), "Edge 4"

    assert testCase.canJump([2, 3, 1, 1, 4]), "Example 1"
    assert not testCase.canJump([3, 2, 1, 0, 4]), "Example 2"

    assert testCase.canJump([3, 2, 5, 0, 1, 0, 0, 0]), "Additional 1"
    assert not testCase.canJump([3, 2, 5, 0, 1, 0, 0, 2, 0, 0, 1]), "Additional 2"

    print("All passed")
