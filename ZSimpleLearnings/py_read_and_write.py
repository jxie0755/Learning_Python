# Learn read and write

# 读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。
    # 读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，
    # 所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
    # 然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。

# 读文件
    # 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：
    # >>> f = open('/Users/michael/test.txt', 'r')
        # 标示符'r'表示读，这样，我们就成功地打开了一个文件。


# 如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在：
    # >>> f=open('/Users/michael/notfound.txt', 'r')
        # Traceback (most recent call last):
        #   File "<stdin>", line 1, in <module>
        # FileNotFoundError: [Errno 2] No such file or directory: '/Users/michael/notfound.txt'

    # 如果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示：
        # >>> f.read()
        # 'Hello, world!'

    # 最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：
        # >>> f.close()
        # 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
        # 所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
            # try:
            #     f = open('/path/to/file', 'r')
            #     print(f.read())
            # finally:
            #     if f:
            #         f.close()

        # 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
            # with open('/path/to/file', 'r') as f:
            #     print(f.read())
            # 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。

        # 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
        # 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
        # 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
            # for line in f.readlines():
            #     print(line.strip()) # 把末尾的'\n'删掉

# Open 辅助参数
# 'r'	open for reading (default)
# 'w'	open for writing, (如果文件存在,就会抹去重写, 不存在则创造空文件写入)
# 'x'	open for exclusive creation, failing if the file already exists
# 'a'	open for writing, appending to the end of the file if it exists
# 'b'	binary mode
# 't'	text mode (default)
# '+'	open a disk file for updating (reading and writing)
# Binary file!
# 'rb'  open binary file for rading!!
# 'wb'  open binary file for writing, (如果文件存在,就会抹去重写, 不存在则创造空文件写入)


with open("D:/Documents/GitHub/Learning_Python/PythonCrashCourse/D_programming.txt", "r") as fobj:
    for i in range(20):
        print(fobj.read(3))  # read函数可以选择一次read多少个字符

# 能不能对非文本文件work呢?
# with open("D:/Documents/GitHub/Data_Structure_with_Java/TestDir/testV.mp4") as vobj:
#     a = vobj.read()
# 不行!



# 读取二进制文件
# 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
with open("D:/Documents/GitHub/Data_Structure_with_Java/TestDir/ClownFish.jpg", "rb") as pobj:
    a = pobj.read()

with open("D:/Documents/GitHub/Data_Structure_with_Java/TestDir/ClownFish_pyout.jpg", "wb") as pobj_out:
    pobj_out.write(a)

with open("D:/Documents/GitHub/Data_Structure_with_Java/TestDir/testV.mp4", "rb") as vobj:
    a = vobj.read()

with open("D:/Documents/GitHub/Data_Structure_with_Java/TestDir/testV_pyout.mp4", "wb") as vobj_out:
    vobj_out.write(a)