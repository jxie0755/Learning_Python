# Inheritance, Parent class, Child class, subclass, super class
# 讲电动车的电池拆分成一个独立的类, 这样电池的很多属性可以在这个类中细化
# 将此文件另存为Car.py以供其他文件导入类

class Car():
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

    # special attributes
    def battery(self):
        print('battery size is ' + str(self.battery_size))
        return self.battery_size

class Battery():
    # 独立battery成为一个类
    def __init__(self, battery_size=50):
        self.battery_size = battery_size

    def battery_info(self):
        print("The battery size is:", self.battery_size)

    #增加其他属性,比如续航历程
    def get_range(self):
        range = self.battery_size * 3 + 30
        print('The car\'s range is', range, 'miles')


my_car = Car('Audi', 'S4', 2016)
print(my_car.get_car_info())

print()

my_tesla = ElectricCar('Tesla', 'Model S', 2017)
print(my_tesla.get_car_info())

print()

my_tesla.battery.battery_info()
# 注意这里,battery是来自my_tesla的self.battery属性,而不是Battery这个class的名字!!
my_tesla.battery.get_range()



