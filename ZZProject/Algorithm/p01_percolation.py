# Give a matrix of values @ m * n, in two status, pass or block (1 and 0)
# Determine if there is a open path that could go from the top to bottom

class Percolation:

    def __init__(self, data):
        self.matrix = data
        self.m = len(data)

    def isPercolate(self, row1, row2):
        open_1 = [i for i in range(len(row1)) if row1[i] == 1]
        width = 0
        for i in open_1:
            if row2[i] == 1:
                width += 1
        return width

    # def narrowpoint(self):
    #     hmp = dict()
    #     hmp[0] = self.matrix[0].count(1)
    #     for i in range(self.m - 1):
    #         r1, r2 = self.matrix[i], self.matrix[i + 1]
    #         hmp[i+1] = self.isPercolate(r1, r2)
    #     narrow_point = min(hmp, key=lambda x:hmp[x])
    #     print('Narrow Point at', narrow_point)
    #     print('Narrow Width is', hmp[narrow_point])
    #
    #     return hmp

    def determination(self):
        for i in range(self.m-1):
            r1, r2 = self.matrix[i], self.matrix[i+1]
            if not self.isPercolate(r1, r2):
                return False
        return True





if __name__ == '__main__':
    sample_Y1 = [
        [0, 0, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1],
    ]

    sample_N1 = [
        [1, 0, 0, 0, 1, 1, 0, 1],
        [0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 1, 1, 0, 1],
        [0, 0, 1, 0, 0, 0, 1, 0],
    ]

    sample_N2 = [
        [0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0],
    ]

    Q1 = Percolation(sample_Y1)
    Q2 = Percolation(sample_N1)
    Q3 = Percolation(sample_N2)

    assert Q1.determination(), "Example 1"
    assert not Q2.determination(), "Example 2"
    assert not Q3.determination(), "Example 3"

    print(Q1.narrowpoint())
    print(Q2.narrowpoint())

    print('All passed')
