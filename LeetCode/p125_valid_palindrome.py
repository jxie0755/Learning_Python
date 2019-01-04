# p125 Valid Palindrome
# Easy

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
# For the purpose of this problem, we define empty string as valid palindrome.

# """
# :type s: str
# :rtype: bool
# """

class Solution:
    def isPalindrome(self, s):
        ### take the space to process the string
        if not s:
            return True
        # process the string
        s_processed = ''
        for i in s:
            if i.isalnum():
                s_processed += i.lower()
        print(s_processed)
        # Check if palindrome
        return s_processed == s_processed[::-1]  # String[::-1], O(n)

    def isPalindrome(self, s):
        ### Two pointer method (no extra space needed)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():  # 注意while loop的嵌套
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    assert Solution().isPalindrome('A man, a plan, a canal: Panama') == True
    assert Solution().isPalindrome('race a car') == False
    print('all passed')
