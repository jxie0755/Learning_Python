import json # 导入json模块

pnumbers = [2, 3, 5, 7, 11, 13] # 创立一个list

filename = "pnumbers.json"
# 注意不一定必须是.json格式, 模块也可以用于写入读取txt和其他格式

with open(filename, "w") as f_obj:
    json.dump(pnumbers, f_obj)
    # 第一个参数是内容,第二个参数是被写入的文件

# 再次以读取方式打开文件,并把文件数据导入到numbers2
with open(filename) as f_obj:
    numbers2 = json.load(f_obj)

# 由于原内容就是一个list的格式,所以导出来的numbers2也是一个list
print(numbers2)