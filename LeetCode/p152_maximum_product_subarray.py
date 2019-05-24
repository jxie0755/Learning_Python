# P152 Maximum Product Subarray
# Medium

# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.


class Solution(object):

    ### Version A, brutal force, get all subsequence and find the product
    ### Failed by exceeding max time limit
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = -float('inf')
        for i in range(0, len(nums)):
            for j in range(1, len(nums) - i+1):
                sub = nums[i:i+j]
                product = 1
                for k in sub:
                    product *= k
                if product > result:
                    result = product
        return result



if __name__ == '__main__':
    assert Solution().maxProduct([-2]) == -2, 'Edge 0'

    assert Solution().maxProduct([2,3,-2,4]) == 6, 'Example 1'
    assert Solution().maxProduct([-2,0,-1]) == 0, 'Example 2'

    print('all passed')
