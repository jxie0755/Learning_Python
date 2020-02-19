"""
This is to help collect all the grammar and following code example in project Learning SQL
The script will go through all chapters in MD format, and collect all the grammar and write into one file
"""

import os
import re

def sql_syntax_collect(file_dir: str):
    """
    file_dir must be a full file directory
    destination must be a full file directory
    """

    # Check mac or PC
    destination = "D:\Documents\GitHub\Learning_SQL\Syntax_Summary.md"

    chapter_title_pattern = re.compile(r"(##)[\S\s]+?(##)\n")
    syntax_block_pattern = re.compile(r"(语法)(\d+|extra)(:[\S\s]+?```[\S\s]+?```\s)")

    if os.path.isfile(file_dir) and file_dir.endswith(".md"):
        print("working on:", file_dir)
        with open(file_dir, "r", encoding="utf-8") as cpt:
            chapter_content = cpt.read()

            # 先写章节名称
            chapter_title = chapter_title_pattern.search(chapter_content)

            with open(destination, "a", encoding="utf-8") as summary:
                summary.write("---\n")
                summary.write(chapter_title.group(0) + "\n")

            # 再把语法块写入All_grammars.md
            for block in syntax_block_pattern.findall(chapter_content):
                with open(destination, "a", encoding="utf-8") as summary:
                    summary.write("".join(block) + "\n")




if __name__ == '__main__':

    from FileIteration.dir_search import general_modify

    mac_project = r"/Users/Jxie0755/Documents/DXcodings/Learning_SQL/SQL101byMick"
    pc_project = r"D:\Documents\GitHub\Learning_SQL\SQL101byMick"
    mac_destination = r"/Users/Jxie0755/Documents/DXcodings/Learning_SQL/Syntax_Summary.md"
    pc_destination = r"D:\Documents\GitHub\Learning_SQL\Syntax_Summary.md"

    with open(pc_destination, "w", encoding="utf-8") as fobj:
        fobj.write("#Postgre SQL 语法总结#\n\n")
    print("destination generated")

    general_modify(pc_project, sql_syntax_collect)
