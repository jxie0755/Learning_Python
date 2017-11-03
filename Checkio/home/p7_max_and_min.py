# create a max() function
def Maximum(List, *args):
    # 做一个函数解决代码重用
    def m(x):
        if type(List) == int or type(List) == float:
            Max = List
        else:
            Max = List[0]
        
        for i in x:
            if i > Max:
                Max = i
        return Max
    
    def data_process():
        result = [List,]
        result = [List,] + [i for i in args]
        return result
    
    if not args:
        # just List, and iterable
        return m(List)
    else:
        # multiple argument, each one single item
        if type(List) == int or type(List) == float:
            return m(data_process())
        
        # multiple arugments, each one iterable
        else:
            v = [m(List),] + [m(i) for  i in args]
            for i in data_process():
                if m(v) in i:
                    return i
            
a = [10.5, 2.3, 19.7]
b = [8.1, 10.2, 27.2]
c = [1.1, 2.0, 10.9]
print(Maximum([1.5,-2,-3]))
print(Maximum(1.5,2.3,-3,-4))
print(Maximum(a, b, c))

# TODO 还剩下Keyword参数
