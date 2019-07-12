# 序列化

import pickle


# 在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict：
d = dict(name="Bob", age=20, score=88)
# 修改d
d["name"] = "Cindy"

# 可以随时修改变量，比如把name改成"Bill"
# 但是一旦程序结束，变量所占用的内存就被操作系统全部回收。
# 如果没有把修改后的"Bill"存储到磁盘上，下次重新运行程序，变量又被初始化为"Bob"

# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
# 在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling

# Python提供了pickle模块来实现序列化

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
print(pickle.dumps(d))
# >>> b"\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00Bobq\x02X\x03\x00\x00\x00ageq\x03K\x14X\x05\x00\x00\x00scoreq\x04KXu."

# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
with open("./temp/dump.txt", "wb") as p_obj:
    pickle.dump(d, p_obj)
# 看看写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息


# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
with open("./temp/dump.txt", "rb") as p_obj:
    d2 = pickle.load(p_obj)

d2["name"] = "Denis"
print(d2)  # >>> {"name": "Denis", "age": 20, "score": 88}
# 相当于把d修改了以后, 把d存在了硬盘上, 下次读取时就是修改后的内容

# 再次打开同一个文件, 内容不会变化
with open("./temp/dump.txt", "rb") as p_obj:
    d2 = pickle.load(p_obj)
print(d2)  # >>> {"name": "Cindy", "age": 20, "score": 88}

# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系
# 使用什么格式能够兼容呢? JSON
# 参见learn_json
