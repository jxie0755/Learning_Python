# LC172 Factorial Trailing Zeroes
# Easy

# Given an integer n, return the number of trailing zeroes in n!.
# Note: Your solution should be in logarithmic time complexity.

class Solution(object):

    # Version A
    # Brutal force, adding trailing zero, and keep last digit that is not 0
    # This will fail exceeding max time limit
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        result = 1
        tz = 0
        for i in range(1, n + 1):
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
    # STD ans
    # @return an integer
    # 由于只有2*5能得到尾数10, 而因数2远多于因数5, 所以只要知道从1到n总共能拆解出多少个因数5就行
    # 注意25 = 5 * 5 是两个5, 所以要用循环找遍所有的//5
    def trailingZeroes(self, n):
        result = 0
        while n > 0:
            result += n // 5
            n //= 5
        return result


# 简单理解版本
class Solution(object):
    # Version B
    # 逐个检查1-n中每个数,能拆出多少个5因数
    # 但是这样还是慢这样为N(logN)
    def trailingZeroes(self, n):
        result = 0
        for x in range(1, n + 1):
            while True:
                a, b = divmod(x, 5)
                if b == 0:
                    result += 1
                    x = a
                else:
                    break
        return result


# 简单理解版本B
class Solution(object):
    # Version C
    # 逐个检查5^n因数个数
    def trailingZeroes(self, n):
        result = 0
        factor = 1
        while n // (5 ** factor) != 0:
            result += n // (5 ** factor)
            factor += 1
        return result


if __name__ == "__main__":
    assert Solution().trailingZeroes(0) == 0, "Edge 1"
    assert Solution().trailingZeroes(1) == 0, "Edge 2"
    assert Solution().trailingZeroes(3) == 0, "Example 1"
    assert Solution().trailingZeroes(5) == 1, "Example 2"
    assert Solution().trailingZeroes(20) == 4, "Additional 1"
    assert Solution().trailingZeroes(3743) == 932, "Additional 2"
    print(Solution().trailingZeroes(1808548329))
    print("All passed")
