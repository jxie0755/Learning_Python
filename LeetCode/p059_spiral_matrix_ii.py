# P059 Spiral Matrix II
# Medium

# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

class Solution:
    def generateMatrix(self, n):
        val = 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        top, bot, left, right = 0, n - 1, 0, n - 1
        while top <= bot and left <= right:
            for a in range(left, right + 1):
                matrix[top][a] = val
                val += 1
            top += 1
            for b in range(top, bot + 1):
                matrix[b][right] = val
                val += 1
            right -= 1
            for c in range(right, left - 1, -1):
                matrix[bot][c] = val
                val += 1
            bot -= 1
            for d in range(bot, top - 1, -1):
                matrix[d][left] = val
                val += 1
            left += 1

        return matrix


if __name__ == "__main__":
    assert Solution().generateMatrix(1) == [[1]], "Edge 1"

    assert Solution().generateMatrix(3) == [
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5]
    ], "Example 1"

    print("all passed")
