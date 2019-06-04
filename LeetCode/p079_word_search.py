# P079 Word Search
# Medium


# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

count = 0

class Solution:
    def neighbor(self, board, coor):
        x, y = coor[0], coor[1]
        hmp = dict()
        hmp[(x-1, y)] = board[x-1][y]   # up
        hmp[(x+1, y)] = board[x+1][y]   # down
        hmp[(x, y-1)] = board[x][y-1]   # left
        hmp[(x, y+1)] = board[x][y+1]   # right
        return hmp


    def exist(self, board, word: str):
        # This recursive method passed most cased but exceeded max time when case is long.
        if not board:
            return False

        row, col = len(board), len(board[0])
        N = len(word)

        # 给board周围加一圈'0', 防止检查周围时index找不到
        board = [['0'] * col] + board + [['0'] * col]
        for i in board:
            i.insert(0,'0')
            i.append('0')

        # Starting list
        start = [(r, c) for r in range(1, row+1) for c in range(1, col+1) if board[r][c] == word[0]]

        def helper(board, coor, word, result):
            result.append(coor)
            if len(result) == N:
                return True
            hmp = self.neighbor(board, coor)
            nextcoor = [c for c in hmp if hmp[c] == word[1] and c not in result]
            if nextcoor:
                return any([helper(board, c, word[1:], result[:]) for c in nextcoor])
            else:
                return False

        return any([helper(board, i, word, []) for i in start])

if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    assert Solution().exist(board, 'ABCCED'), 'Example 1'
    assert Solution().exist(board, 'SEE'), 'Example 2'
    assert not Solution().exist(board, 'ABCB'), 'Example 3'

    board = [
        ["b","a","b","a","a","a"],
        ["b","b","b","a","a","a"],
        ["b","a","b","a","b","a"]
    ]

    assert Solution().exist(board, 'ba'), 'Additional 1'

    long = [
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
         "a", "a", "a", "a", "a", "a", "a", "b"]
    ]
    target = "baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # print(Solution().exist(long, target))

    print('all passed')
