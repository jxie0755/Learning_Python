# P415 Add Strings
# Easy


# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


class Solution:

    # Version A, use add method in manual way
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""

        N1, N2 = num1[::-1], num2[::-1]
        L1, L2 = len(N1), len(N2)

        i = 0
        add = 0
        while i < L1 or i < L2:

            d1 = int(N1[i]) if i < L1 else 0
            d2 = int(N2[i]) if i < L2 else 0
            r = d1 + d2 + add
            result += str(r)[-1]

            if r >= 10:
                add = 1
            else:
                add = 0

            i += 1

        if add:
            result += "1"
        return result[::-1]


if __name__ == "__main__":
    assert Solution().addStrings("1", "1") == "2", "Example 1"
    assert Solution().addStrings("10", "1") == "11", "Example 2"
    assert Solution().addStrings("5", "9") == "14", "Example 3"
    assert Solution().addStrings("15", "9") == "24", "Example 4"
    assert Solution().addStrings("15", "19") == "34", "Example 5"
    assert Solution().addStrings("111", "889") == "1000", "Example 6"

    print("all passed")
