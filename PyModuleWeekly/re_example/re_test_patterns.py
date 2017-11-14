# re_test_patterns

# 利用finditer找出所有的match并且返回它们的位置

import re


def find_patterns(text, pattern):
    # Look for each pattern in the text and print the results

    print(f"\nTo Find: {pattern!r}")
    print(f"In:\n{text!r}\n")

    for match in re.finditer(pattern, text):
        s = match.start()
        e = match.end()
        print('Find at', f'text[{s}:{e}]')
        substr = text[s:e]
        n_backslashes = text[:s].count('\\')
        prefix = '.' * (s + n_backslashes)
        print("{}'{}'".format(prefix, substr))


find_patterns('vvabbaaabbbbaaaaa', 'ab')
