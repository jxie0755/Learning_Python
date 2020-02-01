"""
This is to help collect all the grammar and following code example in project Learning SQL
The script will go through all chapters in MD format, and collect all the grammar and write into one file
"""

import os
import re

project_dir = "D:/Documents/GitHub/Learning_SQL/SQL101byMick"

grammar_block_pattern = re.compile(r"语法\d[\S\s]+?```[\S\s]+?```\s")
chapter_title_pattern = re.compile(r"[##]{2}[\S\s]+?[##]{2}\n")

if not os.path.isdir(project_dir):
    print("Error, directory does not exist")
else:
    pass
    # 先创造文件用于收集语法块
    destination = os.path.join(project_dir, "All_grammars.md")
    with open(destination, "w", encoding="utf-8") as fobj:
        fobj.write("#Postgre SQL 语法总结#\n\n")

    # 遍历project folder找出每章节的markdown文件
    for sub_dir in os.listdir(project_dir):
        if sub_dir.startswith("Chapter") and sub_dir.endswith(".md"):
            f_path = os.path.join(project_dir, sub_dir)
            print("working on:", f_path)

            with open(f_path, "r", encoding="utf-8") as cpt:
                chapter_content = cpt.read()

                # 先写章节名称
                chapter_title = chapter_title_pattern.search(chapter_content)
                print(chapter_title)
                with open(destination, "a", encoding="utf-8") as summary:
                    summary.write("---\n")
                    summary.write(chapter_title.group(0) + "\n")

                # 再把语法块写入All_grammars.md
                for block in grammar_block_pattern.findall(chapter_content):
                    with open(destination, "a", encoding="utf-8") as summary:
                        summary.write(block + "\n")


