# Write list/tuple and write back (as List).
# 函数化

# 写入list/tupple到txt文件
def write_data_txt(filename, raw_data):
    """
    write tuple or list to a txt file

    :param filename: need to be a string, avoid space
    :param raw_data: can be a list or tuple (data can be num or str)
    :return: write into a txt file, each item in one line
    """
    with open(f"{filename}.txt", "w") as f_obj:
        f_obj.write("\n".join(str(i) for i in raw_data))

# 把写入的list/tuple写回
def write_into_data(filename):
    """
    return the content back to python written by the function: write_data_txt(filename, raw_data)

    :param filename: the #.txt file's name
    :return: the content (in the form of a tuple or list) back to the output (num will be converted to str)
    """
    with open(f"{filename}.txt", "r") as f_obj:
        raw_list = f_obj.readlines()
    new_list = []
    for i in raw_list[:-1]:  #使用[-1]因为最后一个item后面不需要strip掉换行符
        new_list.append(i.rstrip())
    new_list.append(raw_list[-1]) # 之前的操作是把除了[-1]以外所有的item都加到了new_list,这里再补上最后一个item
    print(new_list)
    # 如果要tuple那就 print(tuple(new_list))

write_data_txt("test_data", (1, 2, 3))
write_into_data("test_data")


# # 写入dict到write_dict.txt中:
# original_dict = {"Denis": 1, "Cindy": 2, "Adrienne": 3}
# with open("M_write_dict.txt", "w") as f_obj:
#     for k, v in original_dict.items():
#         f_obj.write(k + ": " + str(v) + "\n")
#         # 注意, write必须是write字符,所以一切都必须str化
#
# # 把写入的dict写回到文件中.
# with open("M_write_dict.txt", "r") as f_obj:
#     raw_dict = f_obj.readlines()
#
# # 读取每行数据,添加到一个raw_list, 并去除换行符, 同时将keys和values拆分
# raw_list = []
# for i in raw_dict:
#    raw_list.append(i.rstrip().split())
#
# # 将keys和values分辨写入到两个新的list
# listKp = []
# listV = []
# for i in raw_list:
#     listKp.append(i[0])
#     listV.append(i[1])
#
# # 去掉keys中的冒号
# listK = []
# for i in listKp:
#     listK.append(i.replace(":", ""))
#
# # 将keys和values的list打包成为一个dict
# new_dict = dict(zip(listK, listV))
# print(new_dict)


# 函数化.

# Write in
def write_dict_txt(filename, original_dict):
    """
    write a dict to a txt file

    :param filename: must be a string, avoid space
    :param original_dict: a dictionary (both key and value can be num or str)
    :return: writing into the txt file, each pair in one line
    """
    with open(f"{filename}.txt", "w") as f_obj:
        for k, v in original_dict.items():
            f_obj.write(str(k) + ": " + str(v) + "\n")


# Read and write out
def write_into_dict(filename):
    """
    return the content back to python written by the function: write_dict_txt(filename, original_dict)

    :param filename: the #.txt file's name
    :return: the content (in the form dict) back to the output.(output key and value will be converted to str)
    """
    with open(f"{filename}.txt", "r") as f_obj:
        raw_dict = f_obj.readlines()

    raw_list = []
    for i in raw_dict:
        raw_list.append(i.rstrip().split())

    listKp = []
    listV = []
    for i in raw_list:
        listKp.append(i[0])
        listV.append(i[1])

    listK = []
    for i in listKp:
        listK.append(i.replace(":", ""))
    new_dict = dict(zip(listK, listV))
    print(new_dict)

original_dict = {10: 1, 20: 2, 30: 3, 40: 4}
write_dict_txt("test_dict", original_dict)
write_into_dict("test_dict")
