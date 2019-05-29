# P172 Factorial Trailing Zeroes
# Easy

# Given an integer n, return the number of trailing zeroes in n!.
# Note: Your solution should be in logarithmic time complexity.

class Solution(object):

    ### Version A
    ### Brutal force, adding trailing zero, and keep last digit that is not 0
    ### This will fail exceeding max time limit
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        result = 1
        tz = 0
        for i in range(1, n+1):
            result *= i
            while True:
                a, b = divmod(result, 10)
                if b == 0:
                    tz += 1
                    result = a
                else:
                    result = result % 100
                    break
        return tz


class Solution(object):
    # @return an integer
    def trailingZeroes(self, n):
        result = 0
        while n > 0:
            result += n // 5
            n //= 5
        return result


if __name__ == '__main__':
    assert Solution().trailingZeroes(0) == 0, 'Edge 0'
    assert Solution().trailingZeroes(1) == 0, 'Edge 1'
    assert Solution().trailingZeroes(3) == 0, 'Example 1'
    assert Solution().trailingZeroes(5) == 1, 'Example 2'
    assert Solution().trailingZeroes(20) == 4, 'Additional 1'
    assert Solution().trailingZeroes(3743) == 932, 'Additional 2'
    print(Solution().trailingZeroes(1808548329))
    print('all passed')

