aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'

print(aList == bList)
print(aList is bList)

