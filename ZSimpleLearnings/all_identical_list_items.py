# 检查一个list中是否所有元素都相同
# check if all items are identical in a list

xlist = [1, 1, 1, 1]

# solution 1: 检查list中的第一个元素的数量是否等于list的长度
xlist.count(xlist[0]) == len(xlist)

# solution 2: 检查list中的每一个元素是否与第一个元素相等
all(i==xlist[0] for i in xlist)


# 利用以上方法
# 假设一个matrix中含有很多list,写一个函数: 检查是否其中一个list中存在所有元素相等的情况

def verify(matrix):
    return any(xlist.count(xlist[0]) == len(xlist) for xlist in matrix)

def verify2(matrix):
    return any(all(i==xlist[0] for i in xlist) for xlist in matrix)

target = [[1, 2, 1, 1], [1, 1, 1, 1], [1, 3, 1, 6], [1, 7, 2, 5]]
print(verify(target))
print(verify2(target))

# 注意使用all()和any(),配合list comprehension
