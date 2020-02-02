# p383 Ransom Note
# Easy

# Given an arbitrary ransom note string and another string containing letters from all the magazines
# write a function that will return true if the ransom note can be constructed from the magazines
# otherwise, it will return false.
# Each letter in the magazine string can only be used once in your ransom note.
# Note:
# You may assume that both strings contain only lowercase letters.

# """
# :type ransomNote: str
# :type magazine: str
# :rtype: bool
# """

class Solution:
    def canConstruct(self, ransomNote, magazine):
        index = 0
        while index < len(magazine) - len(ransomNote) + 1:
            if magazine[index:index + len(ransomNote)] == ransomNote:
                return True
            index += 1
        return False
        # this only checks a whole slice of magazine == ransomNote, but ransomNote can be break-down into smaller parts

    def canConstruct(self, ransomNote,
                     magazine):  # basically is to check if there is enough letters in magazine to make ransomNote
        return all(ransomNote.count(i) <= magazine.count(i) for i in set(ransomNote))


if __name__ == "__main__":
    assert Solution().canConstruct("aa", "abc") == False, "not in"
    assert Solution().canConstruct("aa", "aaa") == True, "in"
    assert Solution().canConstruct("abc", "aaabdddd") == False, "not in 2"
    assert Solution().canConstruct("abc", "cxxxbxxxxa") == True, "in 2"
    assert Solution().canConstruct("abc", "xxxxxxxxxxbca") == True, "in end 2"
    assert Solution().canConstruct("fffbfg", "effjfggbffjdgbjjhhdegh") == True, "put together"
    print("all passed")
