"""
This is to fix the current leetcode test case in a new form

Current:
testMethod = Solution_STD().plusOne
assert testMethod([0]) == [1], "Edge 0"

New:
testCase = Solution_STD()
assert testCase.plusOne([0]) == [1], "Edge 0"

This requires:
1. replace testMethod to testCase
2. Identify the function and remove from the testCase definition line
3. Add function number to all actual cases
"""

import re
import os

directory = "D:/Documents/GitHub/Learning_Python/LeetCode"

def LCTM2LCTC(directory):
    # read file
    print("Checking:", directory)
    with open(directory, "r", encoding="utf-8") as f:
        content = f.read()

    # Search for the test case definition pattern
    raw_functionline_founder = re.compile(r"(testMethod)( = Solution_\w+\(\))(\.\w+)")
    raw_case_pattern = re.compile(r"testMethod")


    # First store the functionName for future use
    functionLine = raw_functionline_founder.search(content)

    if functionLine:
        fucntionName = functionLine.group(3)

        # Replace the functionLine by removing the funcName
        new_content_case_instance_built = raw_functionline_founder.sub(r"testCase\g<2>", content)

        # Replace the functionLine
        new_content_case_built = raw_case_pattern.sub("testCase" + fucntionName, new_content_case_instance_built)

        # Write content back
        with open(directory, "w", encoding="utf-8") as f:
            f.write(new_content_case_built)



def general_modify(directory, fn):
    """Single directory, non-recursive"""
    for sub_dir in os.listdir(directory):
        true_sub_dir = os.path.join(directory, sub_dir)  # 不要用拼接字符串来组子路径
        if true_sub_dir.endswith(".py"):
            fn(true_sub_dir)

if __name__ == '__main__':
    general_modify(directory, LCTM2LCTC)
