# P268 Missing Number
# Easy


# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Note:
# Your algorithm should run in linear runtime complexity.  # Means no sorting used!!
# Could you implement it using only constant extra space complexity?


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pass




if __name__ == '__main__':
    assert Solution().missingNumber([3,0,1]) == 2, 'Example 1'
    assert Solution().missingNumber([9,6,4,2,3,5,7,0,1]) == 8, 'Example 2'
    print('all passed')

