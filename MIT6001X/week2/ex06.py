
# index和find的区别
# 能找到的时候,是一样的,给出第一个index数字
str1 = 'exterminate!'
str2 = 'number one - the larch'

print(str2.find('z'))  # find找不到的时候会返回int -1
print(str2.find('n'))
# >>>
# -1
# 0

print(str2.index('n')) # index找不到的时候会返回ValueError的错误
print(str2.index('n'))
# >>>
# ValueError
# 0

k = str2.capitalize()
print(k)
