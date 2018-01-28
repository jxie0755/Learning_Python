# 将字符串变成变量名
# string as variable_name

test = 'aaa'
vars()[test] = 999
print(aaa)

test = '123'
vars()[test] = 'zzz'
print(123)  # 显然string不能是全数字

test = 'bbb'
vars()[test] = 'zzz'
print(bbb)

vars()[test] = 'yyy'
print(bbb)  # 可以被覆盖

# 可以是数据结构
test = 'ccc'
vars()[test] = [1,2,3]
print(ccc)
vars()[test] = (1,2,3)
print(ccc)
vars()[test] = {1,2,3}
print(ccc)
vars()[test] = {'a': 1, 'b': 2}
print(ccc)
