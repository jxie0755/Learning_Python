# target: 依次输出最后一个item

list_B = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
last_item = list_B.pop()

for i in list_B:
    print(last_item)
    if 'c' not in list_B:
        break

print("job done.")

# 这样会不停的输出j,没有达到目的
