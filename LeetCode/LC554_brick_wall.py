"""
https://leetcode.com/problems/brick-wall/
LC553 Brick Wall
Medium

There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.
"""

from typing import *

class Solution_A:
    def leastBricks(self, wall: List[List[int]]) -> int:
        total_length = sum(wall[0])

        hmp = {}
        for layer in wall:
            NL = [0]
            for i in layer:
                NL.append(NL[-1]+i) # this will avoid key value 0
                if NL[-1] not in hmp:
                    # avoid create hmp with every value, just add on the run when new value shows up
                    # this saves time when one brick is very long
                    hmp[NL[-1]] = 1
                else:
                    hmp[NL[-1]] += 1

        hmp[total_length] = 0 # adjust back the max_length value to be 0
        max_L = max(hmp, key=lambda i: hmp[i])
        return len(wall) - hmp[max_L]



if __name__ == '__main__':
    testCase = Solution_A()

    assert testCase.leastBricks([
        [1, 2, 2, 1],
        [3, 1, 2],
        [1, 3, 2],
        [2, 4],
        [3, 1, 2],
        [1, 3, 1, 1]
    ]) == 2, "Example 1"

    assert testCase.leastBricks([
        [1],
        [1],
        [1]
    ]) == 3, "Example 2"

    assert testCase.leastBricks([
        [2],
        [2],
        [2]
    ]) == 3, "Additional edge 1"

    assert testCase.leastBricks([
        [100000000],
        [100000000],
        [100000000]
    ]) == 3, "Additional edge 1"


    print("All passed")


