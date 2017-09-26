poem = '''\
Progamming is fun
WHen the work is done
if you wanna make your work also fun:

    use Python!
'''

# 打开文件以编辑('w'ritting)
f = open('M_M_poem.txt', 'w')
# 编辑
f.write(poem)
# 关闭
f.close()

# 如果没有特别指定,将假定启用阅读模式为默认
f = open('M_M_poem.txt')
while True:
    line = f.readline()
    # 零长度指示
    if len(line) == 0:
        break
    # 每行('line')的末尾都又换行符
    # 因为是从一个文件中进行读取
    print(line, end='')  # 设计了一个''空字符串,如果遇到''就终止.
f.close()
