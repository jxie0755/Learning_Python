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

class Solution(object):

    ### Version B
    ### Simplified stack, calculate * and / on the run, then finish with + and -
    ### This is 10 times faster but still only beat 25.67%

    def calc(self, n1, op, n2):
        """
        n1, n2 will be numbers
        op will be operator in str
        """
        if op == '*':
            return n1 * n2
        if op == '/':
            return n1 // n2
        if op == '+':
            return n1 + n2
        if op == '-':
            return n1 - n2

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = '0123456789'
        op = []
        number = []
        priority = False

        temp = ''
        for i in s:
            if i in n:
                temp += i
            elif i in '+-':
                number.append(int(temp))
                op.append(i)
                temp = ''

                # when meet next operator + and -, condentse all previous stacks to one number
                while len(number) >= 2:
                    number.append(self.calc(number.pop(-2), op.pop(-2), number.pop()))
                priority = False

            elif i in '*/':
                number.append(int(temp))
                op.append(i)
                temp = ''
                # when meet next operator * and / only calculate if previous calculation is also * and /
                # Otherwise, hold for priority
                if priority and len(number) >= 2:
                    number.append(self.calc(number.pop(-2), op.pop(-2), number.pop()))
                priority = True

        number.append(int(temp))
        while len(number) >= 2:
            number.append(self.calc(number.pop(-2), op.pop(), number.pop()))

        return number[-1]





if __name__ == '__main__':
    assert Solution().calculate("3+2*2") == 7, 'Example 1'
    assert Solution().calculate(" 3/2 ") == 1, 'Example 2'
    assert Solution().calculate(" 3+5 / 2 ") == 5, 'Example 3'
    assert Solution().calculate("282-1*2*13-30-2*2*2/2-95/5*2+55+804+3024") == 4067, 'Additional'
    print('all passed')
