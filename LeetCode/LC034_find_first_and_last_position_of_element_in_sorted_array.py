"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
P033 Find First and Last Positions of Element in Sorted Array
Medium

Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1]
"""

from typing import *

class Solution_A:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        improved binary search
        3 binary search, find catch mid value, and Low/High of the section,
        Then according to mid value and Low/High to find head and tail by 2 additional binary search
        O(LogN), Space O(1)
        """

        L, H = 0, len(nums) - 1
        target_found = False
        # first determine if target is in nums
        while L <= H:
            M = (L + H) // 2
            low, mid, high = nums[L], nums[M], nums[H]

            if mid < target:
                L = M + 1
            elif target < mid:
                H = M - 1
            else:
                target_found = True
                break

        if not target_found:
            return [-1, -1]


        head = tail = M

        # first find head
        while True:
            M = (L + head) // 2

            if nums[L] == target:
                head = L
                break
            elif nums[M] < target:
                L = M + 1
            else:
                head = M
                if nums[M - 1] != target:
                    break


        # second find tail
        while True:
            M = (tail + H) // 2

            if nums[H] == target:
                tail = H
                break
            elif nums[M] > target:
                H = M - 1
            else:
                tail = M
                if nums[M + 1] != target:
                    break

        return [head, tail]


if __name__ == "__main__":
    testCase = Solution_A()
    assert testCase.searchRange([], 0) == [-1, -1], "Edge 1"
    assert testCase.searchRange([8], 8) == [0, 0], "Edge 2"
    assert testCase.searchRange([0], 8) == [-1, -1], "Edge 3"

    assert testCase.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4], "Example 1"
    assert testCase.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1], "Example 2"

    assert testCase.searchRange([5, 7, 7, 7, 8, 10], 8) == [4, 4], "Addtional 1"
    assert testCase.searchRange([5, 7, 7, 7, 8, 10], 7) == [1, 3], "Addtional 2"

    assert testCase.searchRange([1, 4], 4) == [1, 1], "Extra 1"
    assert testCase.searchRange([1, 3], 1) == [0, 0], "Extra 2"
    assert testCase.searchRange([-3, -2, -1], 0) == [-1, -1], "Extra 3"
    assert testCase.searchRange([0, 0, 2, 3, 4, 4, 4, 5], 5) == [7, 7], "Extra 4"
    assert testCase.searchRange([0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 8, 10, 10], 4) == [10,
                                                                                                               13], "Extra 5"
    assert testCase.searchRange([1, 2, 3, 3, 3, 3, 4, 5, 9], 3) == [2, 5], "Extra 6"

    print("all passed")
