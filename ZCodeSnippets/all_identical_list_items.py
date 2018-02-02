# 检查一个list中是否所有元素都相同
# check if all items are identical in a list

# All following function does the same thing, check if the set contains all identical elements
def all_identical_1(iterable):
    return iterable.count(matrix[0]) == len(iterable)

def all_identical_2(iterable):
    return all(i==iterable[0] for i in iterable)

def all_identical_3(iterable):
    return len(set(iterable)) <= 1   

def all_identical_4(iterable):  # 错位对比法
   return iterable[1:] == iterable[:-1]  # can not be used for unslicable matrix (tuple)

if __name__ == '__main__':
    print(all_identical_3((1,1,1,1)))  # >>> True
    print(all_identical_4([1,2,3,4,5]))  # >>> False
    

# 利用以上方法
# 假设一个matrix中含有很多list,写一个函数: 检查是否其中一个list中存在所有元素相等的情况

# """matrix is a list containing sub-lists"""
def verify1(matrix):
    return any(xlist.count(xlist[0]) == len(xlist) for xlist in matrix)

def verify2(matrix):
    return any(all(i==xlist[0] for i in xlist) for xlist in matrix)

def verify3(matrix):
    return any(len(set(i)) <=1 for i in matrix)

def verify4(matrix):  # 错位对比法
   return any(i[1:] == i[:-1] for i in matrix)

if __name__ == '__main__':
    target = [[1, 2, 1, 1], [1, 1, 1, 1], [1, 3, 1, 6], [1, 7, 2, 5]]
    print(verify1(target))
    print(verify2(target))
    print(verify3(target))
    print(verify4(target))

# 注意使用all()和any(),配合list comprehension
