# P238 Product of Array Except Self
# Medium


# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

from typing import *
class Solution(object):

    # Version A, O(N) time, O(1) space
    # 4 differnt situations:
        # no zero
        # 1 zero
        # >= 2 zeros
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total_product = 1
        zerofound = 0
        for i in nums:
            if i == 0:
                zerofound += 1
            else:
                total_product *= i


        k = 0
        result = []

        if zerofound == 0: # no zero
            while k != len(nums):
                result.append(total_product // nums[k])
                k += 1

        elif zerofound == 1: # 1 zero, everything else is 0 except the i where nums[i] == 0
            for i in nums:
                if i == 0:
                    result.append(total_product)
                else:
                    result.append(0)

        else: # >= 2 zero, everything is zero
            total_product = 0
            for i in nums:
                result.append(total_product)

        return result



if __name__ == '__main__':
    assert Solution().productExceptSelf([1,2,3,4]) == [24,12,8,6], 'Example'
    assert Solution().productExceptSelf([0,0]) == [0,0], 'Additional 1'
    assert Solution().productExceptSelf([1,0,1]) == [0,1,0], 'Additional 2'

    print('all passed')
