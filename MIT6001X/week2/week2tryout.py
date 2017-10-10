target = 0.333
p = 0
int_target = target * 2 ** p

while int_target % 1 != 0:
    p += 1
    int_target *= 2

int_target = int(int_target)
biList = []
while True:
    biList.append(int_target % 2)
    int_target = int_target // 2
    if int_target == 1:
        biList.append(int_target % 2)  # 要么就在创建list的时候把int变成str
        break
biList.reverse()
print(p)
shift = p - len(biList) # 计算退位数目
while shift != 0:
    biList.insert(0, '0')
    shift -= 1
# 附上前置'0.'
biList.insert(0, '.')
biList.insert(0, '0')
binumber = ''.join(str(i) for i in biList)  # 要注意join必须是string,不能是int
print('The binary number of', target, "is", binumber)
