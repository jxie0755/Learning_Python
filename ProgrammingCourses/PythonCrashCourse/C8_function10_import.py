# Then import it in a different file
# Import a module (M_pizza)

import M_pizza as p

help(p)  # 查询帮助文档,如果忘记了怎么用

p.make_pizza(16, "pepperoni")
p.make_pizza(12, "mushroom", "green peppers", "extra cheese")


from M_pizza import make_pizza as mp  # use mp as an alias
mp(16, "pepperoni")
mp(12, "mushrooms", "green peppers", "extra cheese")
