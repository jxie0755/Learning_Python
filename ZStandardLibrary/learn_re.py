# 正则表达式
# 廖雪峰 正则总结 https://www.liaoxuefeng.com/wiki/1016959663602400/1017639890281664

# 字符串是编程时涉及到的最多的一种数据结构，对字符串进行操作的需求几乎无处不在。
# 比如判断一个字符串是否是合法的Email地址，虽然可以编程提取@前后的子串，再分别判断是否是单词和域名，但这样做不但麻烦，而且代码难以复用

# 正则表达式是一种用来匹配字符串的强有力的武器。
# 它的设计思想是用一种描述性的语言来给字符串定义一个规则，凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。
# 所以我们判断一个字符串是否是合法的Email的方法是：
    # 创建一个匹配Email的正则表达式；
    # 用该正则表达式去匹配用户的输入来判断是否合法。


# 因为正则表达式也是用字符串表示的，所以，我们要首先了解如何用字符来描述字符:

# 在正则表达式中，如果直接给出字符，就是精确匹配。用\d可以匹配一个数字，\w可以匹配一个字母或数字，所以：
    # '00\d'    可以匹配'007'，但无法匹配'00A'；
    # '\d\d\d'  可以匹配'010'；
    # '\w\w\d'  可以匹配'py3'；
    # '\s'      可以匹配空格
    # '.'       可以匹配任意字符，所以：
        # 'py.'可以匹配'pyc'、'pyo'、'py!'等等。

# 要匹配变长的字符，在正则表达式中:
    # '*'      表示任意个字符（包括0个）
    # '+'      表示至少一个字符
    # '?'      表示0个或1个字符
    # '{n}'    表示n个字符
    # '{n,m}'  表示n-m个字符

# 来看一个复杂的例子：
# \d{3}\s+\d{3,8}
    # 我们来从左到右解读一下:
        # \d{3}表示匹配3个数字，例如'010'；
        # \s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，'   '等；
        # \d{3,8}表示3-8个数字，例如'1234567'。
# 综合起来，上面的正则表达式可以匹配以任意个空格隔开的带区号的电话号码

# 如果要匹配'010-12345'这样的号码呢？
# 由于'-'是特殊字符，在正则表达式中，要用'\'转义，所以，上面的正则是\d{3}\-\d{3,8} (也就是\-表示特殊字符)
# 但是，仍然无法匹配'010 - 12345'，因为带有空格。所以我们需要更复杂的匹配方式


# 进阶

# 要做更精确地匹配，可以用[]表示范围，比如：
    # [0-9a-zA-Z\_]                   可以匹配一个数字、字母或者下划线；
    # [0-9a-zA-Z\_]+                  可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
    # [a-zA-Z\_][0-9a-zA-Z\_]*        可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
    # [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}  更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）


# 其他手段
    # A|B     可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'
    # ^       表示行的开头，^\d表示必须以数字开头。
    # ^       当在一组方括号里使用^是，它表示“非”或“排除”的意思，常常用来剔除某个字符
    # $       表示行的结束，\d$表示必须以数字结束。
# 你可能注意到了，'py'也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了


# 字符簇含义
# [[:alpha:]] 任何字母
# [[:digit:]] 任何数字
# [[:alnum:]] 任何字母和数字
# [[:space:]] 任何白字符
# [[:upper:]] 任何大写字母
# [[:lower:]] 任何小写字母
# [[:punct:]] 任何标点符号
# [[:xdigit:]] 任何16进制的数字，相当于[0-9a-fA-F]


# re模块
# 有了准备知识，我们就可以在Python中使用正则表达式了。
# Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用\转义，所以要特别注意

s = 'ABC\\-001' # Python的字符串
# 对应的正则表达式字符串变成： 'ABC\-001'
# 因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了
s = r'ABC\-001'
# 对应的正则表达式字符串不变： 'ABC\-001'


# 先看看如何判断正则表达式是否匹配
import re

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
