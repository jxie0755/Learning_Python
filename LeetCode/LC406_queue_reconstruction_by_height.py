"""
https://leetcode.com/problems/queue-reconstruction-by-height/
LC406 Queue Reconstruction by Height
Medium

You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

It is guaranteed that the queue can be reconstructed.
"""

from typing import *

class Solution_A:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        translate = [[] for _ in range(len(people))]
        for p in people:
            translate[p[1]].append(p)
        for x in translate:
            x.sort()
        for x in translate:
            print(x)


testCase = Solution_A()
testCase.reconstructQueue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]])

# if __name__ == '__main__':
#     testCase = Solution_A()
#
#     assert testCase.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]) == [
#         [5, 0], [7, 0],
#         [5, 2],
#         [6, 1],
#         [4, 4],
#         [7, 1]
#     ], "Example 1"
#
#     assert testCase.reconstructQueue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]) == [
#         [4, 0], [5, 0],
#         [2, 2], [3, 2],
#         [1, 4],
#         [6, 0]
#     ], "Example 2"
#
#     print("All passed")





