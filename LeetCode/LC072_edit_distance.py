"""
https://leetcode.com/problems/edit-distance/
P072 Edit Distance
Hard

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character

Input:
word1 = "horse",
word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Input:
word1 = "intention",
word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

class Solution_A:
    def minDistance(self, word1: str, word2: str) -> int:
        # TODO
        pass


    def substring_LS(self, iterable):
        result = []
        for lenth in range(len(iterable), 0, -1):
            for i in range(len(iterable) - lenth + 1):
                result.append(iterable[i:i + lenth])
        return result






# Solution().minDistance('intention', 'execution')


if __name__ == "__main__":
    testCase = Solution_A()
    assert testCase.minDistance("", "ros") == 3, "Edge 0"
    assert testCase.minDistance("ros", "") == 3, "Edge 1"
    assert testCase.minDistance("a", "b") == 3, "Edge 2"

    assert testCase.minDistance("horse", "ros") == 3, "Eample 1"
    assert testCase.minDistance("intention", "execution") == 5, "Eample 2"
    print("All passed")
