"""
https://leetcode.com/problems/string-to-integer-atoi/
P008 String to Integer (atoi)
Medium


Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed. (Example 4)
If no valid conversion could be performed, a zero value is returned.

Note:
Only the space character " " is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.
"""

import re

class Solution_A:
    def myAtoi(self, str: str) -> int:
        """String method"""
        # Two hashmap to convert char to digit
        digits = ["0", "1", "2", "3",
                  "4", "5", "6", "7",
                  "8", "9"]
        prefix = ["+", "-"]

        low = -2 ** 31
        high = 2 ** 31 - 1

        # Get the numeric first (before decimal point)
        found = False
        extract = ""
        for i in str:
            if i == " " and not found:
                pass

            elif i in prefix:
                if not found:
                    extract += i
                    found = True
                else:
                    break

            elif i in digits:
                extract += i
                found = True

            elif i == ".":
                break

            else:
                break

        if not extract:
            return 0
        else:
            result, base = 0, 1
            for i in extract[::-1]:
                if i in digits:
                    result += int(i) * base
                    base *= 10
                elif i == "-":
                    result *= -1

            if result < low:
                return low
            elif result > high:
                return high
            return result

class Solution_B:

    def myAtoi(self, str: str) -> int:
        """use regex method to identify each group of element"""

        mo = re.search(r"^[\s]*([+\-]?)([0]*)(\d+)", str)
        # 4部分, 可选的非数字的开头部分, 可选的正负号, 前驱0, 有效数字部分, 非数字的中间项可以直接忽略

        if not mo:
            return 0

        result, base = 0, 1
        for i in mo.group(3)[::-1]:
            result += int(i) * base
            base *= 10

        result = -1 * result if mo.group(1) == "-" else result

        if result < -2 ** 31:
            return -2 ** 31
        elif result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return result


if __name__ == "__main__":
    testCase = Solution_B()
    assert testCase.myAtoi("ABC") == 0, "Edge 1"

    assert testCase.myAtoi("42") == 42, "Example 1"
    assert testCase.myAtoi("   -42") == -42, "Example 2"
    assert testCase.myAtoi("4193 with words") == 4193, "Example 3"
    assert testCase.myAtoi("words and 987") == 0, "Example 4"
    assert testCase.myAtoi("-91283472332") == -2147483648, "Example 5, return -2^31"

    assert testCase.myAtoi("3.14159") == 3, "Extra 1"
    assert testCase.myAtoi("+1") == 1, "Extra 2"
    assert testCase.myAtoi("+-2") == 0, "Extra 3"
    assert testCase.myAtoi("  -0012a42") == -12, "Extra 4"
    assert testCase.myAtoi("   +0 123") == 0, "Extra 5"
    assert testCase.myAtoi("-5-") == -5, "Extra 6"
    assert testCase.myAtoi("9223372036854775808") == 2147483647, "Extra 7"
    assert testCase.myAtoi("-6147483648") == -2147483648, "Extra 8, 10 digit length but oversize Integer"

    assert testCase.myAtoi("10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000522545459") == 2147483647, "Extra 9, Beyond Long"
    print("all passed")
