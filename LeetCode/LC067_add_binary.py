"""
https://leetcode.com/problems/add-binary/
p067 Add Binary
Easy

Given two binary strings, return their sum (also a binary string)
"""

class Solution_A:
    def addBinary(self, a: str, b: str) -> str:
        """
        use python built-in conversion
        """
        return "{:b}".format(int(a, 2) + int(b, 2))

class Solution_B:
    def addBinary(self, a: str, b: str) -> str:
        """
        Convert binary to decimal then add, and return the binary conversion of the result
        This will pass but very tedious
        """
        def bi_to_deci(target):
            return sum([int(target[::-1][i]) * 2 ** i for i in range(len(target))])

        def deci_to_bi(target):
            if target:
                ans = ""
                while target != 0:
                    target, digit = divmod(target, 2)
                    ans = str(digit) + ans
                return ans
            return "0"

        return deci_to_bi(bi_to_deci(a) + bi_to_deci(b))

class Solution_C:
    def addBinary(self, a: str, b: str) -> str:
        """
        Use the same principle of binary add calculation
        """
        carry = 0
        result = ""

        while a or b:
            a_end = int(a[-1]) if a else 0
            b_end = int(b[-1]) if b else 0
            carry, tmp = divmod(a_end + b_end + carry, 2)
            result = str(tmp) + result
            a, b = a[:-1], b[:-1]

        return "1" + result if carry else result


class Solution_D:
    def addBinary(self, a: str, b: str) -> str:
        """
        Same binary add principle but easier to understand
        Make a and b same length first, (fill with "0" in the head)
        Then add from tail to head, following binary add principle
        """
        if a == "0" and b == "0":  # Edge case for just two "0"
            return "0"

        # Fill in "0" to a and b, to the same length @ MaxLen + 1
        L = max(len(a), len(b))
        a = a.rjust(L + 1, "0")
        b = b.rjust(L + 1, "0")

        result = ""
        carry = "0"
        for i in range(L, -1, -1):
            cur_a, cur_b = a[i], b[i]
            if (cur_a, cur_b, carry).count("1") == 3:
                result = "1" + result
                carry = "1"
            elif (cur_a, cur_b, carry).count("1") == 2:
                result = "0" + result
                carry = "1"
            elif (cur_a, cur_b, carry).count("1") == 1:
                result = "1" + result
                carry = "0"
            elif (cur_a, cur_b, carry).count("1") == 0:
                result = "0" + result
                carry = "0"

        return result.lstrip("0")


if __name__ == "__main__":
    testCase = Solution_C()
    assert testCase.addBinary("0", "0") == "0", "zero"
    assert testCase.addBinary("11", "1") == "100", "Example 1"
    assert testCase.addBinary("1010", "1011") == "10101", "Example 2"
    assert testCase.addBinary("111", "1") == "1000", "extra 1"
    print("All passed")


