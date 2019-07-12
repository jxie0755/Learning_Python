# Input: A map as a list of lists with 1 or 0.
# Output: The sizes of island as a list of integers.

def checkio(land_map):
    return [1]



# if __name__ == "__main__":
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
#     print("done")


land_map = ([[1, 0, 0, 0, 0],
             [0, 0, 1, 0, 1],
             [0, 0, 1, 1, 1],
             [0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0]])

temp_list = []
for i in range(len(land_map)):
    for x in range(len(land_map)):
        if land_map[i][x] == 1:
            collect = int(str(i) + str(x))
            temp_list.append(collect)
print(temp_list)

final = []
temp = []
tempU =[]
for i in temp_list:
    up, down, left, right, up_left, upright, down_left, down_right = x-10, x+10, x-1, x+1, x-11, x-9, x+9, x+11
    neighbors = [up, down, left, right, up_left, upright, down_left, down_right]

# job not done.
# future work includes finish the check neighbor processing to group the numbers for islands.
