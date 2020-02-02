"""
A quick task to change all leetcode problem file from pxxx....py to LCxxx....py
"""

import os
import re

folder = "/Users/Jxie0755/Documents/DXcodings/Learning_Python/LeetCode"
pattern = r"(/Users/Jxie0755/Documents/DXcodings/Learning_Python/LeetCode/)(p)(\w{3}\S+?.py)"

def LC_name_change(file_dir):
    if file_dir.endswith(".py") and "a0_" not in file_dir:
        os.rename(file_dir, re.sub(pattern, r"\1LC\3", file_dir))

if __name__ == '__main__':

    # count = 0
    # for subdir in sorted(os.listdir(folder)):
    #     file_dir = os.path.join(folder, subdir)
    #     if file_dir.endswith(".py") and "a0_" not in file_dir:
    #         # print(file_dir)
    #         count += 1
    #     else:
    #         print(file_dir)
    #
    # print(count)

    # single file test for regex
    first_file = "/Users/Jxie0755/Documents/DXcodings/Learning_Python/LeetCode/p001_two_sum.py"
    assert re.match(pattern, first_file)

    from FileIteration.dir_search import general_modify
    general_modify(folder, LC_name_change)
