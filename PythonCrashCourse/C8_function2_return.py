# Return a value
def format_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()       # 处理完数据,并不展示,而是被用于被其他变量所引用.

musician = format_name('jimi', 'hendrix')
print(musician)


# Optional Argument
def format_name2(first_name2, last_name2, middle_name2=''): # 给middle name一个空白str

    # 利用if条件分别处理
    if middle_name2:
        full_name2 = first_name2 + ' ' + middle_name2 + ' ' + last_name2
    else:
        full_name2 = first_name2 + ' ' + last_name2

    return full_name2.title()

actor = format_name2('tommy', 'jones', 'lee')  # 注意如果用positional arg, middle name要放在末尾.
print(actor)
