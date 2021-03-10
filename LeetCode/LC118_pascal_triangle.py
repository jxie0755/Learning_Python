# LC118 Pascal's triangle
# Easy

# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        current = 2
        result = [[1], [1, 1]]

        while current != numRows:
            new = result[-1][:]
            add_on = [1]
            for i in range(len(new) - 1):
                add_on.append(new[i] + new[i + 1])
            add_on.append(1)

            result.append(add_on)
            current += 1

        return result

    def generate2(self, numRows):
        # a recursion version
        # Time limit exceed
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return self.generate2(0) + [[1]]
        elif numRows == 2:
            return self.generate2(1) + [[1, 1]]
        else:
            previous = self.generate2(numRows - 1)[-1]
            new = [1]
            for i in range(len(previous) - 1):
                new.append(previous[i] + previous[i + 1])
            return self.generate2(numRows - 1) + [new + [1]]


if __name__ == "__main__":
    assert Solution().generate(5) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]

    assert Solution().generate2(5) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]

    print("All passed")
