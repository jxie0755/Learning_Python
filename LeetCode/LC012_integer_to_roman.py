"""
https://leetcode.com/problems/integer-to-roman/
LC012 Integer to Roman
Medium

Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution_A:
    def intToRoman(self, num: int) -> str:
        """Hashmap convert"""

        R = {0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX",
             10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
             100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM",
             1000: "M", 2000: "MM", 3000: "MMM"}

        num = str(num).rjust(4, "0")  # 利用rjust补足数字成为4位数
        dlst = list(map(lambda x, y: int(x) * y, num, (1000, 100, 10, 1)))  # 分解各数位
        return "".join(list(map(lambda x: R[x], dlst)))  # 将各数位代换成罗马数字,然后拼接

class Solution_B:

    def intToRoman(self, num: int) -> str:
        """String method"""

        num = str(num).rjust(4, "0")  # 拆解data成为单独的数字字符,并补足数位

        def rom(n: int, x: str, y: str, z: str) -> str:  # 写一个函数来表明转换逻辑
            """Helper"""

            nd = int(num[n])
            if nd == 0:
                return ""
            elif nd < 4:
                return nd * x
            elif nd == 4:
                return x + y
            elif nd < 9:
                return y + (nd - 5) * x
            elif nd == 9:
                return x + z

        # 使用map对data中每个数位进行转换,然后合并
        return "".join(list(map(rom, range(4), ["M", "C", "X", "I"], ["", "D", "L", "V"], ["", "M", "C", "X"])))

class Solution_C:

    def intToRoman(self, num: int) -> str:
        """
        Hashmap alternative
        DIVMOD method  -- it is actually a system of more than just decimal system, but a mixture of 1 to 1000
        """

        result = ""
        roman_list = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                      (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                      (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
                      (1, "I")
                      ]
        for arabic, roman in roman_list:
            repeat, num = divmod(num, arabic)
            result += repeat * roman
        return result
        # 这个地方tricky在于,要注意字典的order问题,在python3.6,字典是有order
        # 但是如果运行与python低版本,dict没有order,会出现算法bug
        # 在这里LeetCode就出现了这个bug,所以把dict拆分成list来做算法解决
        # 也可以使用collections.OrderedDrict


if __name__ == "__main__":
    testCase = Solution_A()
    assert testCase.intToRoman(3888) == "MMMDCCCLXXXVIII", "one check is good"
    print("All passed")
