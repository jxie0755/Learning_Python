# LC171 Excel Column Number
# Easy

# Given a column title as appear in an Excel sheet, return its corresponding column number.

class Solution:
    def titleToNumber(self, s):
        # Time:  O(n)
        # Space: O(1)
        """
        :type s: str
        :rtype: int
        """
        translate = {
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6,
            "G": 7,
            "H": 8,
            "I": 9,
            "J": 10,
            "K": 11,
            "L": 12,
            "M": 13,
            "N": 14,
            "O": 15,
            "P": 16,
            "Q": 17,
            "R": 18,
            "S": 19,
            "T": 20,
            "U": 21,
            "V": 22,
            "W": 23,
            "X": 24,
            "Y": 25,
            "Z": 26,
        }

        step = 1
        value = 0
        for i in s[::-1]:
            value += translate[i] * step
            step *= 26
        return value


if __name__ == "__main__":
    assert Solution().titleToNumber("A") == 1, "Example 1"
    assert Solution().titleToNumber("AA") == 27, "Example 2"
    assert Solution().titleToNumber("AB") == 28, "Example 3"
    assert Solution().titleToNumber("AZ") == 52, "Example 4"
    assert Solution().titleToNumber("BA") == 53, "Example 5"
    assert Solution().titleToNumber("ZY") == 701, "Example 6"
    assert Solution().titleToNumber("AAB") == 704, "Example 7"
    print("All passed")
