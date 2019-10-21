"""
https://leetcode.com/problems/plus-one/
p066 Plus One
Easy

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
"""


from typing import *

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Version A, quick recursion
        """
        if digits[-1] == 9:
            if len(digits) == 1:
                return [1, 0]
            else:
                return self.plusOne(digits[:-1]) + [0]
        else:
            digits[-1] += 1
            return digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        STD ans with carry number
        """
        carry = 1
        for i in reversed(range(len(digits))):
            tmp = digits[i]
            carry, digits[i] = divmod(tmp + carry, 10)
            if carry == 0:
                break

        if carry == 1:
            digits.insert(0, carry)

        return  digits


if __name__ == "__main__":
    assert Solution().plusOne([0]) == [1], "Edge 0"
    assert Solution().plusOne([1, 2, 3]) == [1, 2, 4], "Example 1"
    assert Solution().plusOne([4, 3, 2, 1]) == [4, 3, 2, 2], "Example 2"
    assert Solution().plusOne([1, 9, 9]) == [2, 0, 0], "Example 3"
    assert Solution().plusOne([9, 9, 9]) == [1, 0, 0, 0], "Example 4"
    print("all passed")
