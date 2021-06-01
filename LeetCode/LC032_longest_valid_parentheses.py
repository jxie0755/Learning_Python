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
        longest_so_far = 0
        L, R = 0, 0

        for i in s:
            if i == "(":
                L += 1
            elif i == ")":
                R += 1

            if L >= R:
                longest_so_far = max(longest_so_far, R*2)
            else:
                L, R = 0, 0

        return longest_so_far




if __name__ == '__main__':
    testCase = Solution_A()

    assert testCase.longestValidParentheses("(()") == 2, "Example 1, '()'"
    assert testCase.longestValidParentheses(")()())") == 4, "Example 2, '()()'"
    assert testCase.longestValidParentheses("") == 0, "Example 3, Edge 0"

    assert testCase.longestValidParentheses("()(()") == 2, "Additional 1"

    print("All passed")

