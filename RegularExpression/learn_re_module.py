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


# re.findall(pattern, string, flags=0) -> List[str] or List[Tuple[str]]
# ro.findall(string[, pos[, endpos]]) -> List[str] or List[Tuple[str]]
# ro optional: indicate the idx start and end to search part of the string
# 对 string 返回一个不重复的 pattern 的匹配列表
# If one or more groups are present in the pattern, return a list of groups !!! 重要!分组将会导致显示不全
faresult = re.findall(raw_pattern, sample) # >>> ['1a', '2d']
faresult2 = re.findall(raw_pattern, '1a2b3a4b') # >>> ['1a', '2b', '3a', '4b']
faresult3 = re.findall(raw_pattern, '1111') # >>> [] # can't find
pre_compile.findall('1a2b3a4b', 4) # >>> ['3a', '4b
re.findall(r'(\d{1,2}[-\/])(\d{1,2}[-\/])\d{2,4}', '4/8/03 10-6/2004 2/2/2 01-02-01')
# >>> [('4/', '8/'), ('10-', '6/'), ('01-', '02-')] # 由于年份没有分组, 所以不会被print
re.findall(r'(\d{1,2}[-\/])\d{1,2}[-\/]\d{2,4}', '4/8/03 10-6/2004 2/2/2 01-02-01')
# >>> ['4/', '10-', '01-']  # 由于只有一个组, 所以不会出现tuple


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
# 匹配对象总是有一个布尔值 True。如果没有匹配的话 match() 和 search() 返回 None
# 所以你可以简单的用 if 语句来判断是否匹配


m_obj = re.match(r'(denis)([0-9]+)[\?]+(cindy)([0-9]+?)', 'denis0??cindy1234')
# >>> <_sre.SRE_Match object; span=(0, 12), match='denis0cindy1'>


# mo.expand(template) -> str
# 对 template 进行反斜杠转义替换并且返回，就像 sub() 方法中一样
m_obj.expand(r'\1##\3@@') # >>> denis##cindy@@


# mo.group([group1, ...]) -> string | Tuple[string]
m_obj.group(0) # >>>    denis0??cindy1     # 若为0, 则返回原完整match string, 不论有无group
m_obj.group(1) # >>>    denis
m_obj.group(1, 3) # >>> ('denis', 'cindy')
m_obj.group(0,1,3) # >>> ('denis0??cindy1', 'denis', 'cindy') # 0同理

# 如果正则表达式使用了 (?P<name>…) 语法， groupN 参数就也可能是命名组合的名字
m_obj = re.match(r'(?P<name1>denis)([0-9]+)[\?]+(?P<name2>cindy)([0-9]+?)', 'denis0??cindy1234')
m_obj.group(1)   # >>> denis
m_obj.group('name1') # >>> denis
m_obj.group('name2') # >>> cindy
m_obj.group(2) # >>>  0  # 没有取名的不影响, 仍然按照正常idx排序

# 如果一个组匹配成功多次，就只返回最后一个匹配
m_obj_2 = re.match(r'([0-9][a-z])+', '1a2b3c') # 这个看似只有一个group,但是实际上match了3此
m_obj_2.group(0) # >>> 1a2b3c
m_obj_2.group(1) # >>> 3c  # 虽然分组idx只有1个组, 但是它会返回最后那个match的情况


# Match.__getitem__(g) -> str
# 这个等价于 m.group(g)。这允许更方便的引用一个匹配
# print(m_obj_2[0]) # >>> 1a2b3c  # 像访问list[n]一样访问
# print(m_obj_2[1]) # >>> 3c


# mo.groups(default=None) -> Tuple[str]
m_obj_3 = re.match(r"(\d+)\.(\d+)", "24.163")
m_obj_3.groups() # >>> ('24', '163')

# 如果我们使小数点可选，那么不是所有的组都会参与到匹配当中。这些组合默认会返回一个 None ，除非指定了 default 参数
m_obj_4 = re.match(r"(\d+)\.?(\d+)?", "24")
m_obj_4.groups() # >>> ('24', None)  # 由于?可选,所以没有的?group就成为None
m_obj_4.groups(default='0') # >>> ('24', '0')  # 通过更改使得None变成'0'


# mo.groupdict(default=None) -> Dict[str:str]
# 返回一个字典，包含了所有的 命名 子组。key就是组名。 default 参数用于不参与匹配的组合
m_obj = re.match(r'(?P<name1>denis)([0-9]+)[\?]+(?P<name2>cindy)([0-9]+?)', 'denis0??cindy1234')
m_obj.groupdict() # >>> {'name1': 'denis', 'name2': 'cindy'}
m_obj = re.match(r'(?P<name1>denis)([0-9]+)[\?]+(?P<name2>cindy)?', 'denis0??')
m_obj.groupdict() # >>> {'name1': 'denis', 'name2': None}
m_obj.groupdict(default='blank') # >>> {'name1': 'denis', 'name2': blank}


# mo.start([group])
# mo.end([group])
# 返回 group 匹配到的字串的开始和结束的idx。
# group 默认为0（意思是整个匹配的子串）。
# 如果 group 存在，但未产生匹配，就返回 -1 。
# 对于一个匹配对象 m， 和一个未参与匹配的组 g ，组 g (等价于 m.group(g))产生的匹配是 m.string[m.start(g):m.end(g)]
email = "tony@tiremove_thisger.net"
m = re.search("remove_this", email)
m.start(), m.end() # >>>  7, 18
new_email = email[:m.start()] + email[m.end():] # >>> tony@tiger.net


# mo.span([group])
# 于一个匹配 m ， 返回一个二元组 (m.start(group), m.end(group)) 。
# 注意如果 group 没有在这个匹配中，就返回 (-1, -1) 。
# group 默认为0，就是整个匹配。
sample = 'denis0??'
m_obj = re.match(r'(?P<name1>denis)([0-9]+)[\?]+(?P<name2>cindy)?', sample)
# print(m_obj.span(1)) # >>>  (0,5)
# print(sample[m_obj.span(1)[0]: m_obj.span(1)[1]]) # >>> denis
# print(m_obj.span(3)) # >>>  (-1, -1))
# print(sample[m_obj.span(3)[0]: m_obj.span(3)[1]]) # >>> ''  # Can't find


# mo.pos       pos 的值  若无指定就是0
# mo.endpos   endpos 的值 若无指定就是最后一个idx
# ro.match(string[, pos[, endpos]]) -> match object
raw_pattern = r'(?P<name1>denis)([0-9]+)[\?]+(?P<name2>cindy)?'
pre_compile = re.compile(raw_pattern)
sample = '0123denis0??23'
m_obj = pre_compile.match(sample, 4, 11)
# print(m_obj.pos, m_obj.endpos) # >>>  4, 11
sample = 'denis0??23'
m_obj = re.match(raw_pattern, sample)
# print(m_obj.pos, m_obj.endpos) # >>>  0, 10


# mo.lastindex
# 捕获组的最后一个匹配的整数索引值，或者 None 如果没有匹配产生的话。
raw_pattern = r'(?P<name1>denis)(?P<code>[0-9]+)[\?]+(?P<name2>cindy)?'
sample = 'denis0??,,,'
m_obj = re.match(raw_pattern, sample)
# print(m_obj.lastindex) # >>> 2 最多中匹配到group(2), 因为group3可选而且没找到
# mo.lastgroup
# 最后一个匹配的命名组名字，或者 None 如果没有产生匹配的话
# print(m_obj.lastgroup) # >>> code 同上,最多匹配到group(2),所以返回group(2)的名字


# mo.re      返回产生这个实例的 regex对象
# print(m_obj.re) # >>> re.compile('(?P<name1>denis)(?P<code>[0-9]+)[\\?]+(?P<name2>cindy)?') # 已预编译过
# mo.string  传递到 match() 或 search() 的字符串
# print(m_obj.string) # >>> denis0??,,,  # 原完整sample (包括不匹配的部分)


# 例子, 利用正则抓取时间
t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
#            只能是0X, 或者1X, 或者2X,对x限制,或者单x
#                                             只能是1X, 2X, 3X, 4X, 5X or X
#                                                                                                  same as minutes
m.groups()  # >>> ('19', '05', '30')

# 另一种匹配法
m = re.match(r'^(2[0-3]|[0-1][0-9]|[0-9])\:([0-5][0-9])\:([0-5][0-9])$', t)
m.groups()  # >>> ('19', '05', '30')
