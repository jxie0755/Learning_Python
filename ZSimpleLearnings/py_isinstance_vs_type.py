class Animal(object):
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    pass


monster = Animal('Denis')
hello_kitty = Cat('HK')

print(type(monster))      # >>> <class '__main__.Animal'>
print(type(hello_kitty))  # >>> <class '__main__.Cat'>

print(isinstance(monster, Animal)) # >>> True

# But check this:
print(isinstance(hello_kitty, Cat))     # >>> True
print(type(hello_kitty) == Cat)         # >>> True

print(isinstance(hello_kitty, Animal))  # >>> True
print(type(hello_kitty) == Animal)      # >>> False

# Therefore use isinstance is a better method than direct check type as it also return True of a sub-class instance to the parent class type.
