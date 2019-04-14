# Give a matrix of values @ m * n, in two status, pass or block (1 and 0)
# Determine if there is a open path that could go from the top to bottom

class Percolation:

    def expand_check(self, idx, row):
        """to check the valid tunnel connecting in this row starting from the tunnel point from last tunnel
        then expand the tunnel to all the indexes that is directly linked to tunnel connecting point
        """
        connected_indexes = []
        for i in reversed(range(0, idx)):
            if row[i] == 1:
                connected_indexes.append(i)
            else:
                break
        for i in range(idx, len(row)):
            if row[i] == 1:
                connected_indexes.append(i)
            else:
                break
        return connected_indexes



    def isPercolate(self, pre_tunnel_index, row):
        """Update the tunnel index of at row
        pre_row_index: the tunnel index from last row: List[int]
        row: current row in the matrix: List[int]
        return: the valid tunnel_index of this row: List[int]
        """
        opens = [i for i in pre_tunnel_index if row[i] == 1]
        all_tunnels = []
        for i in opens:
            tunnel = self.expand_check(i, row)
            for i in tunnel:
                if i not in all_tunnels:
                    all_tunnels.append(i)
        return all_tunnels



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

    def determination(self, matrix):
        tunnel = [i for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            tunnel = self.isPercolate(tunnel, matrix[i])
            if not tunnel:
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

    sample_Y2 = [
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
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


    assert Percolation().determination(sample_Y1), "Example 1"
    assert Percolation().determination(sample_Y2), "Example 2"

    assert not Percolation().determination(sample_N1), "Example 3"
    assert not Percolation().determination(sample_N2), "Example 4"


    print('All passed')
