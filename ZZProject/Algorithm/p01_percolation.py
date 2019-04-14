# Give a matrix of values @ m * n, in two status, pass or block (1 and 0) or ("O" and "X")
# Determine if there is a open path that could go from the top to bottom

class Percolation:

    def __init__(self, data):
        self.matrix = data
        self.m = len(data)
        self.n = len(data[0])

    def getRow(self, i):
        return self.matrix[i]

    def checkRow(self, row, indexes):
        new_indexes = []
        for i in indexes:
            if row[i] == 1:
                new_indexes.append(i)
        return new_indexes

    def determination(self):
        for i in range(self.m):
            row = self.getRow(i)
            opens = self.checkRow(row)
            if opens:
                pass
            else:
                return False

def checkRow(row, indexes):
    new_indexes = []
    for i in indexes:
        if row[i] == 1:
            new_indexes.append(i)
    return new_indexes

idx = [0, 1, 2, 3, 4, 5, 6, 7]
row = [0, 0, 1, 0, 0, 1, 0, 0]
print(checkRow(row, idx))

# if __name__ == '__main__':
#     sample_Y1 = [
#         [0, 0, 0, 0, 0, 1, 0, 0],
#         [0, 0, 1, 0, 0, 1, 0, 0],
#         [0, 0, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 1, 0, 0, 1, 0],
#         [0, 0, 1, 0, 1, 0, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 1],
#         [0, 0, 0, 0, 0, 0, 1, 1],
#     ]
#
#     sample_N1 = [
#         [0, 0, 0, 0, 0, 1, 0, 0],
#         [0, 0, 1, 0, 0, 1, 0, 0],
#         [0, 0, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 1, 1, 0, 1, 0],
#         [0, 0, 1, 0, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 1],
#         [0, 0, 1, 0, 1, 0, 1, 0],
#     ]
