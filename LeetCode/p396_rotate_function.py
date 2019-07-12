# P396 Rotate Function
# Medium

# Given an array of integers A and let n to be its length.

# Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:

# F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].
# Calculate the maximum value of F(0), F(1), ..., F(n-1).

# Note:
# n is guaranteed to be less than 105.

from typing import *

class Solution:

    # Version A1, math method
    # rotate 数字也就是rotate n, 假设n往后rotate, 每次变化都应该是起始F(n-1) - sum(lst[1:]) + lst[0]* (len(lst)-(n-1))
    # Somehow this will exceed max time limit
    def maxRotateFunction(self, A: List[int]) -> int:


        # Then calculate F(0)
        F0 = 0
        for i in range(len(A)):
            F0 += i * A[i]

        max_so_far = F0
        for i in range(1, len(A)):
            F0 = F0 - sum(A[i:]) + A[i-1] * (len(A)-1) - sum(A[:i-1]) # 可能是计算切片需要O(n)操作
            if F0 > max_so_far:
                max_so_far = F0

        return max_so_far

    # Version A2, same as A1, but use total sum by two slice
    # passed quickly
    def maxRotateFunction(self, A: List[int]) -> int:

        # Then calculate F(0)
        F0 = 0
        for i in range(len(A)):
            F0 += i * A[i]

        sumA = sum(A)
        max_so_far = F0
        for i in range(1, len(A)):
            F0 = F0 - sumA + A[i - 1] * len(A)  # 简化计算
            max_so_far = max(max_so_far, F0)

        return max_so_far


if __name__ == "__main__":

    assert Solution().maxRotateFunction([]) == 0, "Edge 0"
    assert Solution().maxRotateFunction([4,3,2,6]) == 26, "Example 1"
    print("all passed")
