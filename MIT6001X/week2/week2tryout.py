target = '302'
int_target = int(target)
biList = []
while True:
    biList.insert(0, int_target % 2)
    int_target = int(int_target / 2)
    if int_target == 1:
        biList.insert(0, int_target % 2)
        break

print(biList)
binumber = int(''.join(str(i) for i in biList))
print('The binary number of', int(target), "is", binumber)
