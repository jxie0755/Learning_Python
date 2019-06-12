# P357 Count Numbers with Unique Digits
# Medium

# Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.


class Solution:

    # Version A, brutal force to check if a number is formed with unique numbers
    def isUnique(self, n):
        digits = []
        while n != 0:
            n, rem = divmod(n, 10)
            digits.append(rem)

        return len(set(digits)) == len(digits)


    def countNumbersWithUniqueDigits(self, n: int) -> int:
        count = 0
        for i in range(10**n):
            if self.isUnique(i):
                count += 1
        return count


class Solution:

    # Version B
    # Recursive method, every n for 10^n, there should be fixed number of non-unique numbers
    # possible combination for 3 digit, every digit before the last has 9 choices, so
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        elif 0 < n <= 9:
            count = 9
            for i in range(9, 9-n+1, -1):
                count *= i
            return count + self.countNumbersWithUniqueDigits(n-1)

        else:
            return self.countNumbersWithUniqueDigits(9)



if __name__ == '__main__':

    assert Solution().countNumbersWithUniqueDigits(0) == 1, 'Edge 0, just 0'
    assert Solution().countNumbersWithUniqueDigits(1) == 10, 'Edge 1, 0 to 9'
    assert Solution().countNumbersWithUniqueDigits(2) == 91, 'Example 1, exclude 9 digits (11,22,33,...99)'

    assert Solution().countNumbersWithUniqueDigits(3) == 739, 'Example 4'
    assert Solution().countNumbersWithUniqueDigits(5) == 32491, 'Example 5'
    assert Solution().countNumbersWithUniqueDigits(9) == 5611771, 'Example Last'
    assert Solution().countNumbersWithUniqueDigits(10) == 5611771, 'Example Exceed Last'

    print('all passed')


