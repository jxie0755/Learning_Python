# Read specific line of a text file
# D_file1.txt contains:
# I am Denis Xie
# You are Cindy Tian
# She is MaoMao

filename = "file1.txt"
lnum = 0  # 创立行的序号
with open(filename) as f_obj:
    for line in f_obj:
        lnum += 1  # 为每行加序号, 从1开始
        if lnum in range(1,3):  # 打印1-2行
            print(line.rstrip())

print()

# 另一种思路
with open(filename) as f_obj:
    lines = f_obj.readlines() # 读取全部line成为一个list
    for line in lines[:2]:  # 打印该list的前2项
        print(line.rstrip())