# target: 依次输出list中的最后一个item

list_A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

for i in list_A:
    print(list_A.pop())
    if 'c' not in list_A:
        break

print("job done.")

# 不知道为何只会输出到j,i,h,g,h.
