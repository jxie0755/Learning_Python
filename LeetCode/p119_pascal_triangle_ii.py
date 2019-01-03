# p119 Pasical's Trianle II
# Easy

# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
# Note that the row index starts from 0.

# Follow up: Could you optimize your algorithm to use only O(k) extra space?

class Solution:
    def getRow_old(self, rowIndex):
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
            result = [1] + [result[i] + result[i-1] for i in range(1, len(result))] + [1]  # 用list comprehension不好吗?
            current += 1

        return result

    # Try to use O(k) space.
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        current = 2
        result = [1, 2]

        while current < rowIndex:
            x = result[-1]
            result = [1] + [result[i] + result[i+1] for i in range(current // 2)]  # 不如只求一半,另一半用复制法节省时间 # 确实快了一倍
            if current % 2 != 0:
                result += [x*2]

            current += 1

        if rowIndex % 2 == 0:
            return result + result[-2::-1]
        else:
            return result + result[::-1]


if __name__ == '__main__':
    assert Solution().getRow(2) == [1, 2, 1]
    assert Solution().getRow(3) == [1, 3, 3, 1]
    assert Solution().getRow(4) == [1, 4, 6, 4, 1]
    print('all passed')
