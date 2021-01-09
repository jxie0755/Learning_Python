"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
P081 Search in Rotated Sorted Array II
Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
You are given a target value to search. If found in the array return true, otherwise return false.

Follow up:
This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

before: [0,1,2,3,4,5,6] might become [3,4,5,6,0,1,2]).
now:    [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]
"""

from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Use a pure binary search helper.
        Find mid index as M. Compare mid element with head and tail

        Three possible situations:
        1. Looks like sorted, but actually not. Recursive run the same test on both section
        2. Run recursive search in unsorted section (first section) and pure binary search in the sorted (second section)
        3. Run pure binary search in sorted section (first section) and recursive search in the unsorted (second section)

        """
        if len(nums) <= 2:
            return target in nums
        else:
            L = 0
            H = len(nums) - 1
            M = (L + H)//2
            Lo = nums[L]
            Hi = nums[H]
            Mid = nums[M]
            if Lo <= Mid <= Hi:
                return self.search(nums[L:M], target) or self.search(nums[M:], target)
            elif Lo > Mid and Mid <= Hi:
                return self.search(nums[L:M], target) or self.binarysearch(nums[M:], target)
            elif Lo <= Mid and Mid > Hi:
                return self.binarysearch(nums[L:M+1], target) or self.search(nums[M+1:], target)


    def binarysearch(self, nums: List[int], target: int) -> bool:
        """
        Binary search in sorted array
        """
        L = 0
        H = len(nums) - 1
        while L <= H:
            M = (L + H) // 2
            if nums[M] == target:
                return True
            elif nums[M] < target:
                L = M + 1
            else:
                H = M - 1
        return False




if __name__ == "__main__":
    testCase = Solution()
    assert testCase.search([1], 1), "Edge 1"
    assert testCase.search([1, 1], 1), "Edge 2"
    assert not testCase.search([3, 1], 0), "Edge 3"
    assert testCase.search([2, 5, 6, 0, 0, 1, 2], 0), "Example 1"
    assert not testCase.search([2, 5, 6, 0, 0, 1, 2], 3), "Example 2"
    assert testCase.search([1, 3, 1, 1, 1], 3), "Additional 1"
    assert testCase.search([3, 1], 1), "Additional 2"
    assert not testCase.search([1, 3, 5], 0), "Additional 3"
    assert not testCase.search([0, 1, 2, 3, 3, 3], 4), "Additional 4"
    print("all passed")
