"""
This is a practice to revise all genNode function for Leetcode LinkedList question
The orignal genNode function supports *nodes as a number of parameter or nodes as a List
It is later decided that to remove *nodes option and force to use single List[int] parameter.

Therefore there is a need to add "[" and "]" to all previous finished questions with genNode implemented with *nodes.
This is a good chance to practice regular expression and file reading / modification.
"""

import os
import re

# to match find the genNode in application
raw_with = r"(genNode\()\[([0-9\s\,]*)\]"
raw_without = r"(genNode\()([0-9\,\s]*)(\))"

# Quick test on groups
# test = "genNode([1,2,3, 4, 5])"  # may mix with spapce
# test_output = re.match(to_match, test)
# print(test_output.groups())
# >>> ("genNode(", "[1,2,3, 4, 5]", ")")

"""
# single case test
# remove "[" and "]"
sample1 = "assert Solution().oddEvenList(genNode([2,1,3,5,6,4,7])) == genNode([2,3,6,7,1,5,4]), "Example 2""
m1 = re.findall(raw, sample1)
print(m1)
# >>> [("genNode(", "2,1,3,5,6,4,7"), ("genNode(", "2,3,6,7,1,5,4")]
x = re.sub(raw, r"\g<1>\g<2>", sample1)  # []内^表示"非", \g<n> 表示原pattern的group(n)
print(x) # worked
"""

"""
# add "[" and "]"
sample2 = "assert Solution().oddEvenList(genNode(2,1,3,5,6,4,7)) == genNode(2,3,6,7,1,5,4), "Example 2""
raw2 = r"(genNode\()([0-9\,\s]*)(\))"
m2 = re.findall(raw2, sample2)
print(m2)
x = re.sub(raw2, r"\g<1>[\g<2>]\g<3>", sample2)
print(x) # worked
"""

# Source dir for leetcode folder
sourcedir = "D:/Documents/GitHub/Learning_Python/LeetCode"

def add_brack(filedir):
    without_brack_pattern = re.compile(raw_without)

    with open(filedir, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = without_brack_pattern.sub(r"\g<1>[\g<2>]\g<3>", content)

    with open(filedir, "w", encoding="utf-8") as f:
        f.write(new_content)


def del_brack(filedir):
    with_brack_pattern = re.compile(raw_with)

    with open(filedir, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = with_brack_pattern.sub(r"\g<1>\g<2>", content)

    with open(filedir, "w", encoding="utf-8") as f:
        f.write(new_content)


def general_modify(directory, fn):
    """Single directory, non-recursive"""
    for sub_dir in os.listdir(directory):
        true_sub_dir = os.path.join(directory, sub_dir)  # 不要用拼接字符串来组子路径
        if true_sub_dir.endswith(".py"):
            fn(true_sub_dir)


if __name__ == "__main__":
    general_modify(sourcedir, add_brack)

