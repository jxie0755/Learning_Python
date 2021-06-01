"""
https://leetcode.com/problems/longest-valid-parentheses/
LC020 Longest Valid Parentheses
Hard

Given a string containing just the characters "(" and ")", find the length of the longest valid (well-formed) parentheses substring.
"""


class Solution_A:
    def longestValidParentheses(self, s: str) -> int:
        pass





if __name__ == '__main__':
    testCase = Solution_A()

    assert testCase.longestValidParentheses("(()") == 2, "Example 1, '()'"
    assert testCase.longestValidParentheses(")()())") == 4, "Example 2, '()()'"
    assert testCase.longestValidParentheses("") == 0, "Example 3, Edge 0"

    print("All passed")
