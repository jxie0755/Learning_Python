# 将一个txt文件中含有一个ordered list的文件中间插入一个新的item,并调整order
# 原文件:
# 1. Denis
# 2. Cindy
# 3. Adrienne

# 用只读模式打开,并且逐行读取,存入list
filename = 'D_olist.txt'
with open(filename, 'r') as f_obj:
    lines = f_obj.readlines()

# 创见list2, 完整切片list
lines2 = lines[:]

#  插入3. Adrienne, 将3. Didi诺到第四位
lines2.insert(2, '3. Adrienne\n')
# 调整3. Didi为序号4
lines2[3] = '4. Didi'

# 再次用写入模式打开,清空原内容,写入新的list
with open(filename, 'w') as f_obj:
    f_obj.write(''.join(lines2)) # 注意这里因为原list的内容中自带换行符,所以会自动换行
    # 若是没有带换行符,则''改为'\n'

