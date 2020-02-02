"""
This is to help collect all the grammar and following code example in project Learning SQL
The script will go through all chapters in MD format, and collect all the grammar and write into one file
"""

import os
import re

def sql_grammar_collect(file_dir: str):
    """
    file_dir must be a full file directory
    destination must be a full file directory
    """

    destination = "/Users/Jxie0755/Documents/DXcodings/Learning_SQL/All_grammars.md"

    chapter_title_pattern = re.compile(r"[##]{2}[\S\s]+?[##]{2}\n")
    grammar_block_pattern = re.compile(r"语法\d[\S\s]+?```[\S\s]+?```\s")

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
            for block in grammar_block_pattern.findall(chapter_content):
                with open(destination, "a", encoding="utf-8") as summary:
                    summary.write(block + "\n")




if __name__ == '__main__':
    from FileIteration.dir_search import general_modify
    mac_project = "/Users/Jxie0755/Documents/DXcodings/Learning_SQL/SQL101byMick"
    destination = "/Users/Jxie0755/Documents/DXcodings/Learning_SQL/All_grammars.md"

    with open(destination, "w", encoding="utf-8") as fobj:
        fobj.write("#Postgre SQL 语法总结#\n\n")
    print("destination generated")

    general_modify(mac_project, sql_grammar_collect)
