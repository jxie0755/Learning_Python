"""
PE015 Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

######
 #  #
######
 #  #
######

How many such routes are there through a 20×20 grid?
"""


# Brutal force
def count_grid_path(n):
    """return number of paths from top left to bottom right

    only allow to move right and down
    n: size of the grid
    """

    count = 0
    current = [(0,0)]  # 从原点出发

    while len(current) != 0:

        # 分裂坐标
        temp = []
        for coor in current:
            temp += [(coor[0] + 1, coor[1]), (coor[0], coor[1] + 1)]  # 得到分叉一层后的坐标

        # 这里检查坐标
        open_path, end_path = [], []
        for coor in temp:
            if coor[0] == n or coor[1] == n:  # 如果遇到x值或者y值等于n,相当于不再可能分叉
                end_path.append(coor)  # 不能分叉的坐标,为路线的终点
            else:
                open_path.append(coor) # 可以继续分叉的坐标

        current = open_path[:]  # 可以继续分叉的坐标,进入下轮循环
        count += len(end_path) # 不能分叉的坐标的数目记入结果

        # 最终current中所有的坐标都会遇到x值=n或者y值=n,所以open_path最终为空list
        # 导致current也就为空,终结while循环

    return count


if __name__ == "__main__":
    assert count_grid_path(1) == 2, "simple"
    assert count_grid_path(2) == 6, "regular"
    print(count_grid_path(10))
    # >>> 184756

    # print(count_grid_path(20))
    # >>> 计算量太大.算不出来


# 第二版,把上一版中的逻辑抽象化成纯数学
# 这个函数的目的是把一个数列变成相邻数两相加,再在开头和结尾添加上原数列的开头和结尾

def count_grid_path_math(n):
    """return number of paths from top left to bottom right

    Only allow to move right and down
    n: size of the grid (sqaure as n*n)
    """

    def list_add(lst):
        """
        test case:
        print(list_add([1,1]))    # >>> [1, 2, 1]
        print(list_add([1,2,1]))  # >>> [1, 3, 3, 1]
        """
        index = 0
        result = []
        while index < len(lst) - 1:
            result.append(lst[index] + lst[index + 1])
            index += 1
        return [lst[0]] + result + [lst[-1]]

    num_list = [1,1]
    for i in range(n*2 - 1):
        num_list = list_add(num_list)

    return num_list[len(num_list)//2]  # 取中间值

# test final function
if __name__ == "__main__":
    assert count_grid_path_math(1) == 2, "start"
    assert count_grid_path_math(2) == 6, "regular"
    assert count_grid_path_math(10) == 184756, "10*10"
    print(count_grid_path_math(20))
    # >>> 137846528820
    # passed

# 第三版,最佳算法,直接利用排列组合

from math import factorial

def count_grid_path_combination_mehtod(n):
    return factorial(2*n) // factorial(n)**2

# 方法原理: 最短路径一定为2*n长度,其中一定有n个向右,n个向下
# 不同的方法在从2n个空格中,找出n个以填满一种移动方式,则剩下的空格就填满另一种移动方式
# 这个计算方式简化下来就是利用组合数C(2*n, n)得到答案

# 此方法可以用于非正方形grid,因为 width + length = total
# 然后 C(total, width) == C(total, length), 所以只要计算任意个即可


# Additional work
# 与第一版相同算法,但是同时附带打印路径
def count_grid_path_with_path_print(n):
    """return number of paths from top left to bottom right only allow to move right and down

     n: size of the grid
    """
    count = 0
    current = [(0, 0)]  # 从原点出发
    possible_routes = [current]
    good_route = []

    while len(current) != 0:

        # 分裂坐标
        temp = []
        for coor in current:
            temp += [(coor[0] + 1, coor[1]), (coor[0], coor[1] + 1)]  # 得到分叉一层后的坐标

        # 以下代码不影响计算线路数目,只是为了打印路径
        # ---------------------------------------------------------------------------

        # 同时也要分裂possible_routes ([A, B] 变成 [A, A, B, B]
        possible_routes_temp = []
        for i in possible_routes:
            possible_routes_temp += [i[:], i[:]]
        possible_routes = possible_routes_temp[:]

        # 然后分别添加temp中的各项到possible_routes各项(一一对应)
        for idx in range(len(temp)):
            possible_routes[idx].append(temp[idx])

        # 检查各条possible_routes的最末项(也就是刚被加入的项)
        for route in possible_routes:
            if route[-1][0] == n or route[-1][1] == n:
                good_route.append(route)

        # 同时在剔除掉possible_routes中
        possible_routes = list(filter(lambda x: x[-1][0] != n and x[-1][1] != n, possible_routes))

        # ---------------------------------------------------------------------------


        # 这里检查坐标
        open_path, end_path = [], []
        for coor in temp:
            if coor[0] == n or coor[1] == n:  # 如果遇到x值或者y值等于n,相当于不再可能分叉
                end_path.append(coor)  # 不能分叉的坐标,为路线的终点
            else:
                open_path.append(coor)  # 可以继续分叉的坐标

        current = open_path[:]  # 可以继续分叉的坐标,进入下轮循环
        count += len(end_path)  # 不能分叉的坐标的数目记入结果

        # 最终current中所有的坐标都会遇到x值=n或者y值=n,所以open_path最终为空list
        # 导致current也就为空,终结while循环

    # 退出while loop以后,good_routes已经完成
    # 但是,它们并没有抵达(n,n),因为当到达之前的点就被判定为路线成立而终止
    # 逐项检查其中每条路径,帮助其填满所有坐标
    for route in good_route:
        if route[-1][0] == n:
            add_on = [(n, i) for i in range(route[-1][1]+1, n+1)]
            route += add_on
        elif route[-1][1] == n:
            add_on = [(i, n) for i in range(route[-1][0]+1, n+1)]
            route += add_on



    # 最终打印完成的全路径坐标图
    for route in good_route:
        print(route)

    return count
