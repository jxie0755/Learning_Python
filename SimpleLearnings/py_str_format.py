"""
学习format()
https://docs.python.org/3/library/string.html#format-string-syntax
python 2.5之后,format通过{}和:来代替%. 

python 3.5新加入f-string,使用更方便,阅读更明确, 主要用于代用之前设定的变量
"""

a = "foo"
b = "bar"
print(f"{a} and {b}")  # >>> foo and bar

# "映射"示例, 通过位置
# 字符串的format函数可以接受不限个参数, 位置可以不按顺序, 可以不用或者用多次, 不过2.6不能为空{}, 2.7才可以
print("{0},{1}".format("foo","bar"))      # >>> foo,bar
print("{},{}".format("foo","bar"))        # >>> foo,bar
print("{1},{0},{1}".format("foo","bar"))  # >>> foo,bar
print("{2}, {1}, {0}".format(*"abc"))     # >>> c, b, a  # unpack

# 通过关键字参数
print("{name}, {age}".format(age=18,name="denis"))  # >>> denis, 18

# 通过对象属性

class Person:
    def __init__(self,name,age):
        self.name,self.age = name,age
    def __str__(self):
        # return "This guy is {self.name}, is {self.age} old".format(self=self)
        return f"This guy is {self.name}, is {self.age} old"  # f-string

print(Person("denis",18))  # >>> This guy is denis, is 18 old

# 通过下标
p = ["foo", "bar"]
print("{0[0]},{0[1]}".format(p))  # >>> foo,bar
print(f"{p[0]}, {p[1]}")  # >>> foo,bar  # f-string

# format 格式限定符
# 它有着丰富的的"格式限定符"(语法是{}中带:号), 比如: 

# 填充与对齐, 填充常跟对齐一起使用
# ^, <, >分别是居中, 左对齐, 右对齐, 后面带宽度
# :号后面带填充的字符, 只能是一个字符, 不指定的话默认是用空格填充
print("{:>8}".format("189"))   # >>> "     189"
print("{:0>8}".format("189"))  # >>> "00000189"
print("{:a^8}".format("189"))  # >>> "aa189aaa"  # 优先补右边
print(f"{'189':x^9}")          # >>> xxx189xxx   # f-string

# 精度与类型f, 精度常跟类型f一起使用
# The default precision is 6
print("{:f}".format(321.12345))    # >>> 321.123450
print("{:.2f}".format(321.12345))  # >>> "321.12" # 其中.2表示长度为2的精度, f表示float类型
print(f"{321.12345:.2f}")          # >>> 321.12   # f-string

# 不带类型f,就是slice切片
print("{:.5}".format(321.12945))    # >>> 321.13  # 虽然是宽度,但是配合.还是会控制精度
print(f"{321.12345:.5}")            # >>> 321.12  f-string
print("{:.5}".format("321.12345"))  # >>> 321.1  # 输出 [:5]

# 其他类型
# 主要就是进制了, b d o x分别是二进制, 十进制, 八进制, 十六进制. 
print("{:b}".format(5))  # >>> "101"
print(f"{5:b}")          # >>> "101"  # f-string

print("{:d}".format(17))  # >>> "17"
print("{:o}".format(9))  # >>>  "11"
print("{:x}".format(15))  # >>> "f"
lst = [17, 9, 15]
print("{:02d}{:02o}{:02x}".format(*lst))  # >>> "17110f"

# 用 , 号还能用来做金额的千位分隔符. 
print("{:,}".format(1234567890))  # >>> "1,234,567,890"
print(f"${1234567890:,}")         # >>> $1,234,567,890  # f-string # must be num(int or float)
print(f"${1234567890.99:,}")      # >>> $1,234,567,890.99

# 表示正负
print("{:+f}; {:+f}".format(3.14, -3.14))  # show it always
# >>> "+3.140000; -3.140000"
print("{: f}; {: f}".format(3.14, -3.14))  # show a space for positive numbers
# >>> " 3.140000; -3.140000"
print("{:-f}; {:-f}".format(3.14, -3.14))  # show only the minus -- same as "{:f}; {:f}"
# >>>> "3.140000; -3.140000"
print("{:-.2f}; {:-.2f}".format(3.14, -3.14))  # and control precision
# >>> 3.14; -3.14

# 百分比
print("{:.2%}".format(19/22))  # >>> 86.36%'

# Special type
import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print("{:%Y-%m-%d %H:%M:%S}".format(d))  # >>> "2010-07-04 12:15:58"
