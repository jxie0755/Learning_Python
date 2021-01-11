# p387 First Unique Character in a String
# Easy

# Given a string, find the first non-repeating character in it and return it's index.
# If it doesn't exist, return -1
# Note: You may assume the string contain only lowercase letters.

# """
# :type s: str
# :rtype: int
# """

class Solution:
    def firstUniqChar(self, s):
        set_list = sorted(set(s), key=s.index)
        for i in set_list:
            if s.count(i) == 1:
                return s.index(i)
        return -1


if __name__ == "__main__":
    assert Solution().firstUniqChar("leetcode") == 0, "test 1"
    assert Solution().firstUniqChar("loveleetcode") == 2, "test 2"
    assert Solution().firstUniqChar("aabbccdd") == -1, "does not exist"
    print("All passed")
