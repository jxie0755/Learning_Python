# create a max() function
def maxx(iterable, *args, **kwargs):
    key = kwargs.get("key", None)
    def m(x):
        if type(x) == int or type(x) == float:
            Max = x
        else:
            x = list(x)
            Max = x[0]
        
        for i in x:
            if i > Max:
                Max = i
        return Max
        
    if key == None:
        if not args:
            return m(iterable)
        if args:
            iterable = [iterable] + [i for i in args]
            return m(iterable)
    else:
        if not args:
            temp = dict(enumerate(list(map(key, iterable))))
            for k, v in temp.items():
                if v == m(list(temp.values())):
                    return iterable[k]
        if args:
            iterable = [iterable] + [i for i in args]
            temp = dict(enumerate(list(map(key, iterable))))
            for k, v in temp.items():
                if v == m(list(temp.values())):
                    return iterable[k]
            
            
a = [1, -6, -2]
print(maxx([1,3,2]))
print(maxx(1, 4, 2))
print(maxx(a, key=abs))
print(maxx(1,-9,2, key=abs))
num = [15, 300, 2700, 821]
num1 = [12, 20000000]
num2 = [34, 567, 78]
dd = [num, num1, num2]
# print('Maximum is:', max(num, num1, num2, key=len))
print('Maximum is:', maxx(dd, key=len))
bb = 'aggbbbbscd'
print(maxx(bb))
print(maxx(bb, key=bb.count))


#其他优秀解法
# 注意利用sorted(),然后求第一个值或者最后一个值

def minnn(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        args = args[0]
    return sorted(args,key=key,reverse=False)[0]

def maxxx(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        args = args[0]
    return sorted(args,key=key,reverse=True)[0]


# 另一个优秀解法
def min(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    items = args[0] if len(args) == 1 else args[:]
    minValue = None
    for i in items:
        # 这里设置的lambda x:x起了作用,如果没有key,那key(i)就是i
        # 如果key=f(),那么key(i)就是f(i)
        # 这样就不论key的有无,都把代码给统一起来了
        if minValue is None or key(i) < key(minValue):
            minValue = i
    return minValue

def max(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    items = args[0] if len(args) == 1 else args[:]
    maxValue = None
    for i in items:
        if maxValue is None or key(i) > key(maxValue):
            maxValue = i
    return maxValue

