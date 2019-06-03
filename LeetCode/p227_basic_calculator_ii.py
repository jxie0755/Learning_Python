# P227 Basic Calculator II
# Medium

# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.


class Solution(object):

    ### Version A
    ### Use the op stack and number staock
    ### This is quite slow
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = '0123456789'

        number, op = [], []
        temp = ''
        for i in s:
            if i in nums:
                temp += i
            elif i in '*/+-':
                number.append(int(temp))
                temp = ''
                op.append(i)
        number.append(int(temp))

        k = 0
        while k != len(op):
            o = op[k]
            if o in '*/':
                if o == '*':
                    number[k] = number[k] * number[k + 1]
                if o == '/':
                    number[k] = number[k] // number[k + 1]
                number.pop(k + 1)
                op.pop(k)
            else:
                k += 1

        k = 0
        while k != len(op):
            o = op[k]
            if o == '+':
                number[k] = number[k] + number[k + 1]
            if o == '-':
                number[k] = number[k] - number[k + 1]
            number.pop(k + 1)
            op.pop(k)

        return number[0]


print(Solution().calculate("3+2*2"))

if __name__ == '__main__':
    assert Solution().calculate("3+2*2") == 7, 'Example 1'
    assert Solution().calculate(" 3/2 ") == 1, 'Example 2'
    assert Solution().calculate(" 3+5 / 2 ") == 5, 'Example 3'
    print('all passed')
