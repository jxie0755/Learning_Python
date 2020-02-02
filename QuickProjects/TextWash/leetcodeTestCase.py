"""
This is to fix the current leetcode test case in a new form

"""

import re

pc_directory_py = "D:/Documents/GitHub/Learning_Python/LeetCode"
pc_directory_java = "D:/Documents/GitHub/Data_Structure_with_Java/Leetcode"

def LC_testCase_fix_py(file_dir):
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
    if file_dir.endswith(".py") and "LC" in file_dir:
        print("Checking:", file_dir)
        with open(file_dir, "r", encoding="utf-8") as f:
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
            with open(file_dir, "w", encoding="utf-8") as f:
                f.write(new_content_case_built)
            print("file changed")
        else:
            print("file NOT changed")


def LC_testCase_fix_java(file_dir):
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
    # read file
    if file_dir.endswith(".java") and "LC" in file_dir:
        print("Checking:", file_dir)
        with open(file_dir, "r", encoding="utf-8") as f:
            content = f.read()

        raw_class_identifier = re.compile(r"(class )(\S+)( {)")
        classFinder = raw_class_identifier.search(content)

        if classFinder and not re.search(r"testCase", content):
            className = classFinder.group(2)
            raw_main_identifier = re.compile(r"public static void main\(String\[] args\) {")
            new_content = raw_main_identifier.sub(r"\g<0>\n\t\t" + className + " testCase = new " + className + "();", content)
            caseFinder = re.compile(r"new " + className + r"\(\)\.")
            for case in caseFinder.finditer(content):
                new_content = case.re.sub("testCase.", new_content)

            with open(file_dir, "w", encoding="utf-8") as f:
                f.write(new_content)
            print("file changed")
        else:
            print("file NOT changed")


if __name__ == '__main__':
    # If repeat running, it won't do anything.
    from FileIteration.dir_search import general_modify
    general_modify(pc_directory_py, LC_testCase_fix_py)
    general_modify(pc_directory_java, LC_testCase_fix_java)

