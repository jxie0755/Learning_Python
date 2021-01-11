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


class Solution_A1:
    def jump(self, nums: List[int]) -> int:
        """
        Simple Recursion method, full iteration
        This will calcualte total_step of every strategy and return the minimum.
        Exceed max time limit
        """
        def jumpHelper(cur_idx: int, cur_step: int = 0) -> None:
            """Helper A"""
            if cur_idx >= last_idx:
                all_ways.append(cur_step)
            else:
                cur_value = nums[cur_idx]
                for i in range(1, cur_value + 1):
                    jumpHelper(cur_idx + i, cur_step + 1)

        last_idx = len(nums) - 1
        all_ways = []
        jumpHelper(0)
        return min(all_ways)


class Solution_A2:
    def jump(self, nums: List[int]) -> int:
        """
        A modified A1 with hashmap search to reduce repeating calculation
        Use memorization method
        This will still fail by exceed max time limit
        """

        def jumpHelper(cur_idx: int, cur_step: int = 0) -> None:
            """Helper A2"""

            if cur_idx >= last_idx:
                all_ways.append(cur_step)
            else:
                cur_value = nums[cur_idx]
                if cur_step < hmp[cur_idx]:  # only iterate if there is a way to get to this idx with less steps than tested before
                    hmp[cur_idx] = cur_step
                    for i in range(1, cur_value + 1):
                        jumpHelper(cur_idx + i, cur_step + 1)


        if len(nums) == 1:
            return 0

        # set up a hashmap to check the minimum steps that can reach to this idx
        hmp = {i: float("inf") for i in range(len(nums))}

        last_idx = len(nums) - 1
        all_ways = []
        jumpHelper(0)
        return min(all_ways)


class Solution_B:
    def jump(self, nums: List[int]) -> int:
        """
        This is not a dynamic algorithm, there is a definite way to determine next_idx for each step based on cur_idx:
        The next_idx comes from the idx that gives max(next_idx - cur_idx + nums[next_idx])
        """

        if len(nums) <= 1:
            return 0

        count = 0
        last_idx = len(nums) - 1
        cur_idx = 0
        while cur_idx + nums[cur_idx] < last_idx:
            jump_range = nums[cur_idx]
            best_next_idx, best_reach = cur_idx, 0

            # iterate each idx within the jump range to find the best_reach
            for jump_distance in range(1, jump_range + 1):
                can_reach = jump_distance + nums[cur_idx + jump_distance]
                if can_reach >= best_reach:
                    best_next_idx, best_reach = cur_idx + jump_distance, can_reach

            count += 1
            cur_idx = best_next_idx  # jump to this best idx

        return count + 1


class Solution_C:
    def jump(self, nums: List[int]) -> int:
        """
        Recursion method, just to practice recursion
        Very similar idea to Solution B, but slower as it is Recursive.
        """

        if len(nums) == 1:
            return 0
        return self.jumphelpter(nums, 0)

    def jumphelpter(self, nums: List[int], cur_idx: int, count: int = 0) -> int:
        """Helper C2"""

        jump_range = nums[cur_idx]
        if cur_idx + jump_range >= len(nums) - 1:  # end case, this idx can cover to or over last_idx
            return count + 1
        else:
            best_next_idx, best_reach = cur_idx, 0
            for jump_distance in range(1, jump_range + 1):
                can_reach = jump_distance + nums[cur_idx + jump_distance]
                if can_reach >= best_reach:
                    best_next_idx, best_reach = cur_idx + jump_distance, can_reach
            return self.jumphelpter(nums, best_next_idx, count + 1)



if __name__ == "__main__":
    testCase = Solution_C()
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

    print("All passed")
