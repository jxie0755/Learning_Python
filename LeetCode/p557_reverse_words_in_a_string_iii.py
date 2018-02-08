# p557 Reverse Words in a String III
# Easy

# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order
# Note: In the string, each word is separated by single space and there will not be any extra space in the string

# """
# :type s: str
# :rtype: str
# """

class Solution:
    def reverseWords(self, s):
        result = ''
        for i in s.split():
            result += i[::-1] + ' '
        return result.rstrip()

    def reverseWords(self, s):  # use joint, to avoid rstrip()
        return ' '.join(map(lambda x: x[::-1], s.split()))


if __name__ == '__main__':
    assert Solution().reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc", 'regular'
    print('all passed')
