"""
https://leetcode.com/problems/roman-to-integer/
p013 Roman to Integer
Easy

Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution_A:

    def romanToInt(self, s: str) -> int:
        """Hashmap method"""

        result = 0
        # remove the possibility of 4 and 9
        checklst = {"CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4}
        for i in checklst.keys():
            if i in s:
                result += checklst[i]
                s = s.replace(i, "")

        # Calculate the rest of it
        Roman_Nu = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        for i in s:
            result += Roman_Nu[i]

        return result


if __name__ == "__main__":
    testCase = Solution_A()
    assert testCase.romanToInt("MMMCDXCIX") == 3499, "Example 1"
    print("All passed")
