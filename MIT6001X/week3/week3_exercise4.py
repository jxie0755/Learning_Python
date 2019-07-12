# "==" vs "is"

aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = "hello"

print(aList == bList)
print(aList is bList)

cList = [6, 5, 4, 3, 2]
dList = []
for num in cList:
    dList.append(num)
print(cList == dList)
print(cList is dList)
