"""
https://leetcode.com/problems/zigzag-conversion/
LC006 ZigZag Conversion
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

class Solution_A1:
    def convert(self, s: str, numRows: int) -> str:
        """Time O(N), space O(N)"""
        z = list(range(0, numRows)) + list(range(numRows - 2, 0, -1))  # cyling pather of 1 Z move (idx)
        cycle = len(z)
        mapping = [[] for _ in range(numRows)]

        i = 0
        while i != len(s):
            mapping[z[i % cycle]].append(s[i])
            i += 1

        return "".join(i for i in ["".join(j) for j in mapping])


class Solution_A2:
    def convert(self, s: str, numRows: int) -> str:
        """Time O(N), space O(N)"""
        z = list(range(0, numRows)) + list(range(numRows - 2, 0, -1))
        z *= (len(s) // len(z) + 1)  # 直接扩展z, 不要用cycle的方式
        mapping = [[] for _ in range(numRows)]

        i = 0
        while i != len(s):
            mapping[z[i]].append(s[i])  # 也就是直接引用z中相同的index的index
            i += 1

        return "".join(i for i in ["".join(j) for j in mapping])

class Solution_A3:
    def convert(self, s: str, numRows: int) -> str:
        """Time O(N), space O(N), more general and straightforward for reading"""
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



class Solution_B:
    """Time O(N), Space O(1) better in space"""
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        step = 2 * numRows - 2
        zigzag = ""

        for i in range(numRows):
            for j in range(i, len(s), step):  # 使用step法直接原地找到index值
                zigzag += s[j]

                if 0 < i < numRows - 1: # 指定折返区间不能是头尾
                    returning_idx = j + (numRows - 1 - i) * 2  # 补充折返字符串
                    if returning_idx < len(s):  # 折返不要超出末尾
                        zigzag += s[returning_idx]

        return zigzag


if __name__ == "__main__":
    testCase = Solution_B()
    assert testCase.convert("", 3) == "", "Edge 0"
    assert testCase.convert("A", 1) == "A", "Edge 1"
    assert testCase.convert("AB", 1) == "AB", "Edge 2"

    assert testCase.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR", "Example 1"
    assert testCase.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI", "Example 2"
    print("All passed")
