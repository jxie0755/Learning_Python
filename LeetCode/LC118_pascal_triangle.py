"""
https://leetcode.com/problems/pascals-triangle/
LC118 Pascal's triangle
Easy

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""

from typing import *

class Solution_A1:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        a recursion version
        Time limit exceeded
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return self.generate(0) + [[1]]
        elif numRows == 2:
            return self.generate(1) + [[1, 1]]
        else:
            previous = self.generate(numRows - 1)[-1]
            new = [1]
            for i in range(len(previous) - 1):
                new.append(previous[i] + previous[i + 1])
            return self.generate(numRows - 1) + [new + [1]]


class Solution_A2:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Iteration method
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





if __name__ == "__main__":
    testCase = Solution_A1()

    assert testCase.generate(0) == [
    ], "Edge 0"

    assert testCase.generate(5) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ], "Example 1"

    assert testCase.generate(1) == [
        [1]
    ], "Example 2"

    print("All passed")
