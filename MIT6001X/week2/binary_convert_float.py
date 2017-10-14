# MIT example

x = float(input('Enter a number between 0 and 1:'))

p = 0
while ((2 ** p) * x) % 1 != 0:  # 很关键,这里设定必须被1整除,才是整数
    print('Remainder = ' + str((2 ** p) * x - int((2 ** p) * x)))
    p += 1

print('p=', p)
num = int(x * (2 ** p))
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num // 2

for i in range(p - len(result)):
    result = '0' + result

result = result[0:-p] + '.' + result[-p:]
print("The binary representation of the decimal " + str(x) + " is " + str(result))

# my own tryout:

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

# # reverse convert
# target = 0.011
# temp_target = 0.1
# ans = 0
# numlevel = len(target)
# for index in range(0, numlevel):
#     ans += int(target[numlevel - index - 1]) * 2**index
# print(ans)
# print(bin(ans))