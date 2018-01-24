# This is to learn the difference and relationship between class attributes and instance attributes

class foo(object):
    c = 'class attribute'
    def __init__(self, i):
        self.i = i

o1 = foo('o1')
o2 = foo('o2')

print(o1.i, o2.i)  # >>> o1 o2
print(o1.c, o2.c)  # >>> class attribute class attribute

o1.c = 'WTF'       # BE CAREFUL!!! by doing so, we create o1.c override foo.c (become instance attributes)
print(o1.c, o2.c)  # >>> WTF class attribute  # revise o1.c does not change o2.c
print(foo.c)       # >>> class attribute      # revise o1.c does not change foo.c

foo.c = 'Really?'
print(o1.c, o2.c)  # >>> WTF really?          # only change o2.c, because o1.c got override by previous operation.

# In generall, we do not override class attribute with instance attribute.
# And class attributes should be used separately for systematic purpose.
# ALways call class attribute by ClassName.class_attribute
