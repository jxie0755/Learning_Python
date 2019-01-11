# P033 Find First and Last Positions of Element in Sorted Array
# Medium


# Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1]


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pass







if __name__ == '__main__':



    assert Solution().searchRange([5,7,7,8,8,10], 8) == [3,4], 'Example 1'
    assert Solution().searchRange([5,7,7,8,8,10], 6) == [-1,-1], 'Example 2'

    print('all passed')
