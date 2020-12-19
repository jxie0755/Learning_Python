"""
https://leetcode.com/problems/add-binary/
p067 Add Binary
Easy

Given two binary strings, return their sum (also a binary string)
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pass


if __name__ == "__main__":
    testCase = Solution()
    assert testCase.addBinary("0", "0") == "0", "zero"
    assert testCase.addBinary("11", "1") == "100", "Example 1"
    assert testCase.addBinary("1010", "1011") == "10101", "Example 2"
    assert testCase.addBinary("111", "1") == "1000", "extra 1"
    print("all passed")
