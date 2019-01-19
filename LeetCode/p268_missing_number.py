# P268 Missing Number
# Easy


# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Note:
# Your algorithm should run in linear runtime complexity.  # Means no sorting used!!
# Could you implement it using only constant extra space complexity?


class Solution:
    def missingNumber(self, nums):
        ### 利用等差数列? 过一遍找出首项和末项 (min和max)
        ### 然后长度+1, 补位, 计算等差数列之和, 与实际之和相比的差值就是missing number
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_all, length, min_v, max_v = 0, len(nums), float('inf'), -float('inf')

        for i in nums:
            sum_all += i
            if i < min_v:
                min_v = i
            if i > max_v:
                max_v = i

        if min_v != 0:  # 最左边缺0
            return 0
        elif max_v == length -1:  # 最右边缺最后一个数
            return max_v + 1
        else:   # 在中间, 利用等差数列求差
            return (0 + max_v) * (length+1) // 2 - sum_all


class Solution:
    def missingNumber(self, nums):
        ### XOR method, O(N)

        """
        :type nums: List[int]
        :rtype: int
        """
        checker = 0
        for n in (nums + list(range(len(nums)+1))):
                # 也就是 nums 与真正应该的nums 一起
            checker ^= n  # iteration完毕就能得到缺失的数字,不论顺序
        return checker


# Learn XOR
# The operation of xor is commutative and associative.
# Two common property:
# 1. A ^ B = B^A
# 2. (A ^ B) ^ C = A ^ (B ^ C).
# 3. 0 ^ n = n
# Therefore, A^C^B^A^C = A^A^C^C^B = B.
# So for this code, the order of the numbers does not matter at all.



if __name__ == '__main__':
    assert Solution().missingNumber([0]) == 1, 'Edge 1'
    assert Solution().missingNumber([1]) == 0, 'Edge 2'
    assert Solution().missingNumber([0, 1]) == 2, 'Edge 3'
    assert Solution().missingNumber([1, 2, 3]) == 0, 'Edge 4'

    assert Solution().missingNumber([3,0,1]) == 2, 'Example 1'
    assert Solution().missingNumber([9,6,4,2,3,5,7,0,1]) == 8, 'Example 2'
    print('all passed')
