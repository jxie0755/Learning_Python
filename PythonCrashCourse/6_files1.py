# 事先保存文件pi_digits.txt在PCC文件夹

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents) # 导致末尾多出一个空行
    # print(contents.rstrip()) # 可以减除此空行

