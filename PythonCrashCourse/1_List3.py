# target: 去掉list中的所有'b',并按字母排序

list_C = ['j', 'b', 'f', 'b', 'c', 'i', 'b', 'h', 'b', 'a']
while 'b' in list_C:
    list_C.remove('b')
    if 'b' not in list_C:
        break
list_C.sort()
print(list_C)
print("Removal of b is completed.")
