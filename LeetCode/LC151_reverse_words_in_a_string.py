# LC151 Reverse Words in a String
# Medium

# Given an input string, reverse the string word by word.

# Note:
# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces.
# However, your reversed string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the reversed string.


class Solution(object):

    # Version A, with the help of list
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = []

        wordfound = False
        word = ""
        for i in s:
            if i == " " and not wordfound:
                pass
            elif i == " " and wordfound:
                lst.append(word)
                word = ""
                wordfound = False
            else:
                wordfound = True
                word += i
        if wordfound:
            lst.append(word)
        return " ".join(lst[::-1])


class Solution(object):

    # Version B Do not use list, just directly get the string
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        wordfound = False
        word = ""
        for i in s:
            if i == " " and not wordfound:
                pass
            elif i == " " and wordfound:
                result = word + " " + result
                word = ""
                wordfound = False
            else:
                wordfound = True
                word += i
        if wordfound:
            result = word + " " + result
        return result[:-1]


class Solution(object):
    # STD ans
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return " ".join(reversed(s.split()))


if __name__ == "__main__":
    assert Solution().reverseWords("") == "", "Edge 0"
    assert Solution().reverseWords("    ") == "", "Edge 1"
    assert Solution().reverseWords("   a   ") == "a", "Edge 2"

    assert Solution().reverseWords("the sky is blue") == "blue is sky the", "Example 1"
    assert Solution().reverseWords("  hello world!  ") == "world! hello", "Example 2"
    assert Solution().reverseWords("a good   example") == "example good a", "Example 3"

    print("All passed")
