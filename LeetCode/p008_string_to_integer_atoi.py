# P008 String to Integer (atoi)
# Medium


# Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
# Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
# and interprets them as a numerical value.

# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed. (Example 4)
# If no valid conversion could be performed, a zero value is returned.

# Note:
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        hashtable = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
        }

        prefix = {
            '+': 1,
            '-': -1
        }

        low = -2**31
        high = 2**31 - 1

        # Get the numeric first
        found = False
        extract = ''
        for i in str:
            if i == ' ' and not found:
                pass

            elif i in prefix and not found:
                extract += i
                found = True
            elif i in prefix and found:
                break

            elif i in hashtable:
                extract += i
                found = True

            elif i == '.':
                break

            else:
                break

        if not extract:
            return 0
        else:
            result, base = 0, 1
            for i in extract[::-1]:
                if i in hashtable:
                    result += hashtable[i] * base
                    base *= 10
                elif i in prefix:
                    result *= prefix[i]

            if result < low:
                return low
            elif result > high:
                return high
            return result




if __name__ == '__main__':
    assert Solution().myAtoi("ABC") == 0, 'Edge 1'

    assert Solution().myAtoi("42") == 42, 'Example 1'
    assert Solution().myAtoi("   -42") == -42, 'Example 2'
    assert Solution().myAtoi("4193 with words") == 4193, 'Example 3'
    assert Solution().myAtoi("words and 987") == 0, 'Example 4'
    assert Solution().myAtoi("-91283472332") == -2147483648, 'Example 5, return -2^31'

    assert Solution().myAtoi("3.14159") == 3, 'Extra 1'
    assert Solution().myAtoi("+1") == 1, 'Extra 2'
    assert Solution().myAtoi("+-2") == 0, 'Extra 3'
    assert Solution().myAtoi("  -0012a42") == -12, 'Extra 4'
    assert Solution().myAtoi("   +0 123") == 0, 'Extra 5'
    assert Solution().myAtoi("-5-") == -5, 'Extra 6'

    print('all passed')
