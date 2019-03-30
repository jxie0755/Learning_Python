# This is a script to ensure all of the script file in a coding project:
# has one and only one empty new line at the end.

import os
import re


def process_win_dir(dir):
    """revise the windows dir from using '\' to '/'
    dir: a string of window directory, must be in raw stirng type with "r" as prefix
    """
    result = ''
    for i in dir:
        if i == '\\':
            result += '/'
        else:
            result += i
    return result


def count_empty(content):
    splt = content.split("\n")
    count = 0
    for i in splt[::-1]:
        if i == '':
            count += 1
        else:
            return count

count = 0
def add_empty_line(full_dir, target):
    """ensure there is one and only one empty new line at the end of each target file
    dir: a string of directoy, i.e., "./Dir1/Dir2"
    target: a string of file type, i.e., ".py", ".java"
    """
    all_files = os.listdir(full_dir)
    global count

    for sub_file in all_files:

        full_sub_file = os.path.join(full_dir, sub_file)
        if full_sub_file == "D:/Documents/GitHub/Learning_Python/ZZProject/NewEmptyLine/new_empty_line.py":
            pass
        elif os.path.isdir(full_sub_file):
            print("Processing:", full_sub_file)
            add_empty_line(full_sub_file, target)
        elif sub_file.endswith(target):
            print("Processing:", full_sub_file)
            with open(full_sub_file, encoding='utf-8', mode='r') as py_obj:
                content = py_obj.read()

            emp = count_empty(content)
            if emp == 0:
                new_content = content + '\n'
            elif emp == 1:
                new_content = content
            elif not emp:   # 如果是空白文件
                pass
            else:
                new_content = content[:1 - emp]

            if emp:
                with open(full_sub_file, encoding='utf-8', mode='w') as py_obj:
                    py_obj.write(new_content)
                    count += 1


if __name__ == '__main__':
    directory = input("Please input full directory:")
    file_type = input("Plase input file type: ")

    while True:
        proceed = input("Start? Y/N")
        if proceed == "Y":
            add_empty_line(directory, file_type)
            break
        elif proceed == "N":
            print("Job Canceled")
            break
        else:
            continue

    print("All done")
    print("Total processed file:", count)
