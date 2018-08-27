l1 = [1]
l2 = ['a', 'b', 'c']
l3 = [l1+[i] for i in l2]
l4 = [l1+ i for i in l3]
l5 = [l1+ i for i in l4]
print(l3)
print(l4)
print(l4)


X = [3, [6, 7], [6, 8]]
Y = [[X[0]] + i for i in X[1:]]
print('Y', Y)



def all_paths(TL):
    if all(type(i)== list for i in TL):
        return TL




TL0 = [1]
TL1 = [[1, 2], [1, 3]]
TL2 = [[1, [2, 4], [2, 5]], [1, [3, 6], [3, 7]]]
TL3 = [[1, [2, 4], [2, 5]], [1, [3, 6], [3, [7, 8], [7, 9], [7, 10]]]]

print(all_paths(TL0))
print(all_paths(TL1))
print(all_paths(TL2))
print(all_paths(TL3))


