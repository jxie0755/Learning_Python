# P227 Basic Calculator II
# Medium

# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        pass


if __name__ == '__main__':
    assert Solution().calculate("3+2*2") == 7, 'Example 1'
    assert Solution().calculate(" 3/2 ") == 1, 'Example 2'
    assert Solution().calculate(" 3+5 / 2 ") == 5, 'Example 3'
    print('all passed')
