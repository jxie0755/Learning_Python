"""
JSON

如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，
比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，
可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便
"""

# JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：

#    JSON类型	     Python类型
#      {}	           dict
#      []	           list
#    "string"	       "str"
#     1234.56	     int或float
#    true/false	      True/False
#      null           	None
#      //                #     (comment in json will be ignored)


# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
# 我们先看看如何把Python对象变成一个JSON
import json
d = dict(name="Bob", age=20, score=88, graduate=False, record=None)

# dumps
print(json.dumps(d))
# >>> {"name": "Bob", "age": 20, "score": 88, "graduate": false, "record": null}
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object

# loads
json_str = '{"name": "Bob", "age": 20, "score": 88, "graduate": false, "record": null}'
ld = json.loads(json_str)
print(ld)
# >>> {"name": "Bob", "age": 20, "score": 88, "graduate": False, "record": None}

print(type(ld))
# >>> <class "dict">  认得出是字典

# JSON进阶
# Python的dict对象可以直接序列化为JSON的{}
# 不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化
class Student(object):
    def __init__(self, name, age, score, g, c):
        self.name = name
        self.age = age
        self.score = score
        self.graduated = g
        self.criminal_record = c
    def __str__(self):
        return str((self.name, self.age, self.score, self.graduated, self.criminal_record))

s = Student("Adrienne", 2, 95, False, None)
# print(json.dumps(s))   Error
# Object of type "Student" is not JSON serializable

# 除了第一个必须的obj参数外，dumps()方法还提供了一大堆的可选参数
# json.dumps(obj,
#            *,
#            skipkeys=False,
#            ensure_ascii=True,
#            check_circular=True,
#            allow_nan=True,
#            cls=None,
#            indent=None,
#            separators=None,
#            default=None,
#            sort_keys=False,
#            **kw)

# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可
def student2dict(std):
    return {
        "name": std.name,
        "age": std.age,
        "score": std.score,
        "graduate": std.graduated,
        "criminal_record": std.criminal_record
    }

print(json.dumps(s, default=student2dict)) # default调用转换函数
# >>> {"name": "Adrienne", "age": 2, "score": 95, "graduate": false, "criminal_record": null}


# json的dump和load, 是文本格式的, 不要使用binary
with open("./temp/dump.json", "w") as p_obj:
    json.dump(s, p_obj, default=student2dict)

# 偷懒的办法
print("lazy:", json.dumps(s, default=lambda obj: obj.__dict__))
# >>> lazy: {"name": "Adrienne", "age": 2, "score": 95, "graduated": false, "criminal_record": null}
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量


# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象
def dict2student(d):
    return Student(d["name"], d["age"], d["score"], d["graduate"], d["criminal_record"])

# 我们传入的object_hook函数负责转换
with open("./temp/dump.json", "r") as p_obj:
    std_new = json.load(p_obj, object_hook=dict2student)

print(std_new)
# >>> ("Adrienne", 2, 95, False, None)
