"""
https://leetcode.com/problems/generate-parentheses/
p22 Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

from typing import *


class Solution_A:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Recursive
        Time  O(N^2)
        Space O(N^2)
        """
        if n == 1:
            return ["()"]
        else:
            result = []
            for combination in self.generateParenthesis(n - 1):
                for i in range(len(combination)):
                    if combination[i] == ")":
                        result.append(combination[:i] + "()" + combination[i:])
                        result.append(combination[:i + 1] + "()" + combination[i + 1:])
            return sorted(list(set(result)))

class Solution_STD:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Recursive
        Time:  O(4^n / n^(3/2)) ~= Catalan numbers
        Space: O(n)
        """
        return self.generate("", n, n, [])

    def generate(self, p: str, left: int, right: int, parens: List[str]) -> List[str]:
        """Helper"""

        if left:
            self.generate(p + "(", left - 1, right, parens)
        if right > left:
            self.generate(p + ")", left, right - 1, parens)
        if not right:
            # parens += p,   # Here p, means a tuple (p,) see ZSimpleLearnings.py_tuple_expression
            parens.append(p)
        return parens


class Solution_B:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        An easier way to understand STD ans
        """
        parens = []

        def generate(p: str, left: int, right: int) -> None:
            """Helper"""

            if left:
                generate(p + "(", left - 1, right)
            if right > left:
                generate(p + ")", left, right - 1)
            if not right:
                parens.append(p)

        generate("", n, n)
        return parens


if __name__ == "__main__":
    testCase = Solution_STD()
    assert testCase.generateParenthesis(1) == ["()"], "Edge 1"

    assert testCase.generateParenthesis(2) == ["(())", "()()"]
    assert testCase.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert testCase.generateParenthesis(4) == ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())",
                                                 "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()",
                                                 "()()(())", "()()()()"]

    print("all passed")
