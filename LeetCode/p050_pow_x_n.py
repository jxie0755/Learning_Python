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
        elif n < 0:
            return 1 / self.myPow(x, -n)
        else:
            result = 1.0
            for i in range(n):  # 这里遍历太多了
                result *= x
            return result

class Solution_B:
    def myPow(self, x: float, n: int) -> float:
        """
        Recursive
        利用n每翻倍一次, 只是原数平方一次
        """
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        else:
            v = self.myPow(x, n // 2)  # 这里利用变量只算一次,避免树形递归
            if n % 2 == 0:
                return v * v
            else:
                return v * v * x


if __name__ == "__main__":
    testMethod = Solution_B().myPow
    assert testMethod(2.00000, 10) == math.pow(2.00000, 10), "Example 1"
    assert testMethod(2.10000, 3) == math.pow(2.10000, 3), "Example 2"
    assert testMethod(2.00000, -2) == math.pow(2.00000, -2), "Example 3"
    assert testMethod(0.00001, 2147483647) == math.pow(0.00001, 2147483647), "Large 1"
    print(testMethod(2, -2147483648))
    print("all passed")
