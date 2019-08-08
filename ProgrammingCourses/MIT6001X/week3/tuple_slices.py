x = (1, 2, (3, "John", 4), "Hi")

print(x[0])
# 1

print(x[2])
# (3, "John", 4)

print(x[-1])  # 切片单item中[-1]就是最后一项
# Hi

print(x[2][2])
# 4

print(x[2][-1]) # 当tuple中item又是tuple则继续tuple index
# 4

print(x[2][1][1])
# o

print(x[-1][-1]) # 注意double index,如果是单string,则是继续寻找string的index
# i

# print(x[-1][2]) # 不存在
# error

print(x[0:1]) # 注意切片和单item查询不同,切片输出新的tuple(即使只是单item的元祖,注意"(x,)"的表示)
# (1,)

print(x[0:-1]) # 注意!!!!!!切片的[0:-1]不包括最后一项!!!!完整切片请用[:]或[0:]
# (1, 2, (3, "John", 4))

print(len(x)) # 只算顶层item数量
# 4

print(2 in x)
# True

print(3 in x) # 注意3虽然在x[2]中,但是不能被当做一个item返回存在x中为True
# False
