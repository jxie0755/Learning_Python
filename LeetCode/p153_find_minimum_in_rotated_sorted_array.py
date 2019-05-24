# P153 Find Minimum in Rotated Sorted Array
# Medium

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# Find the minimum element.
# You may assume no duplicate exists in the array.


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pass


if __name__ == '__main__':
    assert Solution().findMin([1]) == 1, 'Edge 0'
    assert Solution().findMin([3,4,5,1,2]) == 1, 'Example 1'
    assert Solution().findMin([4,5,6,7,0,1,2]) == 0, 'Example 2'

    print('all passed')
