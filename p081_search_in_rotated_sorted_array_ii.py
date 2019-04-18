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
    def search(self, nums: List[int], target: int) -> bool:
        pass


if __name__ == '__main__':
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    assert Solution().search(nums, target), 'Example 1'

    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 3
    assert not Solution().search(nums, target), 'Example 2'
