# remove repeating items in a list
# 去除list中的重复元素

# sorted()函数,使用key,维持原来的顺序,a.index
def remove_repeating(L):
    return sorted(set(L), key=L.index)

if __name__ == '__main__':
  a = ['a','a','b','b','c','c','d']
  print(remove_repeating(a))

  a = ['a','a','b','b','c','c','d']
  print(set(a))  # set(a)根本就不会每次输出统一顺序
  print(list(set(a))) # 因此,list之后也不会每次输出统一顺序

# 注意 sorted(iterable, *, key=None, reverse=False), will return a list!
# 不需要list()命令, sorted(list(set(a)), key=a.index), 因为参数只要iterable即可
# 直接 sorted(set(a), key=a.index)
