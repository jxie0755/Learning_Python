# P091 Docde Ways
# Medium

# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# "A" -> 1
# "B" -> 2
# ...
# "Z" -> 26

# Given a non-empty string containing only digits, determine the total number of ways to decode it.


class Solution:
    # This will now work, but exceeded max timei limit
    # Recursion depth is not the problem
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1
        elif s[0] == "0":
            return 0
        elif len(s) == 1:
            return 1
        else:
            if int(s[0]) < 2 or int(s[0]) == 2 and int(s[1]) <= 6:
                return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            elif int(s[0]) > 2 and s[1] == "0":
                return 0
            elif int(s[0]) > 2:
                return self.numDecodings(s[1:])
            else:
                return self.numDecodings(s[2:])


class Solution(object):
    # STD ans
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == "0":
            return 0
        prev, prev_prev = 1, 0  # 追踪到达前两位的路线数目
        for i in range(len(s)):
            cur = 0

            if s[i] != "0":  # 如果当前为0的话, 就没有办法从上一位走到这里, 因为不能以0开头
                cur = prev   # 不为0的话, 能走到上一步就一定能走到这一步

            # 此时再看上一位如果和当前能组成一个小于26且不为0的数, 那么也可以从上上位走到这里
            # 不然的话就没办法从上上位走到这里
            if i > 0 and (s[i - 1] == "1" or (s[i - 1] == "2" and s[i] <= "6")):
                cur += prev_prev

            prev, prev_prev = cur, prev  # 迭代前两位的数线数

        return prev


if __name__ == "__main__":
    assert Solution().numDecodings("0") == 0, "Edge 0"
    assert Solution().numDecodings("00") == 0, "Edge 00"
    assert Solution().numDecodings("230") == 0, "Edge 00"
    assert Solution().numDecodings("1") == 1, "Edge 1"

    assert Solution().numDecodings("12") == 2, "Example 1"
    assert Solution().numDecodings("226") == 3, "Example 2"

    assert Solution().numDecodings("227") == 2, "Additional 1"
    assert Solution().numDecodings("611") == 2, "Additional 2"
    long = "9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"
    print(Solution().numDecodings(long))

    print("all passed")
