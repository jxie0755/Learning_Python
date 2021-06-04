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
        global_max = 0

        last_L = -1
        last_R = -1
        last_equality = 0
        last_equality_idx = -1

        i = 0
        while i < len(s):
            cur = s[i]
            if cur == "(":
                L += 1
                last_R = -1
            elif cur == ")":
                R += 1
                last_L = -1

            if L == R:
                global_max = max(global_max, L+R+last_equality)
                last_equality_idx = i
                last_L = -1
                L, R = 0, 0
            elif L < R:
                last_R = -1
                last_equality = 0
                L, R = 0, 0  # reset
            else:
                if cur == ")":
                    if last_R == i-1:
                        global_max = max(global_max, R*2)
                        last_R = i
                    else:
                        global_max = max(global_max, 2)
                        R = 1
                elif cur == "(":
                    if last_L == i-1:
                        last_L = i
                    else:
                        L = 1

            i += 1

        return global_max


testCase = Solution_B()
print(testCase.longestValidParentheses(")()())"))

# if __name__ == '__main__':
#     testCase = Solution_B()
#
#     assert testCase.longestValidParentheses("(()") == 2, "Example 1, '()'"
#     assert testCase.longestValidParentheses(")()())") == 4, "Example 2, '()()'"
#     assert testCase.longestValidParentheses("") == 0, "Example 3, Edge 0"
#
#     assert testCase.longestValidParentheses("()(()") == 2, "Additional 1"
#     assert testCase.longestValidParentheses("()(()()") == 4, "Additional 2"
#     assert testCase.longestValidParentheses("(()(((()") == 2, "Additional 3"
#     assert testCase.longestValidParentheses("(()((()))") == 8, "Additional 4"
#     assert testCase.longestValidParentheses("(((()())))") == 10, "Additional 5"
#
#     print("All passed")

