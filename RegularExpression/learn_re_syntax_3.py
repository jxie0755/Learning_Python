import re

# 正则表达式 必知必会 第二版

# 正则表达式的基本功能
    # 查找特定信息 (搜索)
    # 查找并编辑特定的信息(替换)


# 正则表达式
    # 一些用来匹配和处理文本的字符串
    # 由正则表达式语言创建, 这门语言有特殊的语法和指令
        # 不存在正则表达式程序
        # 不可以直接运行, 无法购买
        # 但是在绝大多数软件产品,编程语言,开发环境中已被实现
    # 解法不唯一
        # 有的简单
        # 有的快速
        # 有的兼容性好

# 用法
    # 大多数时候用于匹配, 但是也可以用来替换操作, 例如 将网址加厚加上HTML语言,变成可点击的链接



# 匹配纯文本
print(re.findall(r"Be", "Ben BBe is my name"))
# >>> ["Be", "Be"]


# 用.替代任何,甚至.本身
print(re.findall(r"c.t", "cat, cot, scut, sc@t, sc t"))
# >>> ["cat", "cot", "cut", "c@t", "c t"]


# 匹配特殊字符使用转义
print(re.findall(r"c.\.t", "cat, caat, ca.t"))
# >>> ["ca.t"]
print(re.findall(r"Array\[0\]", "Array[0]"))
# >>> ["Array[0]"]


# 匹配某个字符
print(re.findall(r"[cs]at", "cat, sat, nat")) # 规定a前面必须只能是c和s
# >>> ["cat", "sat"]


# 匹配区间
print(re.findall(r"[cs]at[0-9]", "cat, sat11, nat")) # t之后必须接一个数字
# >>> ["sat1"]


# 取非, []内用^
print(re.findall(r"[cs]at[^0-9]", "cat, sat11, nat")) # t之后必须接一个数字
# >>> ["cat,"]


# Chapter 5 重复匹配
# 重复匹配次数限定
print(re.findall(r"(\d{1,2}[-\/])(\d{1,2}[-\/])\d{2,4}", "4/8/03 10-6/2004 2/2/2 01-02-01"))
# >>> [("4/", "8/"), ("10-", "6/"), ("01-", "02-")]

# 贪婪匹配
# + 和 * 可能过度匹配

# Example 1:
# 错误方式:
print(re.findall(r"<[B]>.*</[B]>", "<B>XXXX</B> and <B>YYYY</B>"))
# >>>  ["<B>XXXX</B> and <B>YYYY</B>"] # 错误示范, 形成过度匹配
# 正确方式:
print(re.findall(r"<[B]>.*?</[B]>", "<B>XXXX</B> and <B>YYYY</B>"))
# >>> ["<B>XXXX</B>", "<B>YYYY</B>"]

# Example 2:
# 错误方式:
re.match(r"^(\d+)(0*)$", "102300").groups()
# ("102300", "") # 错误示范
# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
# 正确方式:
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
re.match(r"^(\d+?)(0*)$", "102300").groups()
# >>> ("1023", "00")


# Chapter 6 边界
# 判断单词边界,但是不包括边界
# \b 表示边界必须是空白
# 如果想匹配完整单词, 务必前后加\b
print(re.findall(r"[a-z]{2}", "aa bbk kcc kddk"))
# >>> ["aa", "bb", "kc", "kd", "dk"]
print(re.findall(r"\b[a-z]{2}\b", "aa bbk kcc kddk"))
# >>> ["aa"]
print(re.findall(r"[a-z]{2}\b", "aa bbk kcc kddk"))
# >>> ["aa", "bk", "cc", "dk"]
print(re.findall(r"\b[a-z]{2}", "aa bbk kcc kddk"))
# >>> ["aa", "bb", "kc", "kd"]

# \B 表示边界不能是空白
print(re.findall(r"\B[a-z]{2}\B", "aa bbk kcc kddk"))
# >>> ["dd"]
print(re.findall(r"[a-z]{2}\B", "aa bbk kcc kddk"))
# >>> ["bb", "kc", "kd"]
print(re.findall(r"\B[a-z]{2}", "aa bbk kcc kddk"))
# >>> ["bk", "cc", "dd"]

print(re.findall(r"\B-\B", "nine-digit, color  a  coded, pass-key"))
print(re.findall(r"\Ba\B", "BaB")) # >>> ["a"]
print(re.findall(r"\B-\B", "B-B")) # >>> None
# 注意, \b匹配的是\W^\w或者\w^\W, 之前的^位置, 而\B则是相反
# 它们并不是单纯的判断前后是否为空白, 而是考虑前后字符属性关系
# 所以连字符-和空白, 不属于\B这种情况, 反而是属于\b, 因为空白和-都不是\w
print(re.findall(r"\Ba\b", "Xa#")) # >>> ["a"]  # 可以, 因为#不属于\w,a是\w



# String边界
# ^匹配开头,$匹配结尾
print(re.findall(r"^\s*<\?xml.*\?>", "  <?xml abcdefg ?> <?xml ABCDEFG ?>"))
# >>> ["  <?xml abcdefg ?> <?xml ABCDEFG ?>"]  # # 错误示范, 贪婪导致
print(re.findall(r"^\s*<\?xml.*?\?>", "  <?xml abcdefg ?> <?xml ABCDEFG ?>"))
# >>> ["  <?xml abcdefg ?>"]  # fix贪婪

# ^.*$ 总能找到匹配? 请找出 一个反例
print(re.findall(r"^.*$", "")) # >>> [""]
print(re.findall(r"^.*$", "\n")) # >>> [""]


# 分行匹配模式
print(re.findall(r"(?m)^abc\w*$", "abcde\nabcDE"))
# >>> ["abcde", "abcDE"]   # 找取每一行符合的
# 有许多正则表达式不支持, 但是python支持



# Chapter 7 子表达式 (也就是分组)

# 寻找ip地址
print(re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", "12.159.0.1, 192.168.1.2"))
# >>> ["12.159.0.1", "192.168.1.2"]
# 可以被替换成?
print(re.findall(r"(\d{1,3}\.){3}\d{1,3}", "12.159.0.1, 192.168.1.2"))
# >>> ["0.", "1."]  # 注意这里为何不对? 子表达式, 只显示最后一个分组, 而不是全部
# 在这种情况下, 最好的办法就是避免使用findall,而是finditer
# STOF: https://stackoverflow.com/a/31915134/8435726
print([i.group(0) for i in re.finditer(r"(\d{1,3}\.){3}\d{1,3}", "12.159.0.1, 192.168.1.2")])
# >>> ["12.159.0.1", "192.168.1.2"]
# >>>
# 12.159.0.1
# 192.168.1.2

# 寻找年份
print([i.group(0) for i in re.finditer(r"19|20\d{2}", "1986-07-04")])
# >>> ["19"]  # 错误示范, |彻底隔开了整个rString, 其实只应该隔开19和20
print([i.group(0) for i in re.finditer(r"(19|20)\d{2}", "1986-07-04")])
# >>> ["1986"]


# 子表达式的嵌套
# 不应该过度嵌套, 建议适可而止
# ip地址重看:
# r"(\d{1,3}\.){3}\d{1,3}" 其实可以匹配一些非法ip, 因为ip地址数字必须是0-255范围以内
# 正则表达式不懂得数学运算规律, 所以必须用原始的方法来排除
print([i.group(0) for i in re.finditer(r"(((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))\.){3}((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))", "12.159.0.1, 192.256.1.2")])
# 拆解
# (*  (+  (\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5])  +)   \.    *){3}  一个(*){3}限定为3次出现, 内部为一个(+)和\., (+)内部为4个组的或情况



# Chapter 8 回溯引用, 前后一致配对
# 例子匹配HTML中的标题
print([i.group(0) for i in re.finditer(r"<[hH]1>.*?</[hH]1>", "<H1>Title1</H1> <H2>Title2</H2>, <H3>Title3</H4>")])
# >>> ["<H1>Title1</H1>"]  # 这样只能找到H1
# 简单办法: 使用[1-6]
print([i.group(0) for i in re.finditer(r"<[hH][1-6]>.*?</[hH][1-6]>", "<H1>Title1</H1> <H2>Title2</H2>, <H3>Title3</H4>")])
# >>> ["<H1>Title1</H1>", "<H2>Title2</H2>", "<H3>Title3</H4>"]  # 实现了功能, 但是没有解决错误: 第三项, H3与H4不配对
# 解法: 使用回溯引用
print([i.group(0) for i in re.finditer(r"<[hH]([1-6])>.*?</[hH]\1>", "<H1>Title1</H1> <H2>Title2</H2>, <H3>Title3</H4>")])
# >>> ["<H1>Title1</H1>", "<H2>Title2</H2>"]  # 这样就排除掉了错误的前后title标符

# 例子2, 一段文字, 中间出错了, 里面有些单词背打了两次
print([i.group(0) for i in re.finditer(r"(\w+)[ ]+\1", "denis xie xie cindy tian tian go to school")])
# >>> [" xie xie", " tian tian"]  # 解释: 文字+空格, \1表示前面的(\w)再重复一次
# \1表示group(1), \2表示group(2)以此类推, (\0)表示整个表达式 (python不支持)

# 回溯用途替换
print(re.sub(r"([1-5])234", r"\1??","1234 2234 3234 8234 9234"))
# >>> 1?? 2?? 3?? 8234 9234
print(re.sub(r"([1-5])(234)", r"\2??","1234 2234 3234 8234 9234"))
# >>> 234?? 234?? 234?? 8234 9234
print(re.sub(r"([1-5])(234)", r"\0??","1234 2234 3234 8234 9234"))
# >>>  ??  ??  ?? 8234 9234   # python不支持\0



# Chapter 9 前后查找 (零宽度匹配)

# 向后查找(向上文查找) 使用?<=开头的子表达式 (Positive lookbehind)
print([i.group(0) for i in re.finditer(r"\$[0-9.]+", "Apple: $1.99, Orange: $4.35, Total: 2")])
# >>> ["$1.99", "$4.35"]  # 出现了两个$前缀的价格, 如果不想要$怎么办?
print([i.group(0) for i in re.finditer(r"[0-9.]+", "Apple: $1.99, Orange: $4.35, Total: 2")])
# >>> ["1.99", "4.35", "2"]  直接去掉: 这样会把最后那个不是价格的也提取进来
print([i.group(0) for i in re.finditer(r"(?<=\$)[0-9.]+", "Apple: $1.99, Orange: $4.35, Total: 2")])
# >>> ["1.99", "4.35"] # 通过前文查找完美规避

# 向前查找(向下文查找) 使用?=开头的子表达式 (Positive lookahead)
print([i.group(0) for i in re.finditer(r".+(?=://)", "http://www.google.com \n https://www.apple.com")])
# >>> ["http", " https"]   注意后面的(?=:)匹配的是具体的网址,但是我们不需要它
print([i.group(0) for i in re.finditer(r".+(://)", "http://www.google.com \n https://www.apple.com")])
# >>> ["http://", " https://"]  # 若是不使用, 则://被包括进来



#  提取HTML页面的<TITLE>项, (title可大小写混用)
print(re.findall(r"<[tT][iI][tT][lL][eE]>.*</[tT][iI][tT][lL][eE]>", "<HEAD> <TItlE>????</tItLE>"))
# >>> ["<TItlE>????</tItLE>"]  # 这样不小心把前后<TITLE>标也包括了进来, 但是我不想要这个, 只想要中间的????
# 可用子表达式解决这个问题, 把内容????用子表达式装载, 然后只提取子表达式
# 通过前后查找结合完美解决:
print([i.group(0) for i in re.finditer(r"(?<=<[tT][iI][tT][lL][eE]>).*(?=</[tT][iI][tT][lL][eE]>)", "<HEAD> <TItlE>????</tItLE>")])
# >>> ["????"]

# 前后负查找 与上面类似, 但是刚好相反, 需要匹配的是"前后文没有(?)的内容
# (?<!) Negative Lookbehind  (上文没有)
print([i.group(0) for i in re.finditer(r"(?<!\$)[0-9]+", "Apple: $1, Orange: $2, Total: 3")])
# >>> ["3"]
# (?!)  Negative Lookahead   (下文没有)
print([i.group(0) for i in re.finditer(r"[0-9]+(?! dog|dogs)", "1 dog 2 dogs 3 cats 4 cats")])
# >>> ["3", "4"]

# 零宽度断言(?!exp)
# [^abc]表示不包含a、b、c中任意字符, 我想实现不包含字符串abc应该如何写表达式?
# \b((?!abc)\w)+\b
#
# 注意，我们有一个向前查找的语法(也叫顺序环视)  (?=exp)
# (?=exp) 会查找exp之前的【位置】如果将等号换成感叹号，就变成了否定语义，也就是说查找的位置的后面不能是exp
# 一般情况下?!要与特定的锚点相结合，不然的话, 没法使用简单的零宽度断言
# https://stackoverflow.com/a/4639787/8435726
# 如果排除字符长度不长, 比如排除if在前的情况, 可以用^([^f]|[^i]f)+$, 这里是使用f开头的词,或者没有f前没有i开头的词来实现
# 如果要排除的长度很长, 这个写起来会非常复杂


# Chapter 10 嵌入条件

# 电话号码的格式
# (111)111-1111 和 222-222-2222                 可被接受
# 3333333333 和 (444)-444-4444 和 (555-555-5555) 不可接受

# 如何过滤, 只接受符合格式的电话号码?
option1 = r"\(?\d{3}\)?-?\d{3}-\d{4}"
print(re.match(option1, "(111)111-1111")) # >>> Matched
print(re.match(option1, "222-222-2222")) # >>> Matched
print(re.match(option1, "3333333333")) # >>> None
print(re.match(option1, "(444)-444-4444")) # >>> Matched
print(re.match(option1, "(555-555-5555)")) # >>> Matched

option2 = r"(\()?\d{3}(?(1)\)|-)\d{3}-\d{3}"
print(re.match(option2, "(111)111-1111")) # >>> Matched
print(re.match(option2, "222-222-2222")) # >>> Matched
print(re.match(option2, "3333333333")) # >>> None
print(re.match(option2, "(444)-444-4444")) # >>> None
print(re.match(option2, "(555-555-5555)")) # >>> None
# (\()? 匹配一个可选左括号
# (?(1)\)|-) 是一个回溯引用条件
    # 如果(1)也就是左括号存在, 那就必须有\)右括号匹配 (注意这里不能用\1而是用(1)表示group(1)
    # 如果没有左括号那么必须被-分隔
# 这样就排除掉了(444)-444-4444 和 (555-555-5555)')

# 前后查找条件
# 美国邮编, 两种形式一种是5digits另一种是5digits-4digits
option1 = r"\d{5}(-\d{4})?"
print(re.match(option1, "11111")) # >>> Matched
print(re.match(option1, "22222-")) # >>> Matched
print(re.match(option1, "33333-33")) # >>> Matched
print(re.match(option1, "44444-4444")) # >>> Matched
print(re.match(option1, "555555-5)")) # >>> Matched
# 全都匹配了

option2 = r"\d{5}(-)(?(1)\d{4})|^\d{5}$"
# 若是-存在就必须匹配后4个数字, 不然就是纯5个数字
print(re.match(option2, "11111")) # >>> Matched
print(re.match(option2, "22222-")) # >>> None
print(re.match(option2, "33333-33")) # >>> None
print(re.match(option2, "44444-4444")) # >>> Matched
print(re.match(option2, "555555-5)")) # >>> None


# 匹配数字(带小数点和前置0)
pattern = r"((?=0*)[1-9]+[0-9]+\.{1}|0{1}\.{1})(?(1)(?!\.)\d+)|(?=0*)(?!)([1-9]+[0-9]*(?!\.{2,}))"
print(re.search(pattern, "123"))
print(re.search(pattern, "000123"))
print(re.search(pattern, "000123000456"))
print(re.search(pattern, "0.000123000"))
print(re.search(pattern, "0.000123000456"))
print(re.search(pattern, "00.0099"))
print(re.search(pattern, "100.0099"))
print(re.search(pattern, "12.123"))
print(re.search(pattern, "000123.123"))
print(re.search(pattern, "123..456"))

