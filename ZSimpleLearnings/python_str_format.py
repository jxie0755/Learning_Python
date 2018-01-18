# 学习format()各种用法
# python 2.5之后,format通过{}和:来代替%。

# “映射”示例, 通过位置
# 字符串的format函数可以接受不限个参数，位置可以不按顺序，可以不用或者用多次，不过2.6不能为空{}，2.7才可以
print('{0},{1}'.format('foo','bar'))      # >>> foo,bar
print('{},{}'.format('foo','bar'))        # >>> foo,bar
print('{1},{0},{1}'.format('foo','bar'))  # >>> foo,bar

# 通过关键字参数

print('{name}, {age}'.format(age=18,name='denis'))  # >>> denis, 18

# 通过对象属性

class Person:  
    def __init__(self,name,age):  
        self.name,self.age = name,age  
    def __str__(self):  
        return 'This guy is {self.name}, is {self.age} old'.format(self=self)  

print(Person('denis',18))  # >>> This guy is denis, is 18 old

# 通过下标
p = ['foo', 'bar']
print('{0[0]},{0[1]}'.format(p))  # >>> foo,bar


# format 格式限定符
# 它有着丰富的的“格式限定符”（语法是{}中带:号），比如：

# 填充与对齐, 填充常跟对齐一起使用
# ^、<、>分别是居中、左对齐、右对齐，后面带宽度
# :号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充
print('{:>8}'.format('189'))   # >>> '     189'
print('{:0>8}'.format('189'))  # >>> '00000189'
print('{:a^8}'.format('189'))  # >>> 'aa189aaa'  # 优先补右边

# 精度与类型f, 精度常跟类型f一起使用
print('{:.2f}'.format(321.33345))  # >>> '321.33' # 其中.2表示长度为2的精度，f表示float类型。

# 其他类型
# 主要就是进制了，b d o x分别是二进制、十进制、八进制、十六进制。
print('{:b}'.format(5))  # >>> '101'
print('{:d}'.format(17))  # >>> '17'
print('{:o}'.format(9))  # >>>  '11'
print('{:x}'.format(15))  # >>> 'f'

# 用 , 号还能用来做金额的千位分隔符。
print('{:,}'.format(1234567890))  # >>> '1,234,567,890'
