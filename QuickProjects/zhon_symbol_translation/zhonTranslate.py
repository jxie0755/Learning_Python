"""
This is to create a script to rewrite a file with a lot of 中文标点 and convert to English symbols
The regular Chinese characters should remain unchanged

The file should be in utf-8 in the first place
"""

import re
import os

def strQ2B(ustring: str) -> str:
    """
    中文特殊符号转英文特殊符号
    将ustring中的中文符号替换成英文半角符号
    """

    # 中文特殊符号批量识别
    pattern = re.compile('[，。：“”【】《》？；、（）‘’『』「」﹃﹄〔〕—·]')

    # re.compile: 编译一个正则表达式模式，返回一个模式（匹配模式）对象。
    # [...]用于定义待转换的中文特殊符号字符集

    fps = re.findall(pattern, ustring)

    # re.findall: 搜索string，以列表形式返回全部能匹配的子串。

    # 对有中文特殊符号的文本进行符号替换

    if len(fps) > 0:
        ustring = ustring.replace('，', ', ')
        ustring = ustring.replace('。', '.')
        ustring = ustring.replace('…', '...')
        ustring = ustring.replace('：', ': ')
        ustring = ustring.replace('“', '"')
        ustring = ustring.replace('”', '"')
        ustring = ustring.replace('【', '[')
        ustring = ustring.replace('】', ']')
        ustring = ustring.replace('《', '<')
        ustring = ustring.replace('》', '>')
        ustring = ustring.replace('？', '? ')
        ustring = ustring.replace('；', ': ')
        ustring = ustring.replace('、', ', ')
        ustring = ustring.replace('（', '(')
        ustring = ustring.replace('）', ')')
        ustring = ustring.replace('‘', "'")
        ustring = ustring.replace('’', "'")
        ustring = ustring.replace('’', "'")
        ustring = ustring.replace('『', "[")
        ustring = ustring.replace('』', "]")
        ustring = ustring.replace('「', "[")
        ustring = ustring.replace('」', "]")
        ustring = ustring.replace('﹃', "[")
        ustring = ustring.replace('﹄', "]")
        ustring = ustring.replace('〔', "{")
        ustring = ustring.replace('〕', "}")
        ustring = ustring.replace('—', "-")
        ustring = ustring.replace('·', ".")

    """全角转半角"""
    # 转换说明：
    # 全角字符unicode编码从65281~65374 （十六进制 0xFF01 ~ 0xFF5E）
    # 半角字符unicode编码从33~126 （十六进制 0x21~ 0x7E）
    # 空格比较特殊，全角为 12288（0x3000），半角为 32（0x20）
    # 除空格外，全角/半角按unicode编码排序在顺序上是对应的（半角 + 0x7e= 全角）,所以可以直接通过用+-法来处理非空格数据，对空格单独处理。

    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 12288:  # 全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374):  # 全角字符（除空格）根据关系转化
            inside_code -= 65248
        rstring += chr(inside_code)
    return rstring


def CNwash_single(file_dir: str) -> None:
    """
    将单文件内容中的中文全角标点全部替换成英文标点
    递归操作
    """
    if os.path.isfile(file_dir):
        print("working on:", file_dir)
        with open(file_dir, "r", encoding="utf-8") as fobj:
            content = fobj.read()
        washed_content = strQ2B(content)
        with open(file_dir, "w", encoding="utf-8") as fobj:
            fobj.write(washed_content)


def CNwash_dir(project_dir: str) -> None:
    """
    将路径中的文件内容中的中文全角标点全部替换成英文标点
    非递归操作
    """
    for sub_dir in os.listdir(project_dir):
        full_sub_path = os.path.join(project_dir, sub_dir)
        if os.path.isfile(full_sub_path):
            print("working on:", full_sub_path)
            with open(full_sub_path, "r", encoding="utf-8") as fobj:
                content = fobj.read()
            washed_content = strQ2B(content)
            with open(full_sub_path, "w", encoding="utf-8") as fobj:
                fobj.write(washed_content)


def CNwash_dir_recur(project_dir: str) -> None:
    """
    将路径中的文件内容中的中文全角标点全部替换成英文标点
    递归操作将子路径也做同样的操作
    """
    for sub_dir in os.listdir(project_dir):
        full_sub_path = os.path.join(project_dir, sub_dir)
        if sub_dir == "zhongTranslate.py":
            print("skipped this script")
        elif os.path.isfile(full_sub_path):
            print("working on:", full_sub_path)
            with open(full_sub_path, "r", encoding="utf-8") as fobj:
                content = fobj.read()
            washed_content = strQ2B(content)
            with open(full_sub_path, "w", encoding="utf-8") as fobj:
                fobj.write(washed_content)
        else:
            CNwash_dir_recur(full_sub_path)


if __name__ == "__main__":
    # 测试单条代码
    str = '这是一个，【个人】… ｄｅｂｏｋｅ。。。 正常abcd wtf?'
    str_q2b = strQ2B(str)
    print(str)
    print(str_q2b)

    # 清洗Learning Android中的第一章MD文件
    # CNwash_single("D:/Documents/GitHub/Learning_Android/FirstLineOfCodes/StudyNotes/Chapter_1.MD")

    # 正式进入, 替换整个路径中的markdown文件中的中文标点
    # CNwash_dir("D:/Documents/GitHub/Learning_SQL/SQL101byMick")

    # 清洗整个Learning Python
    CNwash_dir_recur("D:/Documents/GitHub/Learning_Python")
