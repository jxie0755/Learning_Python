# P079 Word Search
# Medium


# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    assert Solution().exist('ABCCED'), 'Example 1'
    assert Solution().exist('SEE'), 'Example 2'
    assert not Solution().exist('ABCB'), 'Example 3'
    print('all passed')
