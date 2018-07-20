a = [1,2,3]
b = [1,2]
c = [i for i in a if i not in b].pop()
print(c)