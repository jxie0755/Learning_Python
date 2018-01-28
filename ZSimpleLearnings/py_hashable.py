# 如果一个对象是可哈希的,那么在它的生存期内必须不可变(需要一个哈希函数),而且可以和其他对象比较(需要比较方法).
# 比较值相同的对象一定有相同的哈希值)
# 简单的说就是生存期内可变的对象不可以哈希,就是说改变时候其id()是不变的.基本就是说列表,字典,集合了.

a = 'a'
b = (1,2,3)
c = [1,2,3]
print(type(a), type(b), type(c))
print(hash(a))
print(hash(b))
# print(hash(c))  >>> lead to error message: TypeError: unhashable type: 'list'

def hashable(x):
    try:
        hash(x)
        print(x, 'is hashable')
        return True

    except TypeError:
        print(x, 'is not hashable')
        return False

print(hashable(c))
