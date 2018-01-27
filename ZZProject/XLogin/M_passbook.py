# 密码本V1 - 两个文件: 一个储存用户名,一个储存密码
# 将此法引用到 Project - User login
# M_passbook.py

# 更新密码本 函数化

def update_passbook():
    with open('USER.txt', 'a') as f_obj:
        f_obj.write(str(new_user_name) + '\n')
    with open('SN.txt', 'a') as f_obj:
        f_obj.write(str(new_password) + '\n')


# 读取密码本 函数化

def read_passbook():
    """read the passbook from USER and SN file, create a dict"""
    with open('data/USER.txt', 'r') as f_obj:
        listK = f_obj.readlines()
    with open('data/SN.txt', 'r') as f_obj:
        listV = f_obj.readlines()

    # 读取内容剥离转义符号, 写入两个list
    user_list = []
    sn_list = []
    for k in listK:
        user_list.append(k.rstrip())
    for v in listV:
        sn_list.append(v.rstrip())

    # 合并两个list到一个dict中
    # 注意zip函数用法
    pass_book = dict(zip(user_list, sn_list))
    return pass_book