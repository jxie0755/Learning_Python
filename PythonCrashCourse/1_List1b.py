# target: 依次输出list中的最后一个item
# 根据STOF网友推荐,使用while loop

list_A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

while list_A:
    print(list_A.pop())
    if 'c' not in list_A:
        break

print("job done.")

# V2

list_A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

while 'c' in list_A:
    print(list_A.pop())

print('job done')

# V3
list_A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

while list_A: # while list_A has elements, in case 'c' wasn't present
    el = list_A.pop() # save the last element
    print(el)
    if 'c' == el: # if 'c' was popped (reached)
        break
print("job done.")
