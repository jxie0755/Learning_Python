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
            for i in prev:
                result += self.dev_parenthesis(i)
            return result + ['()'*n]

    def dev_parenthesis(self, p):
        result = []
        eye = 0
        eye_list = []
        for i in range(0, len(p)-1):
            print(p[i:i + 2])
            if p[i: i + 2] == '()':
                eye_list.append(i+1)
                eye += 1
        for eye_idx in eye_list:
            result.append(p[:eye_idx] + '()' + p[eye_idx:])
        if eye > 1:
            result.append('(' + p + ')')
        return result



# if __name__ == '__main__':
#     assert set(Solution().generateParenthesis(2)) == set(["(())", "()()"])
#     assert set(Solution().generateParenthesis(3)) == set(["((()))", "(()())", "(())()", "()(())", "()()()"])
#     assert set(Solution().generateParenthesis(4)) == set(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])
#     print('all passed')
#
print(Solution().generateParenthesis(0))
print(Solution().generateParenthesis(1))
print(Solution().generateParenthesis(2))
print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(4))


# TODO Need to learn why it works

# "(((())))",    "(((())))"
# "((()))()",    "((()))()"
# "(())(())", # C
# "((())())",    "((())())" # B
# "(())(())",    "(())(())" # C
# "()((()))",    "()((()))"
# "(()(()))",    "(()(()))" # A
# "((())())", # B
# "(()(()))", # A
# "((()()))",    "((()()))"
# "(())()()",    "(())()()"
# "()(())()",    "()(())()"
# "()()(())",    "()()(())"
# "(()()())",    "(()()())"
# "()()()()"     "()()()()"
#
#                "(()())()"
#                "()(()())"
