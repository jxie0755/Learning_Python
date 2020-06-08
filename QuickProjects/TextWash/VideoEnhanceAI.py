import re
import os

folder_dir = "K:\Mac applications\Developer\Common\Python 2.7\IDLE.app\Contents\Library"
pattern = r"([\s\S]+?)(\d.\d\dx)(AA)(.mp4)"
pre_compile = re.compile(pattern)

counter = 0

def TopazVE_AI_rename(file_dir):
    """
    Find out all *.mp4 file that ends with 'xAA.mp4' as the ending and remove the 'AA'
    """
    global counter
    if file_dir.endswith(".mp4") and "xAA" in file_dir:
        if pre_compile.match(file_dir):
            counter += 1
            print(file_dir)
            os.rename(file_dir,pre_compile.sub(r"\1\2\4", file_dir))


if __name__ == '__main__':
    from FileIteration.dir_search import general_modify_recur
    general_modify_recur(folder_dir, TopazVE_AI_rename)
    print(counter)



