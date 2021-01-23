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
        pass


if __name__ == "__main__":
    assert Solution().numDecodings("0") == 0, "Edge 1"
    assert Solution().numDecodings("00") == 0, "Edge 2"
    assert Solution().numDecodings("230") == 0, "Edge 3"
    assert Solution().numDecodings("1") == 1, "Edge 4"

    assert Solution().numDecodings("12") == 2, "Example 1"
    assert Solution().numDecodings("226") == 3, "Example 2"

    assert Solution().numDecodings("227") == 2, "Additional 1"
    assert Solution().numDecodings("611") == 2, "Additional 2"
    long = "9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"
    print(Solution().numDecodings(long))

    print("All passed")
