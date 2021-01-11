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
        total_product = 1
        zerofound = 0
        for i in nums:
            if i == 0:
                zerofound += 1
            else:
                total_product *= i

        k = 0
        result = []

        if zerofound == 0:  # no zero
            while k != len(nums):
                result.append(total_product // nums[k])
                k += 1

        elif zerofound == 1:  # 1 zero, everything else is 0 except the i where nums[i] == 0
            for i in nums:
                if i == 0:
                    result.append(total_product)
                else:
                    result.append(0)

        else:  # >= 2 zero, everything is zero
            total_product = 0
            for i in nums:
                result.append(total_product)

        return result


class Solution(object):

    # Version B, O(N) time, No Division (不使用除法)
    # space O(2n)
    # 从左往右, 记录到每个数之前的乘积, 再从右往左, 然后把左侧的乘积乘以右侧的乘积
    # 可以更加省空间到O(N), 使用右侧扫描时结果直接乘到left里面去
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        N = len(nums)
        left, right = [1] * N, [1] * N
        i = 1
        pd = 1
        while i != N:
            pd *= nums[i - 1]
            left[i] = pd
            i += 1

        i = N - 2
        pd = 1
        while i >= 0:
            pd *= nums[i + 1]
            right[i] = pd
            i -= 1

        return [left[i] * right[i] for i in range(len(left))]


if __name__ == "__main__":
    assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6], "Example"
    assert Solution().productExceptSelf([0, 0]) == [0, 0], "Additional 1"
    assert Solution().productExceptSelf([1, 0, 1]) == [0, 1, 0], "Additional 2"

    print("All passed")
