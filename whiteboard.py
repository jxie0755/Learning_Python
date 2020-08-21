"""
https://leetcode.com/problems/generate-parentheses/
p22 Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

from typing import *

class Solution_STD:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        else:
            result = []
            for combination in self.generateParenthesis(n-1):
                for i in range(len(combination)):
                    if combination[i] == ")":
                        result.append(combination[:i] + "()" + combination[i:])
                        result.append(combination[:i + 1] + "()" + combination[i + 1:])
            return sorted(list(set(result)))


if __name__ == "__main__":
    testCase = Solution_STD()
    assert testCase.generateParenthesis(1) == ["()"], "Edge 1"

    assert testCase.generateParenthesis(2) == ["(())", "()()"]
    print(testCase.generateParenthesis(3))
    assert testCase.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert testCase.generateParenthesis(4) == ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())",
                                                 "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()",
                                                 "()()(())", "()()()()"]

    print("all passed")


