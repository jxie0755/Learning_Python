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
# A   L S   I G
# Y A   H R
# P     I

# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);


class Solution:
    def convert(self, s, numRows):
        ### Time O(N), space O(N)
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        z = list(range(0, numRows)) + list(range(numRows-2, 0, -1))
        cycle = len(z)
        mapping = [[]for i in range(numRows)]

        i = 0
        while i != len(s):
            index = z[i % cycle]
            mapping[index].append(s[i])
            i += 1

        return ''.join(i for i in [''.join(j) for j in mapping])




if __name__ == '__main__':
    assert Solution().convert("", 3) == "", 'Edge 1'
    assert Solution().convert("A", 1) == "A", 'Edge 1'
    assert Solution().convert("AB", 1) == "AB", 'Edge 1'

    assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR", 'Example 1'
    assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI", 'Example 2'
    print('all passed')
