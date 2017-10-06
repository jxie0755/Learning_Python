import textwrap
from textwrap_example import sample_text

# 注意or前方没有加indent是因为它输出时刚好是一行的开头,而且不是第一行
sample_indent = textwrap.fill(sample_text, width=50)
print(sample_indent)

# 当整体都有indent的时候,dedent可以退掉缩进,但是如果只有一行又缩进,则不行
print()
dedented_text = textwrap.dedent(sample_text)
print('Dedented:')
print(dedented_text)