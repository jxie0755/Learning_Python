"""
This is a practice to revise all genNode function for Leetcode LinkedList question
The orignal genNode function supports *nodes as a number of parameter or nodes as a List
It is later decided that to remove *nodes option and force to use single List[int] parameter.

Therefore there is a need to add "[" and "]" to all previous finished questions with genNode implemented with *nodes.
This is a good chance to practice regular expression and file reading / modification.
"""

import re


def add_brack(filedir: str):
    # to match find the genNode in application
    raw_without = r"(genNode\()([0-9\,\s]*)(\))"

    if filedir.endswith(".py"):

        without_brack_pattern = re.compile(raw_without)

        with open(filedir, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = without_brack_pattern.sub(r"\g<1>[\g<2>]\g<3>", content)

        with open(filedir, "w", encoding="utf-8") as f:
            f.write(new_content)


def del_brack(filedir: str):
    # to match find the genNode in application
    raw_with = r"(genNode\()\[([0-9\s\,]*)\]"

    if filedir.endswith(".py"):

        with_brack_pattern = re.compile(raw_with)

        with open(filedir, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = with_brack_pattern.sub(r"\g<1>\g<2>", content)

        with open(filedir, "w", encoding="utf-8") as f:
            f.write(new_content)



if __name__ == "__main__":
    # Source dir for leetcode folder
    # sourcedir = "D:/Documents/GitHub/Learning_Python/LeetCode"
    pass
