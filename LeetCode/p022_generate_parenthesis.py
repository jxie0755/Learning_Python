# p22 Generate Parentheses
# Medium

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# """
# :type n: int
# :rtype: List[str]
# """

class Solution:
    def generateParenthesis(self, n):
        base = []
        for i in range(1, n+1):  # this will include 0 and above
            base.append(i*'()')
        return base

# if __name__ == '__main__':
#     assert Solution().generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
#     print('all passed')

print(Solution().generateParenthesis(0))
print(Solution().generateParenthesis(3))

