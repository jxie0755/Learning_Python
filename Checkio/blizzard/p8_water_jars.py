# https://py.checkio.org/mission/water-jars/

# Each action is described as a string of two symbols: from and to. The jars are marked as 1 and 2, the lake is marked 0. If you want to take water from the lake and fill first jar, then it's "01". To pour water from second jar into the first would be "21". Dump water out of the first jar and back into the lake would be "10". When you fill a jar from the lake, that jars volume will be full. When you pour water out a jar and into the lake, that jars volume will be empty. If you pour water from one jar to another, you can only pour as much as will fill the full volume of the receiving jar.


# The function has three arguments: The volume of first jar, the volume of second jar and the goal. All arguments are positive integers (number > 0). You should return a list with action's sequence.

# The solution must contain the minimum possible number of steps
# Input: The volume of first jar, the volume of second jar and the goal as integers.

# 新思路:
# 一个pair代表两个瓶子的水量,只要target in pair即可终止
# 灌水倒水一共只有六种动作
# 终结条件,重复出现两瓶子的水量

from copy import deepcopy

def checkio(first, second, goal):

    current = [[0, 0]]  # water in [first, second]

    methods = ['01', '02', '12', '21', '10', '20'] # '0' is the lake
    # The string '01' reprenst from lake to first jar, same applies to the other strings '

    temp_method_list = [current]

    def pour(status, first, second):
        """
        return the level of water in first and second
        after pour from first to second
        """
        available = second - status[1]
        if available == 0:
            return status
        elif available > status[0]:
            return [0, status[0]+status[1]]
        else:
            return [status[0]-available, second]

    def process(lst, method):

        now = lst[-1][:]

        if method == '01':
            now[0] = first
        elif method == '02':
            now[1] = second
        elif method == '12':
            now = pour(now, first, second)
        elif method == '21':
            now = pour(now[::-1], second, first)[::-1]
        elif method == '10':
            now[0] = 0
        elif method == '20':
            now[1] = 0

        return now

    def move(lst):
        new_method_list = []
        for i in lst:
            for method in methods:
                new_status = process(i, method)
                if new_status not in i:
                    new_i = deepcopy(i) + [new_status]
                    new_method_list.append(new_i)
        return new_method_list

    tt = move(temp_method_list)
    for i in tt:
        print(i)









# if __name__ == '__main__':
#     #This part is using only for self-checking and not necessary for auto-testing
#     def check_solution(func, initial_data, max_steps):
#         first_volume, second_volume, goal = initial_data
#         actions = {
#             "01": lambda f, s: (first_volume, s),
#             "02": lambda f, s: (f, second_volume),
#             "12": lambda f, s: (
#                 f - (second_volume - s if f > second_volume - s else f),
#                 second_volume if f > second_volume - s else s + f),
#             "21": lambda f, s: (
#                 first_volume if s > first_volume - f else s + f,
#                 s - (first_volume - f if s > first_volume - f else s),
#             ),
#             "10": lambda f, s: (0, s),
#             "20": lambda f, s: (f, 0)
#         }
#         first, second = 0, 0
#         result = func(*initial_data)
#         if len(result) > max_steps:
#             print("You answer contains too many steps. It can be shorter.")
#             return False
#         for act in result:
#             if act not in actions.keys():
#                 print("I don't know this action {0}".format(act))
#                 return False
#             first, second = actions[act](first, second)
#         if goal == first or goal == second:
#             return True
#         print("You did not reach the goal.")
#         return False
#
#     assert check_solution(checkio, (5, 7, 6), 10), "Example"
#     assert check_solution(checkio, (3, 4, 1), 2), "One and two"

checkio(5, 2, 4)
# ['02', '21', '10', '21', '02', '21', '10', '21', '02', '21']

# TODO 未完成
