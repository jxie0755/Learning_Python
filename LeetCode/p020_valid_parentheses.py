# p020 Valid Parentheses
# Easy

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        OPEN_BRACKETS = ("(", "{", "[",)
        CLOSE_BRACKETS = (")", "}", "]",)
        result = []

        for i in s:
            if i in OPEN_BRACKETS:
                result.append(OPEN_BRACKETS[OPEN_BRACKETS.index(i)])
            if i in CLOSE_BRACKETS:
                if len(result) == 0:
                    return False
                if result.pop() != OPEN_BRACKETS[CLOSE_BRACKETS.index(i)]:
                    return False
        return len(result) == 0

print(Solution().isValid("{[(3+1)+2]+}"))
