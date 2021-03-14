"""
https://leetcode.com/problems/pascals-triangle-ii/
LC119 Pasical's Trianle II
Easy

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.

Follow up: Could you optimize your algorithm to use only O(k) extra space?
"""
from typing import *

class Solution_A1:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        Quick iteration
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        row = [1, 1]
        for i in range(1, rowIndex):
            new_row = [1]
            for j in range(i):
                new_row.append(row[j] + row[j+1])
            new_row.append(1)
            row = new_row

        return row


if __name__ == "__main__":
    testCase = Solution_A1()

    assert testCase.getRow(3) == [1, 3, 3, 1], "Example 1"
    assert testCase.getRow(0) == [1], "Example 2"
    assert testCase.getRow(1) == [1, 1], "Example 3"

    print("All passed")
