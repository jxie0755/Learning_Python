"""
https://leetcode.com/problems/valid-parentheses/
p020 Valid Parentheses
Easy

Given a string containing just the characters "(", ")", "{", "}", "[" and "]", determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution_A:
    def isValid(self, s: str) -> bool:
        """
        idea from checkio/electionic station/p1_brackets and improved
        不再使用index,因为太不直观,直接使用mapping把左括号和右括号对应值(其实不需要是num,任何三个键值都能成立)
        仍然是用pop()来对应括号位置关系
        """
        OPEN_BRACKETS = {"(": 1, "{": 2, "[": 3}
        CLOSE_BRACKETS = {")": 1, "}": 2, "]": 3}  # setup data as class attributes

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


if __name__ == "__main__":
    testMethod = Solution_A().isValid
    assert testMethod("((5+3)*2+1)"), "Simple"
    assert testMethod("{[(3+1)+2]+}"), "Different types"
    assert not testMethod("(3+{1-1)}"), ") is alone inside {}"
    assert testMethod("[1+1]+(2*2)-{3/3}"), "Different operators"
    assert not testMethod("(({[(((1)-2)+3)-3]/3}-3)"), "One is redundant"
    assert testMethod("2+3"), "No brackets, no problem"
    print("all passed")
