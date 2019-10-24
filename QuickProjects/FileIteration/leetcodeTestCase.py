"""
This is to fix the current leetcode test case in a new form

"""

import re
import os

directory_py = "D:/Documents/GitHub/Learning_Python/LeetCode"
directory_java = "D:/Documents/GitHub/Learning_Python/LeetCode"


def LC_testCase_fix_py(directory):
    """
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
        print("Changing")
        fucntionName = functionLine.group(3)

        # Replace the functionLine by removing the funcName
        new_content_case_instance_built = raw_functionline_founder.sub(r"testCase\g<2>", content)

        # Replace the functionLine
        new_content_case_built = raw_case_pattern.sub("testCase" + fucntionName, new_content_case_instance_built)

        # Write content back
        with open(directory, "w", encoding="utf-8") as f:
            f.write(new_content_case_built)
    else:
        print("Not Chaning")


def LC_testCase_fix_java(directory):
    """
    Current:
    // No test case, each test build a new instance
    new LC073_Set_Matrix_Zeroes().setZeroes(e1);
    assert Arrays.deepEquals(e1, new int[][]{{}}) : "Edge 1"; // irrelavant

    New:
    LC073_Set_Matrix_Zeroes testCase = new LC073_Set_Matrix_Zeroes();
    testCase.setZeroes(e1);
    assert Arrays.deepEquals(e1, new int[][]{{}}) : "Edge 1"; // irrelavant

    This requires:
    1. Build a testCase as the class instance
    2. Replace each new instance in actual testing with the same testCase
    """
    pass




def general_modify(directory, fn, languange):
    """Single directory, non-recursive"""
    for sub_dir in os.listdir(directory):
        true_sub_dir = os.path.join(directory, sub_dir)  # 不要用拼接字符串来组子路径
        if true_sub_dir.endswith("." + languange):
            fn(true_sub_dir)



if __name__ == '__main__':
    general_modify(directory_py, LC_testCase_fix_py, "py")
    general_modify(directory_java, LC_testCase_fix_java, "java")
