# 创建dog类, 为其设置名字和年龄,赋予蹲下和打滚的能力

class Dog(object):
    '''a simple attemp to model a dog'''

    def __init__(self, name, age, doggy):
        self.dog_name = name
        self.dog_age = age
        self.__doggy = doggy  # attribute前加双__使得属性变为私有,外部无法访问

    def sit(self):
        print(self.dog_name.title() + ' is now sitting')

    def roll_over(self):
        print(self.dog_name.title() + ' rolled over!')

    def doggystyle(self):
        print('doggy is', self.__doggy)

myDog = Dog('didi', 3, '123')
print('Dog name is ' + myDog.dog_name.title() +
      '. Dog age is ' + str(myDog.dog_age))

myDog.sit() # 等同于 Dog.sit(myDog)
myDog.roll_over() # 等同于 Dog.roll_over(myDog)
# 区别只在于代码简单度,但是后者更好理解
# 两者逻辑不同,前者在于面向对象,后者在面向过程, 还是推荐前者
# 请教STOF网友,得到结论,第二种方式不符合OOP精神.在面对无数对象时,需要花太多时间去确定object的类型.

print(myDog.dog_name)  # >>> didi
print(myDog.dog_age)   # >>> 3
# print(myDog.__doggy)  # 此处会报错,因为__doggy无法直接被调用
print(myDog.doggystyle())  # >>> doggy is 123  # 而类方法调用__doggy则可输出结果.

print(dir(myDog))
