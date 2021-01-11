# P326 Power of Three
# Easy


# Given an integer, write a function to determine if it is a power of three.

# Follow up:
# Could you do it without using any loop / recursion?

import math


class Solution:

    # Version A, O(LogN), used loop
    def isPowerOfThree(self, n: int) -> bool:
        exp = 0
        while 3 ** exp < n:
            exp += 1

        return 3 ** exp == n

    def isPowerOfThree(self, n):
        # STD ans
        return n > 0 and (math.log10(n) / math.log10(3)).is_integer()


if __name__ == "__main__":
    assert Solution().isPowerOfThree(1), "Edge 1"
    assert not Solution().isPowerOfThree(2), "Edge 2"
    assert Solution().isPowerOfThree(27), "Example 1"
    assert not Solution().isPowerOfThree(0), "Example 2"
    assert Solution().isPowerOfThree(9), "Example 3"
    assert not Solution().isPowerOfThree(45), "Example 3"
    assert not Solution().isPowerOfThree(19684), "Example 4"
    print("All passed")
