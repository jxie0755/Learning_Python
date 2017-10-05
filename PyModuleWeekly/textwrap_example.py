import textwrap

sample_text = '''
     The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
      programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''

# 注意or前方没有加indent是因为它输出时刚好是一行的开头,而且不是第一行

sample_indent = textwrap.fill(sample_text, width=50)
print(sample_indent)

print()
dedented_text = textwrap.dedent(sample_text)
print('Dedented:')
print(dedented_text)

