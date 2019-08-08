# 测试list中为数字，会不会sort？
list1 = [1, 9, 5, 7, 3]
list2 = ["1", "9", "5", "7", "3"]
# list3 = [1, "9", 5, "7", "3"]         --------sort 不能让str和int混合排序
# list4 = ["apple", "abple", "banana", 1, 4, 3] ----同上
list5 = ["apple", "3", "abple", "4", "banana", "1"]

list1.sort()
list2.remove("9")
list2.sort()


list5.sort()

print(list1)
print(list2)


print(list5)

# 1,3,5,7,9不论是int还是str都会排序成功
# 数字字符和文字字符排序按照数字优先小到大，然后文字字母顺序

shoplist = ["apple", "mango", "carrot", "banana"]

# 两种删除list内部对象的方式
del shoplist[0]
shoplist.remove("banana")

print(shoplist)
