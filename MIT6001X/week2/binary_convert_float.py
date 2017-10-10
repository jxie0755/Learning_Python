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

x = 0.333
p = 0
int_x = x * 2 ** p
while int_x % 1 != 0:
    p += 1


