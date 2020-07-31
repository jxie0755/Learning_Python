"""
https://leetcode.com/problems/zigzag-conversion/
P006 ZigZag Conversion
Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

n = 3
P   A   H   N
A P L S I I G
Y   I   R

n = 4
P     I     N
A   L S7  I G
Y A   H R 11
P     I

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """Time O(N), space O(N)"""

        # build a grid first
        grid = []

        # build a cycling grid_idx to guide adding letter from str to grid
        cycle_idx = [i for i in range(numRows)]
        cycle_idx = cycle_idx + cycle_idx[-2:0:-1]
        for i in range(numRows):
            grid.append([])

        # add letter to grid following the rule
        for i in range(len(s)):
            letter = s[i]
            grid_idx = cycle_idx[i % len(cycle_idx)]
            grid[grid_idx].append(letter)

        # output result by joining
        ans = ""
        for row in grid:
            ans += "".join(row)

        return ans



if __name__ == "__main__":
    testCase = Solution()
    assert testCase.convert("", 3) == "", "Edge 1"
    assert testCase.convert("A", 1) == "A", "Edge 2"
    assert testCase.convert("AB", 1) == "AB", "Edge 3"

    assert testCase.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR", "Example 1"
    assert testCase.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI", "Example 2"
    print("all passed")
