# re module
# https://docs.python.org/3/library/re.html
# https://docs.python.org/zh-cn/3/library/re.html
# https://docs.python.org/zh-cn/3/howto/regex.html#regex-howto


# 建议:
# 对于正则表达式样式使用 Python 的原始字符串表示法, 也就是raw string, 形式为 r'string'

# 语法略过, 参考learn_re_syntax和learn_re_sytanx_2

# 模块内容
import re


# 先看看如何判断正则表达式是否匹配


# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
# >>> <_sre.SRE_Match) object; span=(0, 9), match='010-12345'>
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))
# >>> None


# 切分字符串
s = 'a b    c'
print(s.split(' '))        # >>>  ['a', 'b', '', '', '', 'c']  无法识别连续空格
print(re.split(r'\s+', s)) # >>>  ['a', 'b', 'c']      用'\s+'来表示根据任何数目的空格切分
print(re.split(r'[\s\,]+', 'a,b,,,,  c  d'))   # >>>  ['a', 'b', 'c', 'd']  # 根据任意长度的空格或者逗号区分
print(re.split(r'[\s\,\;]+', 'a,b;; c,;  d'))  # >>>  ['a', 'b', 'c', 'd']   同理


# 分组
# 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组(Group)
# ^(\d{3})-(\d{3,8})$
    # 分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0)) # >>>  010-12345
print(m.group(1)) # >>>  010
print(m.group(2)) # >>>  12345
# 注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串

m = re.match(r'^([0-9a-zA-Z]+)@([0-9a-zA-Z]+)(.com)$', 'jxie0755@gmail.com')
print(m.group(1)) # >>>  jxie0755
print(m.group(2)) # >>>  gmail
print(m.group(3)) # >>>  .com
print(m.groups()) # >>> ('jxie0755', 'gmail', '.com')  # 将全部分组放入一个tuple

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
#            只能是0X, 或者1X, 或者2X,对x限制,或者单x
#                                             只能是1X, 2X, 3X, 4X, 5X or X
#                                                                                                  same as minutes
print(m.groups())
# >>> ('19', '05', '30')

# 另一种匹配法
m = re.match(r'^(2[0-3]|[0-1][0-9]|[0-9])\:([0-5][0-9])\:([0-5][0-9])$', t)
print(m.groups())
# >>> ('19', '05', '30')



# 贪婪匹配
# 最后需要特别指出的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。举例如下，匹配出数字后面的0
print(re.match(r'^(\d+)(0*)$', '102300').groups())
# ('102300', '')
# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。

# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
print(re.match(r'^(\d+?)(0*)$', '102300').groups())
# >>> ('1023', '00')



# Test
def is_valid_email(addr):
    return re.match(r'^([0-9a-zA-Z]+|[0-9a-zA-Z]+\.[0-9a-zA-Z]+)@([0-9a-zA-Z]+)(.com)$', addr)


if __name__ == '__main__':
    assert is_valid_email('someone@gmail.com'), "E1"
    assert is_valid_email('bill.gates@microsoft.com'), "E2"
    assert not is_valid_email('bob#example.com'), "E3"
    assert not is_valid_email('mr-bob@example.com'), "E4"
    print('ok')
