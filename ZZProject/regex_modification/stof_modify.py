# This is a practice to revise all genNode function for Leetcode LinkedList question
# The orignal genNode function supports *nodes as a number of parameter or nodes as a List
# It is later decided that to remove *nodes option and force to use single List[int] parameter.

# Therefore there is a need to add '[' and ']' to all previous finished questions with genNode implemented with *nodes.
# This is a good chance to practice regular expression and file reading / modification.

import re
import os

raw = r'[^(STOF:\s)]https://stackoverflow.co[mM]'
raw = r'^(?!STOF:\s)+?https'

without_stof = re.compile(raw)

# 注意这里不能使用零宽容度, 因为不一定是一行开头使用
# https://stackoverflow.com/a/4639787/8435726

# quick test
print(without_stof.findall('STOF: https://stackoverflow.coM, https://stackoverflow.coM'))


# Source dir for leetcode folder
sourcedir = 'D:/Documents/GitHub/Learning_Python/LeetCode'


def add_stof(content, filedir):
    new_content = without_brack_pattern.sub(r'\g<1>[\g<2>]\g<3>', content)
    with open(filedir, 'w', encoding="utf-8") as f:
        f.write(new_content)


# while True:
#     command = input("Please choose a command to [add] or [del] the '[]':")
#     if command != 'add' and command != 'del':
#         continue
#     else:
#         break
#
# for sub_dir in os.listdir(sourcedir):
#     full_sub_dir = sourcedir + '/' + sub_dir
#     if full_sub_dir.endswith(".py"):
#         with open(full_sub_dir, 'r', encoding="utf-8") as f:
#             content = f.read()
#
#         ## choose here to add or del []
#         operate_brack(command, content, full_sub_dir)
#
