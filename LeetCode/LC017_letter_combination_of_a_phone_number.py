"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
LC017 Letter Combination of a Phone Number
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

        hmp = {
            "0": [" "],
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
        for i in range(len(digits)):

            current = digits[i]

            if i == 0:
                result = hmp[current]
            else:
                result = [j + k
                          for j in result
                          for k in hmp[current]
                          ]
        return result



if __name__ == "__main__":
    testCase = Solution_A()
    assert testCase.letterCombinations("") == [], "Edge 0"
    assert testCase.letterCombinations("1") == [""], "Edge 1"
    assert testCase.letterCombinations("0") == [" "], "Edge 2"

    assert testCase.letterCombinations("2") == ["a", "b", "c"], "Example 1"
    assert testCase.letterCombinations("20") == ["a ", "b ", "c "], "Example 2"
    assert testCase.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], "Example 3"
    assert testCase.letterCombinations("213") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], "Example 4"

    print("All passed")
