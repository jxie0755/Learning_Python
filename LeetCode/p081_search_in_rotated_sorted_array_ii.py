# P081 Search in Rotated Sorted Array II
# Medium


# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
# You are given a target value to search. If found in the array return true, otherwise return false.


# Follow up:
# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# Would this affect the run-time complexity? How and why?

# before: [0,1,2,3,4,5,6] might become [3,4,5,6,0,1,2]).
# now:    [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]


from typing import *


class Solution:
    def binarySearch(self, nums, target):
        """regular binary search in sorted list"""
        lo, high = 0, len(nums) - 1
        while lo <= high:
            mid = (lo + high) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        return False

    def isSortedQuick(self, nums):

        if len(set(nums)) <= 1:
            return True
        else:
            if nums[0] < nums[-1]:
                return True
            else:
                return False

    def search(self, nums: List[int], target: int) -> bool:
        lo, high = 0, len(nums) - 1
        mid = (lo + high) // 2 + 1
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


class Solution:
    # Method modified from Leetcode P033
    def search(self, nums, target):
        # Regular while loop, binary search O(logN)
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums:
            return False

        L, H = 0, len(nums) - 1

        while L <= H:
            M = (L + H) // 2
            low, mid, high = nums[L], nums[M], nums[H]
            print('L', L, 'M', M, 'H', H)
            if L == H:
                return low == target
            if mid == target:
                return True
            if low <= mid and low <= target <= mid:
                H = M - 1
            elif mid <= high and mid <= target <= high:
                L = M + 1

            # if target not in sorted sub-array, then it must be in the unsorted sub-array
            # an array can be sorted in two way:
            # 1 - Truely sorted
            # 2 - Fake sorted because all elements is the same
            # modified the way to tell which half is sorted, considering repeating elements, by excluding situation 2
            elif len(set(nums[L:M+1])) == 1 or low < mid:
                L = M + 1
            elif len(set(nums[M:H+1])) == 1 or mid < high:
                H = M - 1




if __name__ == '__main__':
    nums = [1]
    target = 1
    assert Solution().search(nums, target), 'Edge 1'

    nums = [1, 1]
    target = 1
    assert Solution().search(nums, target), 'Edge 2'

    nums = [3, 1]
    target = 0
    assert not Solution().search(nums, target), 'Edge 3'

    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    assert Solution().search(nums, target), 'Example 1'

    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 3
    assert not Solution().search(nums, target), 'Example 2'

    nums = [1, 3, 1, 1, 1]
    target = 3
    assert Solution().search(nums, target), 'Additional 1'

    print('all passed')
