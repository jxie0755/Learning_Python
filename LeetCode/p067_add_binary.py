# p067 Add Binary
# Easy

# Given two binary strings, return their sum (also a binary string)

# """
# :type a: str
# :type b: str
# :rtype: str
# """

class Solution:
    def addBinary(self, a, b):
        ### use python characteristics
        return '{:b}'.format(int(a, 2) + int(b, 2))

    def addBinary(self, a, b):
        ### avoid python characteristics
        def bi_to_deci(target):
            return sum([int(target[::-1][i]) * 2 ** i for i in range(len(target))])

        def deci_to_bi(target):
            if target:
                ans = ''
                while target != 0:
                    target, digit = divmod(target, 2)
                    ans = str(digit) + ans
                return ans
            return '0'

        return deci_to_bi(bi_to_deci(a) + bi_to_deci(b))


if __name__ == '__main__':
    assert Solution().addBinary('11', '1') == '100', 'regular'
    assert Solution().addBinary('0', '0') == '0', 'zero'
    print('all passed')
