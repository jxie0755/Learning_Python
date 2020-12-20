"""
https://leetcode.com/problems/sqrtx/
p069 Sqrt(x)
Easy

Implement int sqrt(int x).
 Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        pass


if __name__ == "__main__":
    testCase = Solution()
    assert testCase.mySqrt(0) == 0
    assert testCase.mySqrt(1) == 1
    assert testCase.mySqrt(4) == 2
    assert testCase.mySqrt(8) == 2
    assert testCase.mySqrt(36) == 6
    assert testCase.mySqrt(2147395601) == 46340
    print("all passed")
