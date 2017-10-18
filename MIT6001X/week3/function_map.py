# idea generalization
# High Order Programming : HOP, map
# a unary function and a collection of suitable arguments
# simple form

# apply function to a list of argument, each in turn
map(abs, [1, -2, 3, -4])
# return iterable


print(list(map(abs, [1, -2, 3, -4])))


L1 = [1, 28, 36]
L2 = [2, 57, 9]
for elt in map(min, (L1, L2)):  # 注意L1, L2,需要加括号,变成一个iterable的tuple,包含两个list
    print(elt)
