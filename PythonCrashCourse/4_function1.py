# Simply set func to replace print
def func(a):
    print(a)

func('dd')
print('dd')

# Passing information to function
def greet_user(username):
    print('Hello', username.title(), '!')

greet_user('Denis Xie')  # 记住这里输入string


# Positional Arguments
def pet(animal, name):
    print('I have a', animal)
    print('His name is', name.title())

pet('hamster', 'benny')       # 所谓positional是指的引用的时候必须按顺序放置实参.

# Keyword Arguments
def pet2(animal2, name2):
    print('I have a', animal2)
    print('His name is', name2.title())

pet2(animal2='hamster', name2='benny')  # 具体就是落实在实参被指定好.

# Default Values
def pet3(name3, animal3='dog'):  # 在def时就指定一个keyword作为默认,(默认实参后面不能再有非默认实参)
    print('I have a', animal3)
    print('His name is', name3.title())

pet3('jackie')  # 引用实参时,如果想用默认值,就不必在指定实参了.
