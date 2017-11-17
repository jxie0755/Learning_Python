# Input: A map as a list of lists with 1 or 0.
# Output: The sizes of island as a list of integers.

def checkio(land_map):
    return [1]



# if __name__ == '__main__':
#     assert checkio([[0, 0, 0, 0, 0],
#                     [0, 0, 1, 1, 0],
#                     [0, 0, 0, 1, 0],
#                     [0, 1, 0, 0, 0],
#                     [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
#     assert checkio([[0, 0, 0, 0, 0],
#                     [0, 0, 1, 1, 0],
#                     [0, 0, 0, 1, 0],
#                     [0, 1, 1, 0, 0]]) == [5], "2nd example"
#     assert checkio([[0, 0, 0, 0, 0, 0],
#                     [1, 0, 0, 1, 1, 1],
#                     [1, 0, 0, 0, 0, 0],
#                     [0, 0, 1, 1, 1, 0],
#                     [0, 0, 0, 0, 0, 0],
#                     [0, 1, 1, 1, 1, 0],
#                     [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
#     print('done')


a = ([[1, 0, 0, 0, 0],
      [0, 0, 1, 1, 0],
      [0, 0, 0, 1, 0],
      [0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0]])
print(checkio(a))
