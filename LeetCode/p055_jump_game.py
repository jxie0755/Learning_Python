"""
https://leetcode.com/problems/jump-game/
P055 Jump Game
Medium

Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
"""

from typing import *


class Solution:

    def canJump(self, nums: List[int]) -> bool:
        """
        Version A
        Use a helper to find next idx based on current index, as long as it was able to move forward
        """

        def findNext(cur_idx):
            cur_val = nums[cur_idx]
            next_idx, next_val = 0, 0
            for idx in range(cur_idx + 1, cur_idx + cur_val + 1):
                idx_val = nums[idx]
                if idx + idx_val > next_idx + next_val:
                    next_idx, next_val = idx, idx_val
            return next_idx

        cur_idx, cur_val = 0, nums[0]
        last_idx = len(nums) - 1

        if len(nums) == 1 or 0 not in nums:
            return True

        while cur_val < last_idx - cur_idx:
            cur_idx = findNext(cur_idx)
            cur_val = nums[cur_idx]
            if cur_idx == 0:
                return False

        return True


class Solution(object):

    def canJump(self, nums: List[int]) -> bool:
        """
        STD ans
        """

        max_reachable_idx = 0  # 定义一个当前能走到的最远的位置

        for i, length in enumerate(nums):
            if i > max_reachable_idx:
                return False  # 如果到了一个idx, 发现之前最远idx都走不到这,就表示走不通
            max_reachable_idx = max(max_reachable_idx, i + length)  # 对每个idx检查, 保留最大值

        return True


if __name__ == "__main__":
    assert Solution().canJump([0]), "Edge 1"
    assert not Solution().canJump([0, 0]), "Edge 2"
    assert Solution().canJump([1, 0]), "Edge 3"
    assert not Solution().canJump([1, 0, 0, 0]), "Edge 4"

    assert Solution().canJump([2, 3, 1, 1, 4]), "Example 1"
    assert not Solution().canJump([3, 2, 1, 0, 4]), "Example 2"

    print("all passed")
