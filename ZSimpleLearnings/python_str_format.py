# format 格式限定符
# 它有着丰富的的“格式限定符”（语法是{}中带:号），比如：

# 填充与对齐, 填充常跟对齐一起使用
# ^、<、>分别是居中、左对齐、右对齐，后面带宽度
# :号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充
print('{:>8}'.format('189'))   # >>> '     189'
print('{:0>8}'.format('189'))  # >>> '00000189'
print('{:a^8}'.format('189'))  # >>> 'aa189aaa'  # 优先补右边
print(f"{'189':x^9}")          # >>> xxx189xxx   # f-string

# 精度与类型f, 精度常跟类型f一起使用
# The default precision is 6
print('{:f}'.format(321.12345))    # >>> 321.123450
print('{:.2f}'.format(321.12345))  # >>> '321.12' # 其中.2表示长度为2的精度，f表示float类型
print(f'{321.12345:.2f}')          # >>> 321.12   # f-string

# 不带类型f,就是slice切片
print('{:.5}'.format(321.12945))    # >>> 321.13  # 虽然是宽度,但是配合.还是会控制精度
print(f'{321.12345:.5}')            # >>> 321.12  f-string
print('{:.5}'.format('321.12345'))  # >>> 321.1  # 输出 [:5]

# 其他类型
# 主要就是进制了，b d o x分别是二进制、十进制、八进制、十六进制。
print('{:b}'.format(5))  # >>> '101'
print(f'{5:b}')          # >>> '101'  # f-string

print('{:d}'.format(17))  # >>> '17'
print('{:o}'.format(9))  # >>>  '11'
print('{:x}'.format(15))  # >>> 'f'
lst = [17, 9, 15]
print('{:02d}{:02o}{:02x}'.format(*lst))  # >>> '17110f'

# 用 , 号还能用来做金额的千位分隔符。
print('{:,}'.format(1234567890))  # >>> '1,234,567,890'
print(f'{1234567890:,}')          # >>> 1,234,567,890  # f-string

# 表示正负
print('{:+f}; {:+f}'.format(3.14, -3.14))  # show it always
# >>> '+3.140000; -3.140000'
print('{: f}; {: f}'.format(3.14, -3.14))  # show a space for positive numbers
# >>> ' 3.140000; -3.140000'
print('{:-f}; {:-f}'.format(3.14, -3.14))  # show only the minus -- same as '{:f}; {:f}'
# >>>> '3.140000; -3.140000'

# 百分比
print('{:.2%}'.format(19/22))  # >>> 86.36%'

# Special type
import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))  # >>> '2010-07-04 12:15:58'

