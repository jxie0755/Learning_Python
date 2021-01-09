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

    def binarySearch(self, nums: List[int], target: int) -> bool:
        """
        Helper
        regular binary search if a value is in sorted list
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
        return False

    def isSortedQuick(self, nums: List[int]) -> bool:
        """
        Helper function specialized for this question
        Quickly tell whether an array is sorted on two condition:
            1. First element < Last Element
            2. If the array has only one repeating elements.
        """
        if len(set(nums)) <= 1:
            return True
        else:
            if nums[0] < nums[-1]:
                return True
            else:
                return False

    def search(self, nums: List[int], target: int) -> bool:
        """
        Recursive method to break the array into two halves:
            - binary search the sorted part
            - Recursive run on the other half
        """
        lo, hi = 0, len(nums) - 1  # index
        mid = (lo + hi) // 2 + 1
        first, second = nums[:mid], nums[mid:]

        A, B = self.isSortedQuick(first), self.isSortedQuick(second)

        if A and B:
            return self.binarySearch(first, target) or self.binarySearch(second, target)
        elif A:
            if self.binarySearch(first, target):
                return True
            else:
                return self.search(second, target)
        elif B:
            if self.binarySearch(second, target):
                return True
            else:
                return self.search(first, target)


class Solution_B:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Regular while loop, binary search O(logN)
        Method modified from Leetcode P033
        This will pass but it is not the preferred method as too many conditions and edge cases
        """
        if not nums:
            return False

        L, H = 0, len(nums) - 1
        while L <= H:
            M = (L + H) // 2
            low, mid, high = nums[L], nums[M], nums[H]
            if L == H:  # means the length of the array is 1
                return low == high == target
            if mid == target:
                return True
            elif low <= target <= mid:  # determine if the first half is sorted
                H = M - 1
            elif mid <= target <= high:  # determine if the second half is sorted
                L = M + 1
            # if target not in sorted sub-array, then it must be in the unsorted sub-array
            # an array can be unsorted in two way:
            # 1 - Truely unsorted sorted (head > tail)
            # 2 - Fake sorted because all elements is the same (can't use head == tail, must confirm with set())
            elif low > mid or len(set(nums[M:H + 1])) == 1:  # if first half is unsorted, then must be in first half
                H = M - 1
            elif mid > high or len(set(nums[L:M + 1])) == 1:  # if second half is unsorted, then must be in first half
                L = M + 1
            else:
                return target in nums[L:H + 1]


class Solution_C:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Use a pure binary search helper.
        Find mid index as M. Compare mid element with head and tail

        Clearer logic with 3 possible situations:
        1. Looks like sorted, but actually not. Recursive run the same test on both section
        2. Run recursive search in unsorted section (first section) and pure binary search in the sorted (second section)
        3. Run pure binary search in sorted section (first section) and recursive search in the unsorted (second section)

        """
        if len(nums) <= 2:
            # when it comes down to less than two elements, just directly check
            # To avoid infinite cut of M betwen L and H
            return target in nums
        else:
            L = 0
            H = len(nums) - 1
            M = (L + H) // 2
            Lo = nums[L]
            Hi = nums[H]
            Mid = nums[M]
            if Lo <= Mid <= Hi:
                return self.search(nums[L:M], target) or self.search(nums[M:], target)
            elif Lo > Mid and Mid <= Hi:
                return self.search(nums[L:M], target) or self.binarysearch(nums[M:], target)
            elif Lo <= Mid and Mid > Hi:
                return self.binarysearch(nums[L:M + 1], target) or self.search(nums[M + 1:], target)

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
    testCase = Solution_C()
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
