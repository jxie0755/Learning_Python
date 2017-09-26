# 事先保存文件pi_digits.txt在PCC文件夹
import os

with open('D_pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents) # 导致末尾多出一个空行


# 若是文件在子文件夹中
with open('sub_folder/D_pi_digits.txt') as file_object2:
    contents2 = file_object2.read()
    print(contents2.rstrip()) # print(contents.rstrip()) # 可以减除此空行

# 若是文件在计算机其他任何位置
with open('/Users/Jxie0755/Documents/DXcodings/Learning_Python/PythonCrashCourse/sub_folder/D_pi_digits.txt') as file_object3:
    # 注意不要使用 鄂化符 tilde ~, 建议用完全完整的路径
    contents3 = file_object3.read()
    print(contents3)

with open(os.path.expanduser('~/Documents/DXcodings/Learning_Python/PythonCrashCourse/D_pi_digits.txt')) as file_object4:
    # 如果非要用颚化符,那么请import os,用os.path.expanduser命令来处理颚化符路径
    contents4 = file_object4.read()
    print(contents4)
