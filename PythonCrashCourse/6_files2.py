# 使用for loop逐行读取文件
# 3.1415926535
#   8979323846
#   2643383279

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        if '7' in line:
            break
        else:
            print(line)

# 空白行更多了,因为每一行都碰到了末尾换行符,同时python自己也会为读取的内容末尾添加一个换行符,两者个换行符重叠,使得每一行之间都有一个空行
# 同样用rstrip()来处理


