"""
https://leetcode.com/problems/valid-parentheses/
p020 Valid Parentheses
Easy

Given a string containing just the characters "(", ")", "{", "}", "[" and "]", determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution_A:

    # setup data as class attributes
    OPEN_BRACKETS = {"(": 1, "{": 2, "[": 3}
    CLOSE_BRACKETS = {")": 1, "}": 2, "]": 3}

    def isValid(self, s: str) -> bool:
        """
        idea from checkio/electionic station/p1_brackets and improved
        不再使用index,因为太不直观,直接使用mapping把左括号和右括号对应值(其实不需要是num,任何三个键值都能成立)
        仍然是用pop()来对应括号位置关系
        """
        brackets = []
        for i in s:
            if i in self.OPEN_BRACKETS:
                brackets.append(self.OPEN_BRACKETS[i])
            if i in self.CLOSE_BRACKETS:
                if len(brackets) == 0:
                    return False
                if brackets.pop() != self.CLOSE_BRACKETS[i]:  # one step for two operations
                    return False    # pop anyway, and if true, pop is aleady done.
        return len(brackets) == 0


if __name__ == "__main__":
    testCase = Solution_A()
    assert testCase.isValid("((5+3)*2+1)"), "Simple"
    assert testCase.isValid("{[(3+1)+2]+}"), "Different types"
    assert not testCase.isValid("(3+{1-1)}"), ") is alone inside {}"
    assert testCase.isValid("[1+1]+(2*2)-{3/3}"), "Different operators"
    assert not testCase.isValid("(({[(((1)-2)+3)-3]/3}-3)"), "One is redundant"
    assert testCase.isValid("2+3"), "No brackets, no problem"
    assert not testCase.isValid(")("), "begin with right"
    print("All passed")
