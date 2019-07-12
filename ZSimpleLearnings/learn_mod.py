# this is to learn how import command will work differently

print("this is global, will be seen even if selective import")

var1 = 5
def fun1():
    return var1

var2 = 5
def fun2():
    return var2

class People(object):
    var_p = "people"
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def set_varP(self, newstring):
        People.var_p = newstring
