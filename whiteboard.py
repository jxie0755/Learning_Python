"""
https://leetcode.com/problems/trapping-rain-water/
P042 Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
"""

from typing import *


class Solution:
    def trap(self, height: List[int]) -> int:

        volume = 0

        def find_max_idx(start: int, end: int):
            """Helper A: find out the max idx in idx range"""
            max_so_far = -1
            max_idx = -1
            for i in range(start, end + 1):
                if height[i] > max_so_far:
                    max_so_far = height[i]
                    max_idx = i
            return max_idx

        def trap_helper(start: int, end: int, cur_max_idx):
            """
            Helper B: recursively calcualte the volume between two peaks
            this can go two directsions:
                if the new max idx < pre_max_i, means sweeping to head
                if the new max idx > pre_max_i, means sweeping to end

            """
            nonlocal volume
            if end - start < 1:
                pass
            else:
                new_max_idx = find_max_idx(start, end)
                if new_max_idx < cur_max_idx:
                    for i in range(new_max_idx, cur_max_idx):
                        volume += (height[new_max_idx] - height[i])
                    trap_helper(0, new_max_idx - 1, new_max_idx)  # sweeping to head
                else:
                    for i in range(cur_max_idx + 1, new_max_idx):
                        volume += (height[new_max_idx] - height[i])
                    trap_helper(new_max_idx + 1, len(height) - 1, new_max_idx)  # sweeping to end

        peak_idx = find_max_idx(0, len(height) - 1) # first locate the max peak idx
        trap_helper(0, peak_idx - 1, peak_idx)  # find everything before max_idx
        trap_helper(peak_idx + 1, len(height) - 1, peak_idx) # find everything after max_idx

        return volume


if __name__ == "__main__":
    testCase = Solution()
    assert testCase.trap([]) == 0, "Edge 1"
    assert testCase.trap([0]) == 0, "Edge 2"
    assert testCase.trap([1]) == 0, "Edge 3"
    assert testCase.trap([1, 1]) == 0, "Edge 4"
    assert testCase.trap([2, 2, 2]) == 0, "Edge 5"
    assert testCase.trap([2, 0, 2]) == 2, "Edge 6"

    assert testCase.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6, "Example 1"
    assert testCase.trap([10, 1, 2, 1, 2, 1, 10]) == 43, "Example 2"
    assert testCase.trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6]) == 23, "Example 3"
    assert testCase.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6, "Extra 1"
    assert testCase.trap([8, 5, 4, 1, 8, 9, 3, 0, 0]) ==14, "Extra 2"
    print("all passed")
