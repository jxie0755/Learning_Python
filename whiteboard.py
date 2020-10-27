"""
https://leetcode.com/problems/powx-n/
P050 Pow(x, n)
Medium

Implement pow(x, n), which calculates x raised to the power n (x^n)
Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
"""

import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        pass


# if __name__ == "__main__":
#     testCase = Solution()
#     assert testCase.myPow(2.00000, 10) == math.pow(2.00000, 10), "Example 1"
#     assert testCase.myPow(2.10000, 3) == math.pow(2.10000, 3), "Example 2"
#     assert testCase.myPow(2.00000, -2) == math.pow(2.00000, -2), "Example 3"
#     assert testCase.myPow(0.00001, 2147483647) == math.pow(0.00001, 2147483647), "Large 1"
#     print(testCase.myPow(2, -2147483648))
#     print("all passed")


print(math.pow(2,10))
