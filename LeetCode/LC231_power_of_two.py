# P231 Power of Two
# Easy


# Given an integer, write a function to determine if it is a power of two.


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        elif n == 1:
            return True

        cur = 2
        while cur < n:
            cur *= 2
        return cur == n


class Solution(object):
    # Time O(1) Space O(1)
    # 利用位运算, 也就是把n转换成二进制数, 2的幂在二进制中必为 1000...
    # 这样n-1就必为0111....
    # 利用&对比各位, 必然每一位都不相同, 则结果为0
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0


if __name__ == "__main__":
    assert Solution().isPowerOfTwo(-1) == False, "Edege 1"
    assert Solution().isPowerOfTwo(0) == False, "Edge 2"
    assert Solution().isPowerOfTwo(1) == True, "Example 1"
    assert Solution().isPowerOfTwo(16) == True, "Example 2"
    assert Solution().isPowerOfTwo(218) == False, "Example 3"
    print("all passed")
