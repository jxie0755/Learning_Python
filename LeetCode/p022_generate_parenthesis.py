# p22 Generate Parentheses
# Medium

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# """
# :type n: int
# :rtype: List[str]
# """

# my own solusion
class Solution:

    ### recursive
    ### Time  O(N^2)
    ### Space O(N^2)
    def gen_par(self, par):
        index_list = []    # 找到所有右括号')'的位置
        for i in range(0, len(par)):
            if par[i] == ')':
                index_list.append(i)

        result = []        # 根据右括号的位置,分别插入一个'()'在左侧,和右侧
        for i in index_list:
            result.append(par[:i] + '()' + par[i:])
            result.append(par[:i+1] + '()' + par[i+1:])
        return result

    def generateParenthesis(self, n):
        if n == 1:
            return ['()']
        else:
            result = []
            prev = self.generateParenthesis(n-1)   # 根据n-1的答案, 其中每一个括号组做一个新的生成
            for par in prev:
                result += self.gen_par(par)
            return list(set(result))              # 需要用set来去重复


class Solution:
    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:
                generate(p + '(', left - 1, right)
            if right > left:
                generate(p + ')', left, right - 1)
            if not right:
                parens += p,   # Here p, means a tuple (p,) see ZSimpleLearnings.py_tuple_expression
            return parens

        return generate('', n, n)


# An easier way to understand previous
class Solution:
    ### Time:  O(4^n / n^(3/2)) ~= Catalan numbers
    ### Space: O(n)
    def generateParenthesis(self, n):
        parens = []
        def generate(p, left, right):

            nonlocal parens

            if left:
                generate(p + '(', left - 1, right)
            if right > left:
                generate(p + ')', left, right - 1)
            if not right:
                parens.append(p)

        generate('', n, n)
        return parens



if __name__ == '__main__':
    assert Solution().generateParenthesis(1) == ['()'], "Edge 1"

    assert set(Solution().generateParenthesis(2)) == set(["(())", "()()"])
    assert set(Solution().generateParenthesis(3)) == set(["((()))", "(()())", "(())()", "()(())", "()()()"])
    assert set(Solution().generateParenthesis(4)) == set(['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()'])
    print('all passed')
