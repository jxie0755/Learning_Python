a = [1, 2, 3, 2, 3, 4, 2, 3, 1]
# max() will return max value in an iterable object
print("max value is", max(a))  # >>> 4
# min() will return min value in an iterable object
print("min value is", min(a))  # >>> 1

# also works for strings
b = "abcdegf"
print("max char is", max(b))  # >>> g
print("min char is", min(b))  # >>> a

# or just give a few values as argument for max or min value
print("max value is", max(1, 3, 4, 2)) # >>> 4
print("min value is", min(2, 1, 4, 3)) # >>> 1

# Pay attention to the key argument!
b = "aabbccccccdddeggfff"
print(max(b, key=b.count))  # >>> c
print(min(b, key=b.count))  # >>> e
# This gives the char occrued most often by using .count()
# key一般指定一个function,这个function对于interable argument的每一个item进行处理,
# 然后返回一个function output最大的item.

a = [1, 2, 3, 4, 5]
# 创造一个函数,求除以4的余数, 对于1,2,3,4,5
#                     结果分别是1,2,3,0,1
def func(x):
    return x % 4
print(max(a, key=func))  # 注意只要函数名,不要括号和参数
# >>> 此时返回的是a中除以4,余数最大的那个item, 也就是 3
print(min(a, key=func))  # 注意只要函数名,不要括号和参数
# >>> 同理如果是min,就会返回4,因为余数等于0

# Find the longest list
num = [15, 300, 2700000, 821]
num1 = [12, 2]
num2 = [34, 567, 78, 1, 2, 4]
total = [num, num1, num2]
# using max(iterable, *iterables, key)
print("longest list is:", max(total, key=len))


# Find the key of a dict by max value
a = {"a": 10, "b":40, "c": 20}
print(max(a, key=a.get)) # >>> b

a = {"a": "0000010", "b":"40", "c": "020"}
print(max(a, key=lambda x: len(a.get(x))))  # >>> a


# additional nested dict
a = {
    (1,1): {"prev": ".", "cur": ".", "possible": ["2", "7", "8", "9"]},
    (2,2): {"prev": ".", "cur": ".", "possible": ["1", "3", "8"]},
    (3,3): {"prev": ".", "cur": ".", "possible": ["2", "7", "8", "9", "8"]}
}

b = min(a, key=lambda x: len(a[x]["possible"]))
c = min(a, key=lambda x: len(a.get(x).get("possible")))
print(b) # >>> (2,2)
print(c) # >>> (2,2)