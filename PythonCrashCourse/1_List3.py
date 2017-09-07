# target: 去掉list中的所有'b',并按字母排序

list_C = ['j', 'b', 'f', 'b', 'c', 'i', 'b', 'h', 'b', 'a']
running = True
while running:
    if 'b' in list_C:
        list_C.remove('b')
    if 'b' not in list_C:
        running = False
else:
    print("Removal of b is completed.")

list_C.sort()
print(list_C)
