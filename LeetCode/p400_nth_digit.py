# P400 Nth Digit
# Easy


# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n < 231).


class Solution:

    # Version A, brutal force
    # Exceed max time limit
    def findNthDigit(self, n: int) -> int:
        count = 0
        check = 0
        for i in range(1, n+1):
            add_on = len(str(i))
            if count + add_on >= n:
                check = i
                break
            else:
                count += add_on

        return int(str(i)[n-count-1])


    # Version B, counting method
    # from range(1, 10), 9 numbers
    # from range(10, 100), 90 numbers
    # from range(10**n, 10**(n+1)), 9 * 10**n
    def findNthDigit(self, n: int) -> int:

        count = 0
        deci = 0
        all_digit_count = 9
        while count + all_digit_count < n:
            count += all_digit_count
            deci += 1
            all_digit_count = 10**deci * 9 * (deci+1)
        # Up to here we know the number is at least >= 10**deci

        rest = n - count   # need rest digit
        i, k = divmod(rest, deci+1) # each number provide deci+1 digit

        if k == 0:
            sample = 10**deci - 1 + i
            return int(str(sample)[-1])
        else:
            sample = 10 ** deci + i
            return int(str(sample)[k-1])



if __name__ == '__main__':

    assert Solution().findNthDigit(3) == 3, 'Example 1'
    assert Solution().findNthDigit(11) == 0, 'Example 2'
    assert Solution().findNthDigit(15) == 2, 'Example 3'

    assert Solution().findNthDigit(10000000) == 7, 'Long'
    print('all passed')
