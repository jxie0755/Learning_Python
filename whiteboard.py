import os
import re

folder = "/Users/Jxie0755/Documents/DXcodings/Learning_Python/LeetCode"
pattern = r"[/Users/Jxie0755/Documents/DXcodings/Learning_Python/LeetCode/][p][\w{3}\S+?.py]"

def LC_name_change(file_dir):
    if file_dir.endswith(".py") and "a0_" not in file_dir:
        os.rename(file_dir, re.sub(pattern, r"\1LC\3", file_dir))



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
