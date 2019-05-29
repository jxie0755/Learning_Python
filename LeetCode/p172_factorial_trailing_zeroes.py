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
            tz_factor = 0
            while result % (10**(tz_factor+1)) == 0:
                tz_factor += 1
            tz += tz_factor
            result = result // (10**tz_factor)
        return tz




if __name__ == '__main__':
    assert Solution().trailingZeroes(0) == 0, 'Edge 0'
    assert Solution().trailingZeroes(1) == 0, 'Edge 1'
    assert Solution().trailingZeroes(3) == 0, 'Example 1'
    assert Solution().trailingZeroes(5) == 1, 'Example 2'
    assert Solution().trailingZeroes(20) == 4, 'Additional'

    print('all passed')

