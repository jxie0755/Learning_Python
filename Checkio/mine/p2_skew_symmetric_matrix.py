# A = (aij) then the symmetric condition becomes aij = âˆ’aji.
# Input: A square matrix as a list of lists with integers.
# Output: If the matrix is skew-symmetric or not as a boolean.

def checkio(matrix):
    index = len(matrix)
    for i in range(index):
        for j in range(index):
            if matrix[i][j] != -matrix[j][i]:
                return False
    return True

if __name__ == "__main__":
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"
    print("done")
