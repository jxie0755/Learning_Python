# P202 Happy Number
# Easy


# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.


class Solution:
    def isHappy(self, n):
        ### Regular method, process n untill repeating
        """
        :type n: int
        :rtype: bool
        """
        def process(n):
            result = 0
            while n != 0:
                n, digit = divmod(n, 10)
                result += digit ** 2
            return result

        hashtable = {}
        while n not in hashtable:
            hashtable[n] = 1
            n = process(n)

        return n == 1

if __name__ == '__main__':
    assert Solution().isHappy(19) is True, 'Example 1'
    print('all passed')




