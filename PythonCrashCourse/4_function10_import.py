# Then import it in a different file
# Import a module (pizza)

import pizza as p

help(pizza)  # 查询帮助文档,如果忘记了怎么用

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')


from pizza import make_pizza as mp  # use mp as an alias
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
