# P091 Docde Ways
# Medium

# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# "A" -> 1
# "B" -> 2
# ...
# "Z" -> 26

# Given a non-empty string containing only digits, determine the total number of ways to decode it.


class Solution_A:

    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            if s == "0":
                return 0
            else:
                return 1
        elif len(s) >= 2:
            if s[0] == "0":
                return 0
            elif s[0] != "1" and s[0] != "2":
                return 0
            elif s[0] == "2" and s[1] in ["7", "8", "9"]:
                return 0
            elif self.numDecodings(s[:1]) == 0:
                return 0
            elif self.





s = "ABC"
print(s[:2])




# if __name__ == "__main__":
#     testCase = Solution_A()
#
#     assert testCase.numDecodings("0") == 0, "Edge 1"
#     assert testCase.numDecodings("00") == 0, "Edge 2"
#     assert testCase.numDecodings("230") == 0, "Edge 3"
#     assert testCase.numDecodings("1") == 1, "Edge 4"
#
#     assert testCase.numDecodings("12") == 2, "Example 1"
#     assert testCase.numDecodings("226") == 3, "Example 2"
#
#     assert testCase.numDecodings("227") == 2, "Additional 1"
#     assert testCase.numDecodings("611") == 2, "Additional 2"
#     assert testCase.numDecodings("12390123") == 0, "Additional 3"
#
#     long = "9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"
#     assert testCase.numDecodings(long) == 3981312, "Long"
#     print("All passed")
