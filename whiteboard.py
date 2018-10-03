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

    print('total route number: ', count)
    return count


count_grid_path_with_path_print(2)