# 将一个属性独立成为一个新的类
# 讲电动车的电池拆分成一个独立的类, 这样电池的很多属性可以在这个类中细化
# 将此文件另存为Car.py以供其他文件导入类

class Car(object):
    '''car information summary'''
    def __init__(self, make, model, year, type='sedan', tank=35):
        self.make = make
        self.model = model
        self.year = year
        self.type = type
        self.odometer = 0
        self.tank_size = tank

    def get_car_info(self):
        description = str(self.year) + ' ' + self.make + ' ' + self.model + ' ' + self.type
        return description

class ElectricCar(Car):
    def __init__(self, make, model, year, type='sports car'):
        super().__init__(make, model, year, type)
        self.odometer = 0
        self.battery = Battery()  # 将Battery类的一个实例Battery()做为电动车的一个属性
        # 每当方法__init__()被调用时，都将执行该操作；因此现在每个ElectricCar实例都包含一个自动创建的Battery实例。

    # special attributes
    def battery(self):
        print('battery size is ' + str(self.battery_size))
        return self.battery_size

class Battery(object):
    # 独立battery成为一个类
    def __init__(self, battery_size=50):
        self.battery_size = battery_size

    def battery_info(self):
        print("The battery size is:", self.battery_size)

    #增加其他属性,比如续航历程
    def get_range(self):
        range = self.battery_size * 3 + 30
        print('The car\'s range is', range, 'miles')

    def upgrade_battery(self):
        self.battery_size = 85

my_car = Car('Audi', 'S4', 2016)
print(my_car.get_car_info())

print()

my_tesla = ElectricCar('Tesla', 'Model S', 2017)
print(my_tesla.get_car_info())
print(type(my_tesla))  # >>> <class '__main__.ElectricCar'>
print()

my_tesla.battery.battery_info()  # 这里前半段my_tesla.battery表面是调用Ecar的battery属性,但是这个属性其实是Battery类的一个实例
my_tesla.battery.get_range()     # 后半段的battery_info()和get_range()实际是Battery类的方法
print(type(my_tesla.battery))    # >>> <class '__main__.Battery'> 属性为Battery的一个实例


print()
# 给Battery 类添加一个名为upgrade_battery() 的方法。这个方法检查电瓶容量，如果它不是85，就将它设置为85。
my_tesla.battery.upgrade_battery()
my_tesla.battery.battery_info()  # >>> The battery size is: 85
my_tesla.battery.get_range()     # >>> The car's range is 285 miles


# 这样做的目的就是把一个类的属性(如果该属性可以细化)本身做成一个类.
# 这个做法和创造子类是不同的逻辑.
# 子类的做法是将从父类中创造一个从属的分支
# 而这里的做法是将一个类的属性独立成一个类,没有从属关系
