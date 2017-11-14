import re

text = 'abbaaabbbbaaaaa'
target = 'ab'

print(re.findall(target, text))
# >>> ['ab', 'ab'], findall生成一个list把全部找到的都放入该list

# 使用keywords来直接表达
print(len(re.findall(pattern='abc', string='abcdabceabcfabc')))
# >>> 用len()来计量找到了几个
