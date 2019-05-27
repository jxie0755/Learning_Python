# P162 Find Peak Element
# Medium


# A peak element is an element that is greater than its neighbors.
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that nums[-1] = nums[n] = -∞.

# Note:
# Your solution should be in logarithmic complexity.


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pass


if __name__ == '__main__':
    assert Solution().findPeakElement([]) is None, 'Edge'
    assert Solution().findPeakElement([1]) == 1, 'Edge 1'

    assert Solution().findPeakElement([1,2,3,1]) == 2, 'Example 1'

    B = Solution().findPeakElement([1,2,1,3,5,6,4])
    assert B == 1 or B == 5, 'Example 2'

    print('all passed')
