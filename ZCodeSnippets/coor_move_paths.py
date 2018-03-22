# This is code snippet developed from ProjectEuler P015
# https://projecteuler.net/problem=15
# See details in ProjectEuler/p015_lattice_paths.py


from itertools import permutations


# 定义一个函数翻译路径
def move_translate(start, moves):
    """translate moves into a route list of coordinates

    start: starting point tuple as coordinates (x, y)
    moves: a string represents the movement, example, 'RRDDRRDR'

    return: a list of tuples, each tuple represent a cooridnate, as start follows the direction of moves
    """
    path = [start]
    current = start
    for move in moves:
        if move == 'R':
            current = (current[0] + 1, current[1])
        elif move == 'U':
            current = (current[0], current[1] + 1)
        elif move == 'D':
            current = (current[0], current[1] - 1)
        path.append(current)
    return path


def lattice_paths_search(coor_1, coor_2):
    """search all the possible shortest paths between coor_1 and coor_2

    coor_1: a tuple to represent coordination (x, y)
    coor_2: a tuple to represent coordination (x, y)

    print: all the paths in a list of coordinates
    return: number of paths in total
    """

    # determine the direction:
    ordered_coor_list = [coor_1, coor_2]
    start, end = sorted(ordered_coor_list)[0], sorted(ordered_coor_list)[1]

    # Sice start[0] will always <= end[0], it will always move right
    # but if start[0] == end[0]
    if start[0] == end[0]:
        move_horizontal = None  # 若x值相同,则处于同一条y轴,不必左右移动
    else:
        move_horizontal = 'R'  # 由于start,end是排序所得,所以start一定在end的左侧,只能向右移.

    # determine the movement direction up or down
    if start[1] > end[1]:
        move_vertical = 'D'  # 从start开始必须向下移动才能到end
    elif start[1] < end[1]:
        move_vertical = 'U'  # 从start开始必须向上移动才能到end
    else:
        move_vertical = None  # 若y值相同,则处于同一条x轴,不必上下移动

    # 先处理特殊情况
    if not move_horizontal and not move_vertical:
        print('coor_1 and coor_2 is the same point')  # 两坐标重合
        return 0

    elif not move_horizontal:
        movement = move_vertical * abs(start[1] - end[1])  # 只有竖直移动一条路线
        print(move_translate(start, movement))
        return 1

    elif not move_vertical:
        movement = 'R' * (end[0] - start[0])
        print(move_translate(start, movement))  # 只有水平移动一条路线
        return 1

    # 普通情况
    else:
        # raw = list(permutations('RRDD', 4))
        # filtered_raw = sorted(set(raw), key=a.index)
        pass

print(lattice_paths_search((-1,1), (5,1)))
print(lattice_paths_search((-1,-1), (-1,4)))
