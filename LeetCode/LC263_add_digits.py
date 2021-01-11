# P263 Add Digits
# Easy


# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

class Solution:
    def addDigits(self, num: int) -> int:
        # O(log(len(n))) ?
        # 即使是iteration速度也是很快的,数字之和缩小的速度非常之快

        def process(num):
            result = 0
            while num != 0:
                num, digit = divmod(num, 10)
                result += digit
            return result

        while num >= 10:
            print(num)
            num = process(num)

        return num


class Solution(object):
    def addDigits(self, num: int) -> int:
        # Time O(1)
        # if num==0:
        #     return 0
        # t = num % 9
        # return t if t else 9

        return 0 if not num else (num - 1) % 9 + 1

    # Explain:
    # 123 = 100 + 20 + 3
    # 123 = 100 + 10*2 + 1*3
    # 注意数学规律: 1 % 9 = 1, 10 % 9 = 1, 100 % 9 = 1 --> 10^n % 9 = 1

    # 123 % 9 = 6
    # 100 % 9 = (100 % 9) * 1 = 1  (也就是数位1)
    # 20 % 9  = (10 % 9) * 2  = 2  (也就是数位2)
    # 3 % 9   = (1 % 9) * 3   = 3  (也就是数位3)
    # 余数就是 1+2+3 = 6

    # 为什么一直累积数字之和永远维持%9的余数呢?
    # 因为 各项数字之和加起来如果大于9, 也就是各部分除以9的余数相加后大于9
    # 那样就继续除以9,直到余数小于10为止.
    # 若各项加起来刚好等于9 是什么意思? 也就是数字可以被9整除,但是当余到9时我们人为终止,因为9已经是个位数了.


if __name__ == "__main__":
    assert Solution().addDigits(1) == 1, "Edge 1"
    assert Solution().addDigits(10) == 1, "Edge 2"

    assert Solution().addDigits(38) == 2, "Example 1"
    print("All passed")
