# p020 Valid Parentheses
# Easy

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

# """
# :type s: str
# :rtype: bool
# """

class Solution():
    class Solution():
    
    OPEN_BRACKETS = {'(': 1, '{': 2, '[': 3}
    CLOSE_BRACKETS = {')': 1, '}': 2, ']': 3}  # setup data as class attributes
    
    def isValid(self, s):  # beats 60.51%
        result = []
        for i in s:
            if i in Solution.OPEN_BRACKETS:
                result.append(Solution.OPEN_BRACKETS[i])
            if i in Solution.CLOSE_BRACKETS:
                if len(result) == 0:
                    return False
                if result.pop() != Solution.CLOSE_BRACKETS[i]:
                    return False
        return len(result) == 0

# 改进了Checkio/electronic_station/p1_brackets的写法
# 不再使用index,因为太不直观,直接使用mapping把左括号和右括号对应值(其实不需要是num,任何三个键值都能成立)
# 仍然是用pop()来对应括号位置关系

if __name__ == '__main__':
    assert Solution().isValid("((5+3)*2+1)") == True, "Simple"
    assert Solution().isValid("{[(3+1)+2]+}") == True, "Different types"
    assert Solution().isValid("(3+{1-1)}") == False, ") is alone inside {}"
    assert Solution().isValid("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert Solution().isValid("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert Solution().isValid("2+3") == True, "No brackets, no problem"
    print('all passed')
    
