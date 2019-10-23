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
            prev = self.generateParenthesis(n - 1)  # 根据n-1的答案, 其中每一个括号组做一个新的生成
            for par in prev:
                result += self.gen_par(par)
            return list(set(result))  # 需要用set来去重复 (注意顺序可能变化,不能match test case)

    def gen_par(self, par: str) -> List[str]:
        """Helper A"""

        index_list = []  # 找到所有右括号")"的位置
        for i in range(0, len(par)):
            if par[i] == ")":
                index_list.append(i)

        result = []  # 根据右括号的位置,分别插入一个"()"在左侧,和右侧
        for i in index_list:
            result.append(par[:i] + "()" + par[i:])
            result.append(par[:i + 1] + "()" + par[i + 1:])
        return result

class Solution_STD:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Recursive
        Time:  O(4^n / n^(3/2)) ~= Catalan numbers
        Space: O(n)
        """
        def generate(p: str, left: int, right: int, parens: List[str] = []) -> List[str]:
            """Helper"""

            if left:
                generate(p + "(", left - 1, right)
            if right > left:
                generate(p + ")", left, right - 1)
            if not right:
                # parens += p,   # Here p, means a tuple (p,) see ZSimpleLearnings.py_tuple_expression
                parens.append(p)
            return parens

        return generate("", n, n)


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
    testMethod = Solution_B().generateParenthesis
    assert testMethod(1) == ["()"], "Edge 1"

    assert testMethod(2) == ["(())", "()()"]
    assert testMethod(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert testMethod(4) == ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())",
                                                 "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()",
                                                 "()()(())", "()()()()"]

    print("all passed")
