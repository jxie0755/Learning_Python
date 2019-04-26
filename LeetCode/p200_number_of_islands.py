# P200 Number of Islands
# Medium


# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


class LC200UnionFind(object):
    ### Designed for Leetcode P200
    ### Weighted and NOT path compressed
    def __init__(self, size):
        self.id = list(range(size))
        self.sz = [1] * size           # track the size of each tree (only on the root)

    def root(self, p):
        while self.id[p] != p:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def groupCount(self):
        count = 0
        for i in range(len(self.id)):
            if self.id[i] == i:
                count += 1
        return count

    def union(self, p, q):
        rt_p = self.root(p)
        rt_q = self.root(q)

        if rt_p != rt_q:
            if self.sz[q] <= self.sz[p]:
                self.id[rt_q] = rt_p       # assign the new root to the bigger tree
                self.sz[rt_p] += self.sz[rt_q]  # update the size of the new root
            else:
                self.id[rt_p] = rt_q
                self.sz[rt_q] += self.sz[rt_p]

class Solution:

    def numIslands(self, grid) -> int:
        if not grid:
            return 0

        def translate(coor):
            """translate coor to UF id's index
            the grid is added buffer area, so coor start from (1,1) to (row, col)
            """
            x, y = coor[0], coor[1]
            return x * col + y

        def isValid(coor):
            x, y = coor[0], coor[1]
            if x < 0 or x > row - 1 or y < 0 or y > col - 1:
                return False
            else:
                return True

        def neighbor(coor):
            """return the UF id's index at up, down, left, right"""
            x, y = coor[0], coor[1]
            down = (x+1,y)
            right = (x, y+1)
            candidates = list(filter(isValid, [down, right]))  # 由于按顺序遍历coor, 只需要和右边和下面的link就行, 同样能覆盖全局
            candidates = [translate(i) for i in candidates if grid[i[0]][i[1]] == '1']
            return candidates


        row = len(grid)
        col = len(grid[0])
        N = len(grid) * len(grid[0])
        UF = LC200UnionFind(N)
        for r in range(row):
            for c in range(col):
                coor = (r, c)
                coorval = grid[r][c]
                p = translate(coor)
                if coorval == '1':
                    for q in neighbor(coor):
                        UF.union(p, q)
                else:
                    UF.id[p] = -1
        return UF.groupCount()

# ### Improved by using dict for Union-Find
# class LC200UnionFind_hmp(object):
#     ### Designed for Leetcode P200, with hash-map as the id
#     ### It is still slow
#     def __init__(self, m, n):
#         self.id = {(x, y):(x, y) for x in range(m) for y in range(n)}
#         self.sz = {(x, y):1 for x in range(m) for y in range(n)}  # track the size of each tree (only on the root)
#
#     def root(self, p):
#         while self.id[p] != p:
#             p = self.id[p]
#         return p
#
#     def groupCount(self):
#         count = 0
#         for coor in self.id:
#             if self.id[coor] == coor:
#                 count += 1
#         return count
#
#     def union(self, p, q):
#         rt_p = self.root(p)
#         rt_q = self.root(q)
#
#         if rt_p != rt_q:
#             if self.sz[q] <= self.sz[p]:
#                 self.id[rt_q] = rt_p  # assign the new root to the bigger tree
#                 self.sz[rt_p] += self.sz[rt_q]  # update the size of the new root
#             else:
#                 self.id[rt_p] = rt_q
#                 self.sz[rt_q] += self.sz[rt_p]
#
#
# class Solution:
#
#     def numIslands(self, grid) -> int:
#         if not grid:
#             return 0
#
#         def neighbor(coor):
#             """return the UF id's index at up, down, left, right"""
#             x, y = coor[0], coor[1]
#             up = (x-1, y)
#             down = (x+1,y)
#             left = (x, y-1)
#             right = (x, y+1)
#             candidates = list(filter(isValid, [up, down, left, right]))
#             candidates = [i for i in candidates if grid[i[0]][i[1]] == '1']
#             return candidates
#
#         def isValid(coor):
#             x, y = coor[0], coor[1]
#             if x < 0 or x > row - 1 or y < 0 or y > col - 1:
#                 return False
#             else:
#                 return True
#
#         row = len(grid)
#         col = len(grid[0])
#         UF = LC200UnionFind_hmp(row, col)
#
#         for r in range(row):
#             for c in range(col):
#                 coor = (r, c)
#                 coorval = grid[r][c]
#                 if coorval == '1':
#                     for q in neighbor(coor):
#                         UF.union(coor, q)
#                 else:
#                     UF.id[coor] = None
#
#         return UF.groupCount()



if __name__ == '__main__':
    M0 = []
    assert Solution().numIslands(M0) == 0, 'Edge 1'

    M00 = [
        ['1'],
        ['1']
    ]

    assert Solution().numIslands(M00) == 1, 'Edge 2'

    M1 = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
    ]

    assert Solution().numIslands(M1) == 1, 'Example 1'

    M2 = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1'],
    ]
    assert Solution().numIslands(M2) == 3, 'Example 2'

    print('all passed')
