"""
https://leetcode.com/problems/sqrtx/
p069 Sqrt(x)
Easy

Implement int sqrt(int x).
 Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
"""

class Solution_A1:
    def mySqrt(self, x: int) -> int:
        """
        Binary search
        DO not use the straight high-low method, because it will return float number incorrectly to be integerized.
        Handle the integer method from the begining
        """
        high, low = x, 1
        temp_result = (high + low) / 2
        while abs(temp_result ** 2 - x) >= 1:
            if temp_result ** 2 > x:
                high = temp_result
            elif temp_result ** 2 < x:
                low = temp_result

            temp_result = (high + low) / 2

        temp_result = int(temp_result)
        if (temp_result + 1) ** 2 > x:
            return temp_result
        else:
            return temp_result + 1

class Solution_A2:
    def mySqrt(self, x: int) -> int:
        """
        A modified binary search
        """
        lo = 0
        hi = x
        while True:
            mid = (lo + hi) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):  # (mid + 1)^2 will exceed x, to round back to integer
                return mid
            else:
                if mid * mid < x:
                    lo = mid + 1
                elif mid * mid > x:
                    hi = mid - 1

class Solution_Cheat:
    def mySqrt(self, x):
        """Cheating by use python internal function"""
        return int(x ** 0.5)


if __name__ == "__main__":
    testCase = Solution_A2()
    assert testCase.mySqrt(0) == 0, "Zero"
    assert testCase.mySqrt(1) == 1, "One"
    assert testCase.mySqrt(4) == 2, "Four"
    assert testCase.mySqrt(8) == 2, "Eight"
    assert testCase.mySqrt(36) == 6, "Thirty Six"
    assert testCase.mySqrt(2147395601) == 46340, "Long"
    print("All passed")
