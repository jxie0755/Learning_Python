# p22 Generate Parentheses
# Medium

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# """
# :type n: int
# :rtype: List[str]
# """

class Solution:
    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:
                generate(p + '(', left - 1, right)
            if right > left:
                generate(p + ')', left, right - 1)
            if not right:
                parens += p,
            return parens

        return generate('', n, n)


class Solution:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        if n == 0:
            return []
        elif n == 1:
            return ['()']
        else:
            prev = self.generateParenthesis(n-1)
            result = []
            result += ['(' + i + ')' for i in prev]
            result += ['()' + i for i in prev]
            result += [i + '()' for i in prev]
            return list(set(result))



# if __name__ == '__main__':
#     assert Solution().generateParenthesis(0) == [], "Edge 1"
#     assert Solution().generateParenthesis(1) == ['()'], "Edge 2"

#     assert set(Solution().generateParenthesis(2)) == set(["(())", "()()"])
#     assert set(Solution().generateParenthesis(3)) == set(["((()))", "(()())", "(())()", "()(())", "()()()"])
#     assert set(Solution().generateParenthesis(4)) == set(['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()'])
#     print('all passed')


print(Solution().generateParenthesis(0))
print(Solution().generateParenthesis(1))
print(Solution().generateParenthesis(2))
print(Solution().generateParenthesis(3))
a = Solution().generateParenthesis(4)
print(len(a))

print(sorted(a))

# ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']
# ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']
#       x          x            x           x           x           x           x
# '(())(())'

# TODO Need to learn why it works

