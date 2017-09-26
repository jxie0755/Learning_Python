import io

f = io.open('M_M_abc.txt', 'wt', encoding='utf-8')
f.write(u"Imagine non-English language here")
f.close

text = io.open('M_M_abc.txt', encoding='utf8').read()
print(text)
