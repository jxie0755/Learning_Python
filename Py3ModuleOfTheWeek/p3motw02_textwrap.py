# https://pymotw.com/3/textwrap/index.html

import textwrap

# 这个\很重要!!!!!!!!!!!!
sample_text = ""'\
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    ""'

# 注意or前方没有加indent是因为它输出时刚好是一行的开头,而且不是第一行
sample_indent = textwrap.fill(sample_text, width=50)
print(sample_indent)

# 当整体都有indent的时候,dedent可以退掉缩进,但是如果只有一行又缩进,则不行
print()
dedented_text = textwrap.dedent(sample_text)
print("Dedented:")
print(dedented_text)

# 控制段落宽度
dedented_text = textwrap.dedent(sample_text).strip()
for width in [45, 60]:
    print("{} Columns:\n".format(width))
    print(textwrap.fill(dedented_text, width=width))  # 注意fill()有一个控制width的参数
    print()

# Indenting Blocks
dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
wrapped += "\n\nSecond paragraph after a blank line"
final = textwrap.indent(wrapped, "> ")  # indent这个method允许对目标使用一个字符作为前置,每行都用

print("Quoted block:\n")
print(final)

print()

# 对于一行中含有偶数字符的前方加"EVEN "
def should_indent(line):
    print("Indent {!r}?".format(line))
    return len(line.strip()) % 2 == 0


dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
final = textwrap.indent(wrapped, "EVEN ", predicate=should_indent)

print("\nQuoted block:\n")
print(final)
print()


# 了解更多的fill可选参数
dedented_text = textwrap.dedent(sample_text).strip()
print(textwrap.fill(dedented_text,
                    initial_indent="",
                    subsequent_indent=" " * 4,
                    width=50,
                    ))

# shorten方法: 使用缩略号省略内容
dedented_text = textwrap.dedent(sample_text)
original = textwrap.fill(dedented_text, width=50)

print("Original:\n")
print(original)

shortened = textwrap.shorten(original, 100)  # 注意最终是要算上[...]后不能超过100个字符.
shortened_wrapped = textwrap.fill(shortened, width=50)

print("\nShortened:\n")
print(shortened_wrapped)
