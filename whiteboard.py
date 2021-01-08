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


class Solution_A:
    def search(self, nums: List[int], target: int) -> bool:
        pass


if __name__ == "__main__":
    testCase = Solution_A()
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


