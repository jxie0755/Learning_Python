# remove repeating items in a list
# 去除list中的重复元素
a = ['b','c','d','b','c','a','a']
print(set(a))  # set(a)根本就不会每次输出统一顺序
print(list(set(a))) # 因此,list之后也不会每次输出统一顺序

# 解决办法
# sorted()函数,使用key,维持原来的顺序,a.index
a = ['b','c','d','b','c','a','a']
print(sorted(set(a), key=a.index))

