"""
https://leetcode.com/problems/search-insert-position/
p035 Search Insert Position
Easy

Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array
"""

from typing import *

class Solution_A:
    def searchInsert(self, nums: List[int], target: int) -> int:

        """
        Time O(N)
        """

        idx = 0
        while idx < len(nums):
            cur = nums[idx]
            if target > cur:
                idx += 1
            else:
                return idx
        return idx


if __name__ == "__main__":
    testCase = Solution_A()
    assert testCase.searchInsert([], 5) == 0, "Empty"
    assert testCase.searchInsert([1, 3, 5, 6], 5) == 2, "In the list"
    assert testCase.searchInsert([1, 3, 5, 6], 2) == 1, "Not in the list"
    assert testCase.searchInsert([1, 3, 5, 6], 7) == 4, "At the end"
    assert testCase.searchInsert([1, 3, 5, 6], 0) == 0, "At the beginning"
    print("all passed")
