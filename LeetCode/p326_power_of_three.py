# P326 Power of Three
# Easy


# Given an integer, write a function to determine if it is a power of three.

# Follow up:
# Could you do it without using any loop / recursion?

class Solution:

    # O(LogN), used loop
    def isPowerOfThree(self, n: int) -> bool:
        while n > 3:
            n //= 3
        if n == 3:
            return True
        else:
            return False


if __name__ == '__main__':
    assert Solution().isPowerOfThree(27), 'Example 1'
    assert not Solution().isPowerOfThree(0), 'Example 2'
    assert Solution().isPowerOfThree(9), 'Example 3'
    assert not Solution().isPowerOfThree(45), 'Example 3'
    print('all passed')

