# Inheritance, Parent class, Child class, subclass, super class
# 继续使用Car的例子,在下面创建一个electric car的子类

class Car(object):
    """car information summary"""
    def __init__(self, make, model, year, type="sedan", tank=35):
        self.make = make
        self.model = model
        self.year = year
        self.type = type
        self.odometer = 0
        self.tank_size = tank

    def get_car_info(self):
        description = str(self.year) + " " + self.make + " " + self.model + " " + self.type
        return description

    def read_odometer(self):
        print("The car has been driven: " + str(self.odometer) + " miles")
        return self.odometer

    def update_odometer(self, mileage):
        if mileage > self.odometer:
            self.odometer = mileage
        else:
            print("you can't roll an odometer back!")
        return Car.read_odometer(self)

    def increment_odometer(self, add_mileage):
        if add_mileage > 0:
            self.odometer += add_mileage
            print(add_mileage, "miles has been added to the odometer")
        else:
            print("what are you trying to do? \nYou think I am stupid?")

    def fill_tank(self, volume):
        if volume <= self.tank_size:
            print("Fill up the gas", volume, "gallons")
        else:
            print("You can't fill up the tank more than it can take!")


# 一个类继承继承 另一个类时，它将自动获得另一个类的所有属性和方法；原有的 类称为父类父类 ，而新类称为子类子类 。
# 子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。

class ElectricCar(Car):  # 创建子类的方法是创建时参数填写父类的名字
    # 添加一个电动车独有的属性,电瓶容量(battery_size)
    def __init__(self, make, model, year, type="sports car", battery_size=50):  # 此处设置新默认值,而不是继承超类
        #  添加ECar的init有一个battery属性,设置默认值为50

        super().__init__(make, model, year, type)  # super()用于继承
                                             # 注意这里gas tank不再是电动车的属性
        # Car.__init__(self, make, model, year) # also works
        self.odometer = 100  # 由于Ecar有新的默认odometer reading,所以不要继承父类,而是新写一个odometer属性
        self.battery_size = battery_size  # 新加一个子类特有的属性,battery_size

    # 由于子类继承父类的方法,所以不需要再写一次相同的方法

    # special attributes
    def battery(self):
        print("battery size is " + str(self.battery_size))
        return self.battery_size

    # 如果父类的方法对于子类不再合适,那么可以进行重写来覆盖
    def fill_tank(self, volume):
        print("Electric car does not have a gas tank!")
        # 以上方法如果被删除,则会转而执行父类的相同名称的方法

# 关于默认属性的设置 -
# 如果不同车型会有一个不同的值,比如battery size或者gas tank size,那么最佳是设置为:
# parameter = default, self.parameter = parameter
# 如果所有车都会有一个固定的起始值,比如odometer,刚造出来的车一定是0,那么最佳设置:
# 不设置paramter, 但是设置self.parameter = 0.
# 这样做好处就是,在创造实例时,不需要输入一个固定的,重复的参数.


my_car = Car("Audi", "S4", 2016)
print(my_car.get_car_info())

print(my_car.read_odometer())
print(my_car.update_odometer(1999))
my_car.increment_odometer(200)
print(my_car.read_odometer())

my_car.fill_tank(32)


print()

my_tesla = ElectricCar("Tesla", "Model S", 2017)
print(my_tesla.get_car_info())

print(my_tesla.read_odometer())
print(my_tesla.update_odometer(3000))
my_tesla.increment_odometer(500)
print(my_tesla.read_odometer())

# 若是父类中的某些方法,对于子类来说不能用,那么就在子类中创造同样名称的方法,然后返回一个不能用的print即可
my_tesla.fill_tank(32)
print(my_tesla.battery())
print(my_tesla.type)
