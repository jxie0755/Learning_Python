# Cut out a value from a list and merge the rest
# this is to show all of them


# Version 1
# 利用enumerate()
lst = [1,2,3,4,5]
for i, k in enumerate(lst):
    print(lst[0:i] + lst[i+1:])

# >>> [2, 3, 4, 5]
# >>> [1, 3, 4, 5]
# >>> [1, 2, 4, 5]
# >>> [1, 2, 3, 5]
# >>> [1, 2, 3, 4]

# 相当于:
# print(lst[0:0] + lst[1:])
# print(lst[0:1] + lst[2:])
# print(lst[0:2] + lst[3:])
# print(lst[0:3] + lst[4:])
# print(lst[0:4] + lst[5:])

print()

# Version 2
# 利用pop
lst = [1,2,3,4,5]
for i in range(len(lst)):
    temp = lst[:]  # 注意利用切片复制一个lst,以免变动影响下次迭代
    temp.pop(i)
    print(temp)


print()
# Version 3
# 不需要利用pop, 直接list index也可以
lst = [1,2,3,4,5]
for i in range(len(lst)):
    print(lst[0:i] + lst[i+1:])
