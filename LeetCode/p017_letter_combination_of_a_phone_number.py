"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
P017 Letter Combination of a Phone Number
Medium


Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
"""

from typing import *


class Solution_A:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Hashtable
        Time:  O(n * 3^n)
        """

        hashtable = {"0": [" "],
                     "1": [""],
                     "2": ["a", "b", "c"],
                     "3": ["d", "e", "f"],
                     "4": ["g", "h", "i"],
                     "5": ["j", "k", "l"],
                     "6": ["m", "n", "o"],
                     "7": ["p", "q", "r", "s"],
                     "8": ["t", "u", "v"],
                     "9": ["w", "x", "y", "z"]
                     }

        result = []
        i = 0
        while i != len(digits):
            current = digits[i]

            if i == 0:
                result = hashtable[current]
            else:
                new_list = hashtable[current]
                result = [j + k for j in result for k in new_list]
            i += 1

        return result


if __name__ == "__main__":
    testMethod = Solution_A().letterCombinations
    assert testMethod("") == [], "Edge 1"
    assert testMethod("1") == [""], "Edge 2"
    assert testMethod("0") == [" "], "Edge 3"

    assert testMethod("2") == ["a", "b", "c"], "Example 1"
    assert testMethod("20") == ["a ", "b ", "c "], "Example 2"
    assert testMethod("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], "Example 3"
    assert testMethod("213") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], "Example 4"

    print("all passed")
