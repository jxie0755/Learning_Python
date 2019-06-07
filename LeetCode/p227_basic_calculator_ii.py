# P227 Basic Calculator II
# Medium

# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.


class Solution(object):

    # Version A
    # Use the op stack and number staock
    # This is quite slow
    def calculate(self, s: str) -> int:
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

    # Version B
    # Simplified stack, calculate * and / on the run, then finish with + and -
    # This is 10 times faster and passed the same speed as STD ans
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

    def calculate(self, s: str) -> int:
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


class Solution(object):

    # STD ans, this will inlcude the use of "()"
    # @param {string} s
    # @return {integer}

    # THis modify the stacks directly by removing the last two item and add calculated result
    def compute(self, operands, operators):
        left, right = operands.pop(), operands.pop()
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)
        elif op == '*':
            operands.append(left * right)
        elif op == '/':
            operands.append(left // right)

    def calculate(self, s: str) -> int:
        operands, operators = [], []
        operand = ""
        for i in reversed(range(len(s))):
            elem = s[i]
            if elem.isdigit():
                operand += elem
                if i == 0 or not s[i-1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif elem == ')' or elem == '*' or elem == '/':
                operators.append(s[i])
            elif elem == '+' or elem == '-':
                while operators and \
                      (operators[-1] == '*' or operators[-1] == '/'):
                    self.compute(operands, operators)
                operators.append(elem)
            elif elem == '(':
                while operators[-1] != ')':
                    self.compute(operands, operators)
                operators.pop()

        while operators:
            self.compute(operands, operators)

        return operands[-1]



if __name__ == '__main__':
    assert Solution().calculate("3+2*2") == 7, 'Example 1'
    assert Solution().calculate(" 3/2 ") == 1, 'Example 2'
    assert Solution().calculate(" 3+5 / 2 ") == 5, 'Example 3'
    assert Solution().calculate("282-1*2*13-30-2*2*2/2-95/5*2+55+804+3024") == 4067, 'Additional 1'
    # assert Solution().calculate("(3-1)*(4-1)") == 6, 'Additional 2'

    print('all passed')
