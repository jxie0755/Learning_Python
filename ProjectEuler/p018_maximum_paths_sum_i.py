# P018 Maximum path sum I


# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

#    3
#   7 4
#  2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:
#                             75
#                           95  64
#                         17  47  82
#                       18  35  87  10
#                     20  04  82  47  65
#                   19  01  23  75  03  34
#                 88  02  77  73  07  63  67
#               99  65  04  28  06  16  70  92
#             41  41  26  56  83  40  80  70  33
#           41  48  72  33  47  32  37  16  94  29
#         53  71  44  65  25  43  91  52  97  51  14
#       70  11  33  28  77  73  17  78  39  68  17  57
#     91  71  52  38  17  14  91  43  58  50  27  29  48
#   63  66  04  68  89  53  67  30  73  16  69  87  40  31
# 04  62  98  27  23  09  70  98  73  93  38  53  60  04  23

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)


# process the data first
def process(data):
    with open(data) as f_obj:
        content = f_obj.readlines()
    result = []
    for i in content:
        temp = i.strip().split(' ')
        temp = [int(j) for j in temp]
        result.append(temp)
    return result


# Brutal force
def max_path_sum_i(T):
    """calculate the max sum of a route in triangle

    T as triangle: a nested list as triangle grid
    return: the max sum of the numbers in one route of the triangle grid
    """

    depth = len(T)
    paths = [[T[0][0]]]
    row = 1
    while row < depth:
        temp = []
        for i in paths:
            temp += [i[:], i[:]]
        paths = add_row(temp, T[row])
        row += 1

    # for print the result
    for i in paths:
        print(i)

    return sum(max(paths, key=sum))


def add_row(current_paths, row):
    """process row to get ready for add tuple

    keep the first and last item and duplicate items in the middle in the same sequence
    example: [1,2,3] should become [1,2,2,3], then add to [[A],[B],[C],[D]] and return
    [[A,1],[B,2],[C,2],[D,3]]

    current_paths: a list of list of numbers
    row: a list of numbers
    return: a list of numbers
    """

    to_add = [row[0]]
    index = 1
    while index <= len(row) - 2:
        to_add += [row[index], row[index]]
        index += 1
    to_add.append(row[-1])

    j = 0
    while j < len(current_paths):
        current_paths[j].append(to_add[j])
        j += 1

    return current_paths

if __name__ == '__main__':
    print(max_path_sum_i(process('p018_data_test.txt')))
    # print(max_path_sum_i(process('p018_data.txt')))

