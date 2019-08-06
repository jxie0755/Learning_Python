# https://leetcode.com/problems/multiply-strings/
# P043 Multiply Strings
# Medium

# Given two non-negative integers num1 and num2 represented as strings,
# return the product of num1 and num2, also represented as a string.

# Note:
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


class Solution:

    # Version A
    # Python builtin direct convert
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))

    def int2str(self, num):
        """Convert a int to a string through algorithm"""
        hmp_n2s = {
            0: "0", 1: "1", 2: "2", 3: "3", 4: "4",
            5: "5", 6: "6", 7: "7", 8: "8", 9: "9"
        }
        if num == 0:
            return "0"

        result = ""
        while num:
            result = hmp_n2s[num % 10] + result
            num //= 10
        return result

    # Version B2
    # HashMap method
    # Calulate string by hand calculation method, can avoid overflow of integer/long numbers
    # Avoid using integer calculation, direct return the String value
    def multiply(self, num1: str, num2: str) -> str:
        hmp_s2n = {
            "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
            "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
        }

        len_n1, len_n2 = len(num1), len(num2)
        i = len_n1 -1

        result = 0

        while i >= 0:
            i_factor = 10 ** ((len_n1 -1) - i)
            j = len_n2-1
            while j >= 0:
                j_factor = 10 ** ((len_n2 - 1) - j)
                result += hmp_s2n[num2[j]] * hmp_s2n[num1[i]] * i_factor * j_factor
                j -= 1
            i -= 1

        return self.int2str(result)

    # Version C
    # Break down to add with manual method
    # This can completely avoid overflow of integer/long numbers
    def str_add(self, num1, num2):
        """add two integer in string form together"""


    def multiply(self, num1: str, num2: str) -> str:
        hmp_s2n = {
            "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
            "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
        }

        len_n1, len_n2 = len(num1), len(num2)
        i = len_n1 - 1

        result = 0

        while i >= 0:
            i_factor = 10 ** ((len_n1 - 1) - i)
            j = len_n2 - 1
            while j >= 0:
                j_factor = 10 ** ((len_n2 - 1) - j)
                result += hmp_s2n[num2[j]] * hmp_s2n[num1[i]] * i_factor * j_factor
                j -= 1
            i -= 1

        return self.int2str(result)


if __name__ == "__main__":
    assert Solution().multiply("0", "23") == "0", "Edge 1"
    assert Solution().multiply("2", "23") == "46", "Edge 2"
    assert Solution().multiply("2", "3") == "6", "Example 1"
    assert Solution().multiply("123", "456") == "56088", "Example 2"
    assert Solution().multiply("50", "50") == "2500", "Extra 1"
    print("all passed!")
