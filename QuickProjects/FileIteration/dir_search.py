"""
High order functions
This is to create a general modification to recursively iterate over all the files under
All the details should be defined in the fn parameter
"""

import os


def single_modify(file_dir: str, fn):
    """
    Single file
    Must be complete directory
    """
    if os.path.isfile(file_dir):
        fn(file_dir)
    else:
        raise FileNotFoundError


def general_modify(folder_dir: str, fn):
    """
    Single directory, non-recursive
    Must be complete directory
    """
    if os.path.isdir(folder_dir):
        for sub_dir in sorted(os.listdir(folder_dir)):
            true_sub_dir = os.path.join(folder_dir, sub_dir)  # 不要用拼接字符串来组子路径
            if os.path.isfile(true_sub_dir):
                fn(true_sub_dir)
    else:
        raise FileNotFoundError

def general_modify_recur(folder_dir: str, fn):
    """
    Single directory, Recursive
    Must be complete directory
    """
    if os.path.isdir(folder_dir):
        for sub_dir in sorted(os.listdir(folder_dir)):
            true_sub_dir = os.path.join(folder_dir, sub_dir)  # 不要用拼接字符串来组子路径
            if os.path.isfile(true_sub_dir):
                fn(true_sub_dir)
            else:
                general_modify_recur(true_sub_dir, fn)
    else:
        raise FileNotFoundError

def fn_test(file_dir):
    print(file_dir)

if __name__ == '__main__':
    # test fn (show file name)
    mac_dir = r"/Users/Jxie0755/Documents/DXcodings/Learning_Python/QuickProjects/FileIteration/test"
    pc_dir = r"D:\Documents\GitHub\Learning_Python\QuickProjects\FileIteration\test"
    # single_modify(mac_dir, fn_test)
    general_modify(mac_dir, fn_test)
    general_modify_recur(mac_dir, fn_test)
