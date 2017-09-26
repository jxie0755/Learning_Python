# 使用读取的文件内容
# 仍然基于pi_digits.txt做演示

filename = 'D_pi_digits.txt'
with open(filename) as file_object:
    # lines = file_object.readline(12), readline是读取一行内的前12个字符
    lines = file_object.readlines()

# 开始进行使用
pi_string = ''  # 创立空字符串
for line in lines:
    pi_string += line.rstrip() # 将逐行内容合并成一个整字符串,取消所有右侧空换行符
    # pi_string += line.strip() # 若在for loop中替换rstrip为strip,则左侧空格也会被去掉
print(pi_string)
print('length is', len(pi_string), 'digits') # 36个字符说明,之间的空格也被记入

