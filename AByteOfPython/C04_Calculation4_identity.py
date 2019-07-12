# 此内容是额外的，不包括在A byte of python这本书里，源自http://www.jianshu.com/p/dc5675b4317c
# 用函数id()来获取存储单元的编号
fruits_1 = ["apple", "banana", "grape", "orange", "pear"]
fruits_2 = ["apple", "banana", "grape", "orange", "pear"]
print(id(fruits_1))
print(id(fruits_2))

# 由于fruits_1和fruits_2的内容，使得他们占用了不同的储存单元，所以这两者是不相同的，结果为False
# 只有两者id相同，才可能被身份运算is返回True的结论。
print(fruits_1 is fruits_2)

print()
# 若将fr等同fruits_1则可见到两者储存单元id相同
fr = fruits_1
print(id(fr))
print(fr is fruits_1)
