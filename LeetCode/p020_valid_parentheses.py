# p020 Valid Parentheses
# Easy

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution(object):
    def isValid(self, s):  # beats 60.51%
        """
        :type s: str
        :rtype: bool
        """
        OPEN_BRACKETS = {'(': 1, '{': 2, '[': 3}
        CLOSE_BRACKETS = {')': 1, '}': 2, ']': 3}
        result = []
        for i in s:
            if i in OPEN_BRACKETS:
                result.append(OPEN_BRACKETS[i])
            if i in CLOSE_BRACKETS:
                if len(result) == 0:
                    return False
                if result.pop() != CLOSE_BRACKETS[i]:
                    return False
        return len(result) == 0

# 改进了Checkio/electronic_station/p1_brackets的写法
# 不再使用index,因为太不直观,直接使用mapping把左括号和右括号对应值(其实不需要是num,任何三个键值都能成立)
# 仍然是用pop()来对应括号位置关系

print(Solution().isValid("{[(3+1)+2]+}"))
