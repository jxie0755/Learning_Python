# p434 Number of Segments in a String
# Easy

# Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
# Please note that the string does not contain any non-printable characters.

# """
# :type s: str
# :rtype: int
# """

class Solution:
    def countSegments(self, s):
        # use python built-in string method
        return len(s.split())

    def countSegments(self, s):
        # does not use python characteristics, O(n)
        word = False  # set a flag for word, switch it on and off in iteration
        count = 0
        for i in range(len(s)):
            if s[i] != " ":
                word = True
            elif s[i] == " " and word:
                count += 1
                word = False
        return count + 1 if word else count


if __name__ == "__main__":
    assert Solution().countSegments("Hello, my name is John") == 5, "regular"
    assert Solution().countSegments("Hello") == 1, "one word"
    assert Solution().countSegments("") == 0, "empty"
    assert Solution().countSegments("     ") == 0, "all space"
    assert Solution().countSegments("  aaa   ") == 1, "tricky space on both side"
    print("all passed")
