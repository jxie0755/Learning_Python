# https://py.checkio.org/mission/water-jars/

# Each action is described as a string of two symbols: from and to. The jars are marked as 1 and 2, the lake is marked 0. If you want to take water from the lake and fill first jar, then it's "01". To pour water from second jar into the first would be "21". Dump water out of the first jar and back into the lake would be "10". When you fill a jar from the lake, that jars volume will be full. When you pour water out a jar and into the lake, that jars volume will be empty. If you pour water from one jar to another, you can only pour as much as will fill the full volume of the receiving jar.


# The function has three arguments: The volume of first jar, the volume of second jar and the goal. All arguments are positive integers (number > 0). You should return a list with action's sequence.

# The solution must contain the minimum possible number of steps
# Input: The volume of first jar, the volume of second jar and the goal as integers.

def checkio(first, second, goal):
    # Handle the problem of which jar is small and which is large
    small, large = min(first, second), max(first, second)
    if first < second:
        FS,FL,ES,EL,SL,LS = ['01'], ['02'], ['10'], ['20'], ['12'], ['21']
    elif first > second:
        FS,FL,ES,EL,SL,LS = ['02'], ['01'], ['20'], ['10'], ['21'], ['12']

    # if goal can be achieved by one fill
    if goal == small:
        return [FS]
    if goal == large:
        return [FL]


    # if goal can not be achieved by one fill
    return []

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

checkio(5, 7, 6)
# ['02', '21', '10', '21', '02', '21', '10', '21', '02', '21']

# 未完成
