# In learn_mod.py we define a variable and a functin to call this variable

# var1 = 5
# def fun1():
    # return var1

# var2 = 5
# def fun2():
    # return var2

import learn_mod

print(learn_mod.var1)    # >>> 5
learn_mod.var = 10
print(learn_mod.var1)    # >>> 10   # changed var value
print(learn_mod.fun1())  # >>> 10   # also change the call of var by fun()

from learn_mod import *

print(var2)    # >>> 5
var2 = 10
print(var2)    # >>> 10   # changed var value
print(fun2())  # >>> 5    # BUT does NOT change the call of var by fun()

# For more details in STOF:
# https://stackoverflow.com/questions/3536620/how-to-change-a-module-variable-from-another-module

p1 = learn_mod.People('denis')
print(p1)  # >>> denis

print(learn_mod.People.var_p)  # >>> people
print(p1.var_p)                # >>> people

p1.set_varP('WTF')
print(learn_mod.People.var_p)  # >>> WTF
print(p1.var_p)                # >>> WTF
