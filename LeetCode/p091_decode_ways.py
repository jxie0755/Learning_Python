# P091 Docde Ways
# Medium

# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26

# Given a non-empty string containing only digits, determine the total number of ways to decode it.


class Solution:
    ### This will now work, but exceeded max timei limit
    ### Recursion depth is not the problem
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1
        elif s[0] == '0':
            return 0
        elif len(s) == 1:
            return 1
        else:
            if int(s[0]) < 2 or int(s[0]) == 2 and int(s[1]) <= 6:
                return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            elif int(s[0]) > 2 and s[1] == '0':
                return 0
            elif int(s[0]) > 2:
                return self.numDecodings(s[1:])
            else:
                return self.numDecodings(s[2:])





if __name__ == '__main__':
    assert Solution().numDecodings('0') == 0, 'Edge 0'
    assert Solution().numDecodings('00') == 0, 'Edge 00'
    assert Solution().numDecodings('230') == 0, 'Edge 00'
    assert Solution().numDecodings('1') == 1, 'Edge 1'

    assert Solution().numDecodings('12') == 2, 'Example 1'
    assert Solution().numDecodings('226') == 3, 'Example 2'

    assert Solution().numDecodings('227') == 2, 'Additional 1'
    assert Solution().numDecodings('611') == 2, 'Additional 2'
    long = "9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"
    print(Solution().numDecodings(long))

    print('all passed')
