"""
This is to create a general modification to recursively iterate over all the files under
If the file type fits need, it will apply a function to the file, otherwise just skip
"""

import os
import re


def general_modify(directory, fn):
    """Single directory, non-recursive"""
    for sub_dir in os.listdir(directory):
        true_sub_dir = os.path.join(directory, sub_dir)  # 不要用拼接字符串来组子路径
        if os.path.isfile(true_sub_dir):
            fn(true_sub_dir)

def general_modify_recur(directory, fn):
    for sub_dir in os.listdir(directory):
        true_sub_dir = os.path.join(directory, sub_dir)  # 不要用拼接字符串来组子路径
        if os.path.isfile(true_sub_dir):
            fn(true_sub_dir)
        elif os.path.isdir(true_sub_dir):
            general_modify(true_sub_dir, fn)



# test fn (show file name)
def fn_test(file_dir):
    print(file_dir)
# dir = r"D:\Documents\GitHub\Learning_Python\ZZProject\FileIteration\test"
# general_modify_recur(dir, fn_test)



# String modification
def string_change(file_dir):
    """change all string variable in this script from 'str' to "str" in style"""

    if file_dir.endswith(".py"):
        print("file found:", file_dir)
        re_pattern = re.compile(r"\'(.*?)\'")
        re_pattern_exclude = re.compile(r"\'\"(.*?)\"\'")

        with open(file_dir, "r", encoding="utf-8") as f_obj:
            content = f_obj.read()

        # 避免改动'"abc"'这种混合类型的string
        exclude_list = [i.group(0) for i in re_pattern_exclude.finditer(content)]

        if not exclude_list:
            new_content = re_pattern.sub(r'"\1"', content)
            with open(file_dir, "w", encoding="utf-8") as f_obj:
                f_obj.write(new_content)
        else:
            print(file_dir, "is excluded")

# dir = r"D:\Documents\GitHub\Learning_Python"
# general_modify_recur(dir, string_change)

