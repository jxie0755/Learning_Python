# P162 Find Peak Element
# Medium


# A peak element is an element that is greater than its neighbors.
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that nums[-1] = nums[n] = -∞.

# Note:
# Your solution should be in logarithmic complexity.


class Solution(object):

    # O(LogN), break into half, and check both sides

    def isPeak(self, lst, i):
        if i == 0:
            return lst[i] > lst[i+1]
        elif i == len(lst)-1:
            return lst[i] > lst[i-1]
        else:
            return lst[i] > lst[i+1] and lst[i] > lst[i-1]

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return 0
        result = []
        def helper(lo, hi):
            """a helper function to find peaks in nums"""
            if not result:
                if self.isPeak(nums, lo):
                    result.append(lo)
                elif self.isPeak(nums, hi):
                    result.append(hi)
                elif lo < hi - 1:
                    mid = (lo + hi) // 2
                    helper(lo, mid)
                    helper(mid+1, hi)

        helper(0, len(nums)-1)
        if result:
            return result[0]


class Solution_2(object):

    ### STD ans (problematic, but will pass fast)
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:  # catched a down slope
                right = mid
            else:
                left = mid + 1
            print('mid', mid, 'left', left, 'right', right)

        return left



if __name__ == '__main__':
    assert Solution().findPeakElement([1]) == 0, 'Edge 1'
    assert Solution().findPeakElement([2,1]) == 0, 'Edge 2'
    assert Solution().findPeakElement([3, 2, 1]) == 0, 'Edge 3'

    assert Solution().findPeakElement([1,2,3,1]) == 2, 'Example 1'

    B = Solution().findPeakElement([1,2,1,3,5,6,4])
    assert B == 1 or B == 5, 'Example 2'

    assert Solution().findPeakElement([1, 2]) == 1, 'Additional 1'
    assert Solution().findPeakElement([1, 2, 3]) == 2, 'Additional 2'

    # STD ans is problematic:
    print(Solution_2().findPeakElement([1, 2, 1, 1, 1, 1, 1, 1, 1, 1]))
    #                                   0  1  2  3  4  5  6  7  8  9
    # it should return 1, but it returned 9, nums[9] is not a true peak.

    print('all passed')
