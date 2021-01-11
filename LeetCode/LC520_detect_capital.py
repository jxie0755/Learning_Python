# p520 Detect Capital
# Easy

# Given a word, you need to judge whether the usage of capitals in it is right or not.
# We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital if it has more than one letter, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.
#
# Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

# """
# :type word: str
# :rtype: bool
# """

class Solution:
    def detectCapitalUse(self, word):
        # check condition
        if all(i.isupper() for i in word) or all(i.islower() for i in word):
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        else:
            return False

    def detectCapitalUse(self, word):
        # compare method
        return word == word.upper() or word == word.lower() or word == word.title()

    def detectCapitalUse(self, word):
        # compare method, two conditions
        return word[1:] == word[1:].lower() or word == word.upper()


if __name__ == "__main__":
    assert Solution().detectCapitalUse("USA") == True, "all up"
    assert Solution().detectCapitalUse("FlaG") == False, "up in elsewhere"
    assert Solution().detectCapitalUse("Flag") == True, "Title like"
    assert Solution().detectCapitalUse("flag") == True, "all low"
    assert Solution().detectCapitalUse("a") == True, "one low"
    assert Solution().detectCapitalUse("A") == True, "one up"
    print("All passed")
