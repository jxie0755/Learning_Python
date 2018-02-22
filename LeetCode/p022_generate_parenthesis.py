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


if __name__ == '__main__':
    assert Solution().generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    print('all passed')

print(Solution().generateParenthesis(0))
print(Solution().generateParenthesis(3))

# TODO Need to learn why it works
