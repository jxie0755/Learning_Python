# P279 Perfect Squares
# Medium


# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

class Solution(object):
    def SQlist(self, n):
        """find all possible square number up to n"""
        result = []
        for i in range(1, n+1):
            if i**2 <= n:
                result.append(i ** 2)
            else:
                break
        return result



    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        sqlist = self.SQlist(n)
        print(sqlist)
        result = 0
        while sqlist and n:
            x, n = divmod(n, sqlist.pop())
            result += x

        return result



if __name__ == '__main__':
    assert Solution().numSquares(1) == 1, 'Edge, just 1'
    assert Solution().numSquares(12) == 3, 'Example 1:  4+4+4'
    assert Solution().numSquares(13) == 2, 'Example 2:  4+9'

    assert Solution().numSquares(101) == 2, 'Example 3:  100 + 1'
    assert Solution().numSquares(99) == 4,  'Example 4:  81 + 16 + 1 + 1'

    print('all passed')


