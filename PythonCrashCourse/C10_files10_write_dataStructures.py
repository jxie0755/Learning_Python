# 写入一个list到write_list.txt中:

list = ["1. Denis", "2. Cindy", "3. Adrienne"]
list2 = [1, 2, 3]
with open("D_write_list.txt", "w") as f_obj:
    f_obj.write(", ".join(list)) # ""控制链接方式
    f_obj.write("\n")
    f_obj.write(", ".join(str(i) for i in list2)) # 注意用list comprehension完成str()

# 写入tuple到write_tuple.txt中:

tuple = ("Denis", "Cindy", "Adrienne")
tuple2 = (1, 2, 3)
with open("D_write_tuple.txt", "w") as f_obj:
    f_obj.write("\n".join(tuple))
    f_obj.write("\n")
    f_obj.write("\n".join(str(i) for i in tuple2)) # 注意用list comprehension完成str()

# 写入dict到write_dict.txt中:
dict = {"Denis": 1, "Cindy": 2, "Adrienne": 3}
with open("D_write_dict.txt", "w") as f_obj:
    for k, v in dict.items():
        f_obj.write(k + ": " + str(v) + "\n")
        # 注意, write必须是write字符,所以一切都必须str化