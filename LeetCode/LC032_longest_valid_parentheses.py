"""
https://leetcode.com/problems/longest-valid-parentheses/
LC020 Longest Valid Parentheses
Hard

Given a string containing just the characters "(" and ")", find the length of the longest valid (well-formed) parentheses substring.
"""


class Solution_A:

    def longestValidParentheses(self, s: str) -> int:
        """
        Iterate all substring from long to short and find the first valid
        This will exceed max time
        """
        for lenth in range(len(s), 0, -1):
            for start_idx in range(len(s) - lenth + 1):
                sample = s[start_idx:start_idx + lenth]
                if self.parenIsValid(sample):
                    return len(sample)
        return 0

    def parenIsValid(self, s: str) -> bool:
        """
        Helper function from LC020
        Modified with just to evaluate curved parentheses
        """
        brackets = 0
        for i in s:
            if i == "(":
                brackets += 1
            if i == ")":
                if brackets == 0:
                    return False
                else:
                    brackets -=1

        return brackets == 0


class Solution_B:

    def longestValidParentheses(self, s: str) -> int:
        L, R = 0, 0
        lastR = -1
        i = 0
        while i < len(s):
            cur = s[i]
            pass


testCase = Solution_B()
print(testCase.longestValidParentheses("(()(((()"))

if __name__ == '__main__':
    testCase = Solution_A()

    assert testCase.longestValidParentheses("(()") == 2, "Example 1, '()'"
    assert testCase.longestValidParentheses(")()())") == 4, "Example 2, '()()'"
    assert testCase.longestValidParentheses("") == 0, "Example 3, Edge 0"

    assert testCase.longestValidParentheses("()(()") == 2, "Additional 1"
    assert testCase.longestValidParentheses("()(()()") == 4, "Additional 2"
    assert testCase.longestValidParentheses("(()(((()") == 2, "Additional 3"
    assert testCase.longestValidParentheses("(()((()))") == 8, "Additional 4"

    print("All passed")

