# re module
# https://docs.python.org/3/library/re.html
# https://docs.python.org/zh-cn/3/library/re.html
# https://docs.python.org/zh-cn/3/howto/regex.html#regex-howto


# 建议:
# 对于正则表达式样式使用 Python 的原始字符串表示法, 也就是raw string, 形式为 r'string'

# 语法略过, 参考learn_re_syntax和learn_re_sytanx_2

# 模块内容
import re

# pre-knowledge
# 两个对象需要区分!!
    # regex object 正则对象 (ro)
    # match object 匹配对象 (mo)

# pattern : 就是正则表达式,py中用raw string形式(r'str')

# flags
# 一些方法中可以定制flags参数, 默认为0, 其他选择:
    # re.A
    # ASCII
    # 让 \w, \W, \b, \B, \d, \D, \s 和 \S 只匹配ASCII，而不是Unicode

    # re.I
    # IGNORECASE
    # 忽略字母大小写
    # 其他略过, 需要时查看文档




### Module method, 也就是类方法 ###

raw_pattern = r'[0-9][a-z]'
sample = '1abc2def'

# re.compile(pattern, flags=0) -> regex object (预编译)
# 如果需要多次使用这个正则表达式的话，使用 re.compile() 和保存这个regex对象以便复用，可以让程序更加高效
pre_compile = re.compile(raw_pattern)


# re.search(pattern, string, flags=0) -> match object
# ro.search(string[, pos[, endpos]]) -> match object
# ro optional: indicate the idx start and end to search part of the string
# 扫描整个字符串 找到匹配样式的 第一个位置，并返回一个相应的 match对象。
# 如果没有匹配，就返回一个 None
# 注意这和找到一个零长度匹配是不同的
re.search(raw_pattern, sample) # >>> <_sre.SRE_Match object; span=(0, 2), match='1a'>
pre_compile.search(sample, 2)  # >>> <_sre.SRE_Match object; span=(4, 6), match='2'>  # search after sample[2:]


# re.match(pattern, string, flags=0) -> match object
# ro.match(string[, pos[, endpos]]) -> match object
# 如果 string 开始的0或者多个字符匹配到了正则表达式样式，就返回一个相应的 匹配对象
# 如果没有匹配，就返回 None
match_result = re.match(raw_pattern, sample)
match_result2 = re.match(raw_pattern, 'abc2def') # >>> None 尽管包含一个可匹配的'2d',但是它不是从idx=0开始
pre_compile.match('abc2def', 3) # >>> <_sre.SRE_Match object; span=(3, 5), match='2d'> # 从idx=3开始能找到


# re.fullmatch(pattern, string, flags=0) -> match object
# ro.fullmatch(string[, pos[, endpos]]) -> match object
# ro optional: indicate the idx start and end to search part of the string
# 如果整个 string 匹配到正则表达式样式，就返回一个相应的 match对象, 否则就返回一个 None
fullmatch1 = re.fullmatch(raw_pattern, sample) # >>> None # no match
fullmatch2 = re.fullmatch(raw_pattern, '1a')
pre_compile.fullmatch('1a')


# re.split(pattern, string, maxsplit=0, flags=0) -> List[str]
# ro.split(string, maxsplit=0) -> List[str]
s = 'a b,    c'  # 试图获得a, b, c三个字符串
s.split(' ') # >>>  ['a', 'b,', '', '', '', 'c']  # string方法, 无法识别连续空格, 且包括了','
re.split(r'[,]*[\s]+', s) # >>> ['a', 'b', 'c']   # 正则[可选','至少一个或更多空格], 这样就成功筛选
re.split(r'[\s]', 'abc') # >>> ['abc']            # 无法分开就返回整个List[string]
re.compile(r'[,]*[\s]+').split(s, maxsplit=1)
# >>> ['a', 'b,    c']  # 这里maxsplit指的是split的次数, 而不是最后长度


# re.findall(pattern, string, flags=0) -> List[str]
# ro.findall(string[, pos[, endpos]]) -> List[str]
# ro optional: indicate the idx start and end to search part of the string
# 对 string 返回一个不重复的 pattern 的匹配列表
faresult = re.findall(raw_pattern, sample) # >>> ['1a', '2d']
faresult2 = re.findall(raw_pattern, '1a2b3a4b') # >>> ['1a', '2b', '3a', '4b']
faresult3 = re.findall(raw_pattern, '1111') # >>> [] # can't find
pre_compile.findall('1a2b3a4b', 4) # >>> ['3a', '4b


# re.finditer(pattern, string, flags=0) -> Iterator[match object]
# ro.finditer(string[, pos[, endpos]]) -> Iterator[match object]
# ro optional: indicate the idx start and end to search part of the string
# pattern 在 string 里所有的非重复匹配，返回为一个迭代器 iterator 保存了 match对象
f_iter = re.finditer(raw_pattern, sample)
# for i in f_iter:
# <_sre.SRE_Match object; span=(0, 2), match='1a'>
# <_sre.SRE_Match object; span=(4, 6), match='2d'>
# skip pre_compile test


# re.sub(pattern, repl, string, count=0, flags=0) -> new_string with replacement done
# ro.sub(repl, string, count=0) -> new_string with replacement done
# 返回通过使用 repl 替换在 string 最左边非重叠出现的 pattern 而获得的字符串。
# 如果样式没有找到，则不加改变地返回 string。
raw_pattern = r'(genNode\()([0-9]+)(\))'
sample = '000 genNode(123) 111 genNode(456) 222'

# 直接写出替换string
replacement = re.sub(raw_pattern, 'GGWTF?', sample)
# >>> 000 GGWTF? 111 GGWTF? 222  # 直接把pattern完全替换成另一个string

# 使用样式对象: \g<n> 表示pattern中的group(n)
replacement = re.sub(raw_pattern, r'\1ABC\3', sample)
# >>>  000 genNode(ABC) 111 genNode(ABC) 222 # 去掉group(2), 替换成ABC

def foo(matchobj):
    return 'gen??'
replacement = re.sub(raw_pattern, foo, sample)
# >>> 000 gen?? 111 gen?? 222  # 通过函数, 对原pattern改动
# skip all pre_compile tests


# re.subn(pattern, repl, string, count=0, flags=0) -> (new_string, count_of_replacment)
# ro.subn(repl, string, count=0) -> (new_string, count_of_replacment)
# 行为与 sub() 相同，但是返回一个元组 (字符串, 替换次数)
repl_tuple = re.subn(raw_pattern, r'\1ABC\3', sample)
# >>>  ('000 genNode(ABC) 111 genNode(ABC) 222', 2)
# skip pre_compile test


# re.escape(pattern) -> str
# 转义 pattern 中的特殊字符。如果你想对任意可能包含正则表达式元字符的文本字符串进行匹配，它就是有用的
# 这个函数不能用在 sub() 和 subn() 的替换字符串里，只有反斜杠应该被转义
raw = 'python.exe'
re.escape(raw) # >>> python\.exe
raw = '!@#$%^&*()'
re.escape(raw) # >>> \!\@\#\$\%\^\&\*\(\)


# re.purge() 清除正则表达式缓存



### regex object method ###
# 除去以上和re module method重叠共享的方法外, 还有以下方法(属性):

# Pattern.flags
# pre_compile.flags # >>> 32
# re.compile(r'[0-9]+', flags=re.A).flags # >>> 256
# re.compile(r'([0-9]+)(\?\?)([a-z]+)').groups # >>> 3 # 3 groups
# re.compile(r'([0-9]+)(\?\?)([a-z]+)').groupindex # >>> {}

# re.compile(r'([0-9]+)(\n\n)([a-z]+)').pattern # >>>  '([0-9]+)(\n\n)([a-z]+)'
# Don't forget to convert it back to raw string!
# BUT There is no such thing as "raw string" once the string is created in the process
# https://stackoverflow.com/a/21609848/8435726



### match object method ###





























## 先看看如何判断正则表达式是否匹配

# # 分组
# # 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组(Group)
# # ^(\d{3})-(\d{3,8})$
#     # 分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码
#
# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# print(m.group(0)) # >>>  010-12345
# print(m.group(1)) # >>>  010
# print(m.group(2)) # >>>  12345
# # 注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串
#
# m = re.match(r'^([0-9a-zA-Z]+)@([0-9a-zA-Z]+)(.com)$', 'jxie0755@gmail.com')
# print(m.group(1)) # >>>  jxie0755
# print(m.group(2)) # >>>  gmail
# print(m.group(3)) # >>>  .com
# print(m.groups()) # >>> ('jxie0755', 'gmail', '.com')  # 将全部分组放入一个tuple

# t = '19:05:30'
# m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
# #            只能是0X, 或者1X, 或者2X,对x限制,或者单x
# #                                             只能是1X, 2X, 3X, 4X, 5X or X
# #                                                                                                  same as minutes
# print(m.groups())
# # >>> ('19', '05', '30')
#
# # 另一种匹配法
# m = re.match(r'^(2[0-3]|[0-1][0-9]|[0-9])\:([0-5][0-9])\:([0-5][0-9])$', t)
# print(m.groups())
# # >>> ('19', '05', '30')
#
#
#
# # 贪婪匹配
# # 最后需要特别指出的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。举例如下，匹配出数字后面的0
# print(re.match(r'^(\d+)(0*)$', '102300').groups())
# # ('102300', '')
# # 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
#
# # 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
# print(re.match(r'^(\d+?)(0*)$', '102300').groups())
# # >>> ('1023', '00')
#
#
#
# # Test
# def is_valid_email(addr):
#     return re.match(r'^([0-9a-zA-Z]+|[0-9a-zA-Z]+\.[0-9a-zA-Z]+)@([0-9a-zA-Z]+)(.com)$', addr)
#
#
# if __name__ == '__main__':
#     assert is_valid_email('someone@gmail.com'), "E1"
#     assert is_valid_email('bill.gates@microsoft.com'), "E2"
#     assert not is_valid_email('bob#example.com'), "E3"
#     assert not is_valid_email('mr-bob@example.com'), "E4"
#     print('ok')
