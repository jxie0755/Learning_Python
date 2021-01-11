"""
This is to change the string format from 'string text' to "string text"
"""

import re

re_pattern = re.compile(r"\'(.*?)\'")
re_pattern_exclude = re.compile(r"\'\"(.*?)\"\'")  # TODO improve

def string_change(file_dir):
    """
    change all string variable in this script from 'str' to "str" in style
    file_dir must be a complete file dir
    """
    if file_dir.endswith(".py"):
        print("file found:", file_dir)

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


if __name__ == "__main__":
    from FileIteration.dir_search import general_modify_recur
    folder = "D:\Documents\GitHub\Learning_Python"
    general_modify_recur(folder, string_change)
