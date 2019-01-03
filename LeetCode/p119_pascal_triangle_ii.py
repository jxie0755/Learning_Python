# p119 Pasical's Trianle II
# Easy

# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
# Note that the row index starts from 0.

# Follow up: Could you optimize your algorithm to use only O(k) extra space?

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        current = 1
        result = [1, 1]

        while current < rowIndex:
            result = [1] + [result[i] + result[i-1] for i in range(1, len(result))] + [1]
            current += 1

        return result


if __name__ == '__main__':
    assert Solution().getRow(3) == [1,3,3,1]
    print('all passed')