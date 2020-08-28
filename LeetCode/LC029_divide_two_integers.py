"""
https://leetcode.com/problems/divide-two-integers/
P029 Divide Two Integers
Medium

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Note:
    Both dividend and divisor will be 32-bit signed integers.
    The divisor will never be 0.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 2^31 − 1 when the division result overflows.
"""

class Solution_A1:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Integer method
        Time:  O(logn) = O(1), Space: O(1)
        """

        result = 0
        son, mom = abs(dividend), abs(divisor)

        while son != 0 and son >= mom:

            quotient = 1
            while son - mom > mom: # 不断内循环迭代求商值
                mom += mom
                quotient += quotient

            son = son - mom  # 更新余下的分子
            mom = abs(divisor)  # 分母重回原值
            result += quotient  # 结果累加商值

        if dividend * divisor < 0:
            result *= -1

        if result >= 2147483648:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        else:
            return result

class Solution_A2:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Recursive version of Solution A1
        不断翻倍商,直到马上溢出.
        然后对余值递归,直到abs(分母)<=abs(分子)
        """

        son = abs(dividend)
        mom = abs(divisor)
        prefix = 1 if dividend * divisor >= 0 else -1  # 这里确定答案正负性

        if son < mom:
            return 0
        elif son == mom:
            return prefix
        else:
            quotient = 1
            while son - mom > mom:
                mom *= 2
                quotient *= 2

            new_son = son - mom  # 准备余下来的分子,继续递归求解

            # 注意,为了避免多次递归求商时反复正负性叠加,递归时把各商绝对值累加后只测一次正负性
            result = prefix * (quotient + abs(self.divide(new_son, divisor)))

            # 规避Integer溢出
            if result < -2147483648:
                return -2147483648
            elif result > 2147483647:
                return 2147483647
            else:
                return result

class Solution_C:

    def divide(self, dividend: int, divisor: int) -> int:
        """
        Same idea as Solution A but use bit calculation << and >>
        """
        positive = (dividend < 0) is (divisor < 0)  # great way to align two integer on the same sideK
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)





if __name__ == "__main__":
    testCase = Solution_A1()
    assert testCase.divide(1, 3) == 0, "Edge 1"

    assert testCase.divide(10, 3) == 3, "Example 1"
    assert testCase.divide(7, -3) == -2, "Example 2"
    assert testCase.divide(1, 1) == 1, "Example 3"

    assert testCase.divide(-2147483648, 1) == -2147483648, "Long 1"
    assert testCase.divide(-2147483648, -1) == 2147483647, "Long 2"
    assert testCase.divide(-2147483648, -3) == 715827882, "Long 3"

    print("all passed")
