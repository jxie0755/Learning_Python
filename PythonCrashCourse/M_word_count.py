# 创造一个函数, 将统计文本字数这个功能做成一个函数,供其他代码引用

def word_count(filename):
    '''count how many words in a file. Input the filename as the argument'''
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = 'Can\'t find the file'
        print(msg)
    else:
        # 计算文件包含多少个单词
        words = contents.split() # 用split命令分解一个长字符串成为一群小字符串
        num_words = len(words)
        print('the file contains ' + str(num_words) + ' words')