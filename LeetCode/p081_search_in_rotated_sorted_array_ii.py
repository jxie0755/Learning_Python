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
        lo, high = 0, len(nums)-1
        while lo <= high:
            mid = (lo + high) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                high = mid -1
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
        lo, high = 0, len(nums) -1
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

    print('all passed')
