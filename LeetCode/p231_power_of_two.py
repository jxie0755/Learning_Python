# P231 Power of Two
# Easy


# Given an integer, write a function to determine if it is a power of two.


class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        elif n == 1:
            return True

        cur = 2
        while cur < n:
            cur *= 2
        return cur == n



if __name__ == '__main__':
    assert Solution().isPowerOfTwo(-1) == False, 'Edege 1'
    assert Solution().isPowerOfTwo(0) == False, 'Edge 2'
    assert Solution().isPowerOfTwo(1) == True, 'Example 1'
    assert Solution().isPowerOfTwo(16) == True, 'Example 2'
    assert Solution().isPowerOfTwo(218) == False, 'Example 3'
    print('all passed')
