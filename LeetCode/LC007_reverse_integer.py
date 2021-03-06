"""
https://leetcode.com/problems/reverse-integer/
p007 Reverse Integer
Easy

Given a 32-bit signed integer, reverse digits of an integer.
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
The 32-bit int data type can hold integer values in the range of -2,147,483,648 to 2,147,483,647 ([-2^31, 2^31-1]).
"""

class Solution_A:
    def reverse(self, x: int) -> int:
        """
        use string method, time O(logN), takes extra space O(logn)
        """
        str_result = str(x)[::-1]

        if x >= 0:
            result = int(str_result)
            return result if result <= 2147483647 else 0
        else:
            result = int("-" + str_result[:-1])
            return result if result >= -2147483648 else 0

class Solution_B:
    def reverse(self, x: int) -> int:
        """
        use math method
        """

        # no extra space used, by using divmod method
        absX = abs(x)
        result = 0
        while absX > 0:
            result = result * 10 + absX % 10
            absX //= 10
        if x < 0:
            result = -result
        return result if 2147483647 > result > -2147483648 else 0


if __name__ == "__main__":
    testCase = Solution_A()
    assert testCase.reverse(123) == 321, "regular"
    assert testCase.reverse(-120) == -21, "tricky reverse"
    assert testCase.reverse(1534236469) == 0, "large number"
    assert testCase.reverse(0) == 0, "zero"
    print("All passed")
