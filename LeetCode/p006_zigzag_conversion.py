# P006 ZigZag Conversion
# Medium


# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)

# n = 3
# P   A   H   N
# A P L S I I G
# Y   I   R

# n = 4
# P     I     N
# A   L S7  I G
# Y A   H R 11
# P     I

# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);


class Solution:

    # Version A1, Time O(N), space O(N)
    def convert(self, s: str, numRows: int) -> str:

        z = list(range(0, numRows)) + list(range(numRows-2, 0, -1))  # cyling pather of 1 Z move (idx)
        cycle = len(z)
        mapping = [[]for _ in range(numRows)]

        i = 0
        while i != len(s):
            mapping[z[i % cycle]].append(s[i])
            i += 1

        return ''.join(i for i in [''.join(j) for j in mapping])


class Solution:

    # Version A2, Time O(N), space O(N)
    def convert(self, s: str, numRows: int) -> str:

        z= list(range(0, numRows)) + list(range(numRows-2, 0, -1))
        z *= (len(s) // len(z) + 1)  # 直接扩展z, 不要用cycle的方式
        mapping = [[] for _ in range(numRows)]

        i = 0
        while i != len(s):
            mapping[z[i]].append(s[i])  # 也就是直接引用z中相同的index的index
            i += 1

        return ''.join(i for i in [''.join(j) for j in mapping])


class Solution(object):

    # Version B, Time O(N), Space O(1) better in space
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s
        step, zigzag = 2 * numRows - 2, ""

        for i in range(numRows):
            for j in range(i, len(s), step):  # 使用step法直接原地找到index值
                zigzag += s[j]
                additional = j + (numRows-1-i) * 2
                if 0 < i < numRows - 1 and additional < len(s):  # 重叠空间要管一下
                    zigzag += s[additional]
        return zigzag


Solution().convert("PAYPALISHIRING", 3)


# if __name__ == '__main__':
#     assert Solution().convert("", 3) == "", 'Edge 1'
#     assert Solution().convert("A", 1) == "A", 'Edge 1'
#     assert Solution().convert("AB", 1) == "AB", 'Edge 1'
#
#     assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR", 'Example 1'
#     assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI", 'Example 2'
#     print('all passed')
