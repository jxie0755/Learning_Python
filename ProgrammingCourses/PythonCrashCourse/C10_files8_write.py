# 仍然是读取文件的代码,但是加一个"w"表示需要写入
# "w"是只写模式,不能读
# 如果文件不存在,就自己新建.
# 如果文件存在,则会清空文件,以待写入.

filename = "D_programming.txt"
with open(filename, "w") as file_object:
    file_object.write("I love programing.")

# 这里程序被运行后,是没有输出的,但是prgramming.txt里面会被写入内容



# a模式和a+模式 是增量编辑模式,若无文件,会自动创建,内容输入在文件末端
# 不得在其他位置写入
filename = "D_alice.txt"

with open(filename, "a") as f_obj:
    f_obj.write("abc")


# r+模式, 覆盖写入,可以定位写入(但仍然是覆盖)
# 原文件内容为123456789
filename = "D_alice2.txt"

with open(filename, "r+") as f_obj:
    f_obj.seek(2) # 定位到2个字符后
    f_obj.write("abc") #在定位的位置输入

with open(filename) as f_obj:
    print(f_obj.read())