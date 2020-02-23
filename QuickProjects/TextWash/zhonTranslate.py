"""
This is to create a script to rewrite a file with a lot of 中文标点 and convert to English symbols
The regular Chinese characters should remain unchanged

The file should be in utf-8 in the first place
"""

import os
import re


def strQ2B(ustring: str) -> str:
    """
    中文特殊符号转英文特殊符号
    将ustring中的中文符号替换成英文半角符号
    """

    # 中文特殊符号批量识别
    pattern = re.compile('[，。：“”【】《》？；、（）‘’『』「」﹃﹄〔〕—·…]')

    # re.compile: 编译一个正则表达式模式, 返回一个模式（匹配模式）对象.
    # [...]用于定义待转换的中文特殊符号字符集

    fps = re.findall(pattern, ustring)

    # re.findall: 搜索string, 以列表形式返回全部能匹配的子串.

    # 对有中文特殊符号的文本进行符号替换

    if len(fps) > 0:
        ustring = ustring.replace('，', ', ')
        ustring = ustring.replace('。', '. ')
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
        ustring = ustring.replace('…', '...')



    """全角转半角"""
    # 转换说明：
    # 全角字符unicode编码从65281~65374 (十六进制 0xFF01 ~ 0xFF5E)
    # 半角字符unicode编码从33~126 (十六进制 0x21~ 0x7E)
    # 空格比较特殊, 全角为 12288 (0x3000)，半角为 32(0x20)
    # 除空格外, 全角/半角按unicode编码排序在顺序上是对应的(半角 + 0x7e= 全角), 所以可以直接通过用+-法来处理非空格数据, 对空格单独处理。

    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 12288:  # 全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374):  # 全角字符（除空格）根据关系转化
            inside_code -= 65248
        rstring += chr(inside_code)
    return rstring


def CNwash(file_dir: str) -> None:
    """
    将单文件内容中的中文全角标点全部替换成英文标点
    递归操作
    """
    if os.path.isfile(file_dir):
        if "/." in file_dir or "/__" in file_dir or "\." in file_dir or "\__" in file_dir:
            print(file_dir, "skipped")
        elif "zhonTranslate.py" in file_dir:
            print("skipped this script")
        else:
            try:
                with open(file_dir, "r", encoding="utf-8") as fobj:
                    content = fobj.read()
                print("Working on: " + file_dir)
                washed_content = strQ2B(content)
                if content != washed_content:
                    print(file_dir, "changed mad\n")
                    with open(file_dir, "w", encoding="utf-8") as fobj:
                        fobj.write(washed_content)
                else:
                    print("Nothing changed\n")
            except:
                print(file_dir + " cannot be openned by encoding utf-8")
                pass  # ignore non code files (byte files)


if __name__ == "__main__":
    # 测试单条代码
    str = r"这是一个，【个人】… ｄｅｂｏｋｅ。。。 正常abcd wtf?"
    assert strQ2B(str) == r"这是一个, [个人]... deboke. . .  正常abcd wtf?"

    # 清洗Learning Android中的第一章MD文件
    # CNwash("D:/Documents/GitHub/Learning_Android/FirstLineOfCodes/StudyNotes/Chapter_1.MD")

    # 正式进入, 替换整个路径中的markdown文件中的中文标点
    # CNwash_dir(r"D:/Documents/GitHub/Learning_SQL/SQL101byMick")

    # 清洗整个Learning Python
    # general_modify_recur(r"/Users/Jxie0755/Documents/DXcodings/Learning_Python", CNwash)
    # general_modify_recur(r"/Users/Jxie0755/Documents/DXcodings/Learning_Java", CNwash)
    # general_modify_recur(r"/Users/Jxie0755/Documents/DXcodings/Learning_SQL", CNwash)
    # general_modify_recur(r"/Users/Jxie0755/Documents/DXcodings/Learning_Android", CNwash)


    # Single file clean (PC)
    # CNwash(r"D:\Documents\GitHub\Learning_SQL\SQL101byMick\Chapter_0_Setup.md")
    # CNwash(r"D:\Documents\GitHub\Learning_SQL\SQL101byMick\Chapter_1_DataBase_and_SQL.md")
    # CNwash(r"D:\Documents\GitHub\Learning_SQL\SQL101byMick\Chapter_2_Query.md")
    # CNwash(r"D:\Documents\GitHub\Learning_SQL\SQL101byMick\Chapter_3_Query_with_functions.md")
    # CNwash(r"D:\Documents\GitHub\Learning_SQL\SQL101byMick\Chapter_4_Data_Alternation.md")
    # CNwash(r"D:\Documents\GitHub\Learning_SQL\SQL101byMick\Chapter_5_Complex_Query.md")
    # CNwash(r"D:\Documents\GitHub\Learning_SQL\SQL101byMick\Chapter_6_Functions_Predicates_and_Case_Expression.md")

    # Single file clean (mac)
    # CNwash(r"/Users/Jxie0755/Documents/DXcodings/Learning_SQL/SQL101byMick/Chapter_0_Setup.md")
    # CNwash(r"/Users/Jxie0755/Documents/DXcodings/Learning_SQL/SQL101byMick/Chapter_1_DataBase_and_SQL.md")
    # CNwash(r"/Users/Jxie0755/Documents/DXcodings/Learning_SQL/SQL101byMick/Chapter_2_Query.md")
    # CNwash(r"/Users/Jxie0755/Documents/DXcodings/Learning_SQL/SQL101byMick/Chapter_3_Query_with_functions.md")
    # CNwash(r"/Users/Jxie0755/Documents/DXcodings/Learning_SQL/SQL101byMick/Chapter_4_Data_Alternation.md")
    # CNwash(r"/Users/Jxie0755/Documents/DXcodings/Learning_SQL/SQL101byMick/Chapter_5_Complex_Query.md")
    CNwash(r"/Users/Jxie0755/Documents/DXcodings/Learning_SQL/SQL101byMick/Chapter_6_Functions_Predicates_and_Case_Expression.md")

