x = [1, 2, [3, 'John', 4], 'Hi']

print(x[0])
# 1

print(x[2])
# [3, 'John', 4]

print(x[-1])
# Hi

print(x[2][2])
# 4

print(x[0:1])  # 不再需要逗号,因为中括号识别
# [1]

print(2 in x)
# True

print(3 in x)
# False

x[0] =8
print(x)
# [8, 2, [3, 'John', 4], 'Hi']


print('test1')
