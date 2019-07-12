# P263 Ugly Number
# Easy

# Write a program to check whether a given number is an ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5


# Note:
# 1 is typically treated as an ugly number.
# Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].

class Solution:
    def isUgly(self, num: int) -> bool:
        # Time O(logN), Space O(1)
        if num == 1:
            return True

        def remove_ugly_factor(num):
            for i in [2,3,5]:
                if num % i == 0:
                    return num // i
            return num

        num, old_num = remove_ugly_factor(num), num
        while num != old_num:
            num, old_num = remove_ugly_factor(num), num

        return num == 1


class Solution(object):
    # @param {integer} num
    # @return {boolean}
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num //= i
        return num == 1


if __name__ == "__main__":
    assert Solution().isUgly(0) is False, "Edge 1"
    assert Solution().isUgly(1) is True, "Edge 2"
    assert Solution().isUgly(6) is True, "Example 1"
    assert Solution().isUgly(8) is True, "Example 2"
    assert Solution().isUgly(14) is False, "Example 3"
    print("all passed")
