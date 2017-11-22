# You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits. The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).

# Input: A matrix as a list of lists with integers.
# Output: Whether or not a sequence exists as a boolean.

def checkio(matrix):
index = len(matrix)
# obtain veritical result in a list
ver_result = []
for i in range(index-3):
for j in range(index):
temp = []
for k in range(4):
temp.append(matrix[i+k][j])
ver_result.append(temp)
# obtain horizontal result in a list
hor_result = []
for i in range(index):
for j in range(index - 3):
temp = []
for k in range(4):
temp.append(matrix[i][j+k])
hor_result.append(temp)
# obtain axis start from NE corner
NE_axis = []
for i in range(index - 3):
for j in range(3, index):
temp = []
for k in range(4):
temp.append(matrix[i+k][j-k])
NE_axis.append(temp)
# obtain axis start from NW corner
NW_axis = []
for i in range(index - 3):
for j in range(0, index - 3):
temp = []
for k in range(4):
temp.append(matrix[i+k][j+k])
NW_axis.append(temp)
def verify(matrix):
return any(xlist.count(xlist[0]) == len(xlist) for xlist in matrix)
return verify(hor_result) or verify(ver_result) \
or verify(NW_axis) or verify(NE_axis)

if __name__ == '__main__':
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
