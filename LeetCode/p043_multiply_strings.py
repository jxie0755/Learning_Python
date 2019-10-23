"""
https://leetcode.com/problems/multiply-strings/
P043 Multiply Strings
Medium

Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Note:
    The length of both num1 and num2 is < 110.
    Both num1 and num2 contain only digits 0-9.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution_A:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Python builtin direct convert
        """
        return str(int(num1) * int(num2))


class Solution_B:
    def multiply(self, num1: str, num2: str) -> str:
        """
        HashMap method
        Calulate string by hand calculation method, can avoid overflow of integer/long numbers
        Avoid using integer calculation, direct return the String value
        """

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

    def int2str(self, num: int) -> str:
        """
        Helper B
        Convert a int to a string through algorithm
        """

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


class Solution_C:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Break down to add with manual method
        This can completely avoid overflow of integer/long numbers
        """

        if num1 == "0":
            return "0"

        result = "0"
        factor = 0
        idx2 = len(num2) - 1
        while (idx2 >= 0):
            to_add = "0"

            for i in range(int(num2[idx2])):
                to_add = self.str_add(to_add, num1)
            to_add += "0" * factor

            result = self.str_add(result, to_add)

            factor += 1
            idx2 -= 1

        return result

    def str_add(self, num1: str, num2: str) -> str:
        """
        Helper C
        add two integer in string form together
        """

        result = ""
        add_on = 0
        idx1, idx2 = len(num1) - 1, len(num2) - 1
        while (idx1 >= 0 or idx2 >= 0):

            d1, d2 = 0, 0
            if idx1 >= 0:
                d1 = int(num1[idx1])
            if idx2 >= 0:
                d2 = int(num2[idx2])

            add_on, d_result = divmod(d1 + d2 + add_on, 10)
            result = str(d_result) + result
            idx1 -= 1
            idx2 -= 1

        if add_on:
            result = str(add_on) + result

        return result


if __name__ == "__main__":
    testMethod = Solution_C().multiply
    assert testMethod("0", "23") == "0", "Edge 1"
    assert testMethod("2", "23") == "46", "Edge 2"
    assert testMethod("2", "3") == "6", "Example 1"
    assert testMethod("123", "456") == "56088", "Example 2"
    assert testMethod("50", "50") == "2500", "Extra 1"
    print("all passed!")
