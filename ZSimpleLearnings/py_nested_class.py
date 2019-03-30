# A test for nested class
# STOF: https://stackoverflow.com/a/719718/8435726

class Dog(object):

    class Cat(object):
        def __init__(self, age):
            self.age = age

        def meow(self):
            return 'I want fish!'

    def __init__(self, age):
        self.age = age

    def say(self, content):
        if content == 'Wooh':
            return 'WOOH!! WOOH!! WOOH!!'

        elif content == 'Meow':
            return Dog(1).Cat(0).meow()

        else:
            return 'Fuck off!'


dog = Dog(1)
cat = Dog(1).Cat(99)

print(dog.age) # >>>  0
print(cat.age) # >>>  99

print(dog.say('Wooh'))  # >>> WOOH!! WOOH!! WOOH!!
print(dog.say('Meow'))  # >>> I want fish!
print(cat.meow())       # >>> I want fish!
