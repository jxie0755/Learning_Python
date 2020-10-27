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


class Solution_A:
    def myPow(self, x: float, n: int) -> float:
        """
        Iteration
        this will fail on large case, exceeding max time limit
        """
        if n == 0:
            return 1
        elif n > 0:
            result = 1.0
            for i in range(n):  # 这里遍历太多了
                result *= x
            return result
        else:
            return 1 / self.myPow(x, -n)


class Solution_B:
    def myPow(self, x: float, n: int) -> float:
        """
        Quick recursive version, with O(LogN) speed
        """
        if n == 0:
            return 1.0
        elif n > 0:
            if n == 1:
                return x
            elif n % 2 == 0:
                return self.myPow(x * x, n // 2)
            else:
                return self.myPow(x * x, n // 2) * x
        else:
            return 1 / self.myPow(x, -n)


if __name__ == "__main__":
    testCase = Solution_B()
    assert testCase.myPow(2.00000, 10) == math.pow(2.00000, 10), "Example 1"
    assert testCase.myPow(2.10000, 3) == math.pow(2.10000, 3), "Example 2"
    assert testCase.myPow(2.00000, -2) == math.pow(2.00000, -2), "Example 3"
    assert testCase.myPow(0.00001, 2147483647) == math.pow(0.00001, 2147483647), "Large 1"
    assert testCase.myPow(2, -2147483648) == math.pow(2, -2147483648), "Large 2"
    print("all passed") # takes a while to pass
