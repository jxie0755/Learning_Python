"""
A quick task to change all leetcode codes PXXX to LCXXX
"""

import os
import re

folder = "D:\Documents\GitHub\Learning_Python\LeetCode"
pattern = r"(p|P)(\d{3})"


def p_to_LC(filedir: str):
    # to match find the genNode in application
    raw_pattern = r"(p|P)(\d{3})"

    if filedir.endswith(".py"):
        p_phrase = re.compile(raw_pattern)

        with open(filedir, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = p_phrase.sub(r"LC\g<2>", content)

        with open(filedir, "w", encoding="utf-8") as f:
            f.write(new_content)


if __name__ == "__main__":
    # single file test for regex
    first_file = "D:\Documents\GitHub\Learning_Python\LeetCode\LC001_two_sum.py"
    # p_to_LC(first_file)

    from FileIteration.dir_search import general_modify
    general_modify(folder, p_to_LC)
