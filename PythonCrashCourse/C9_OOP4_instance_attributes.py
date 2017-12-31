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

    def read_odometer(self):
        print('The car has been driven: ' + str(self.odometer) + ' miles')
        return self.odometer

    def update_odometer(self, mileage):
        if mileage > self.odometer:
            self.odometer = mileage
        else:
            print('you can\'t roll an odometer back!')
        return Car.read_odometer(self)

    def increment_odometer(self, add_mileage):
        if add_mileage > 0:
            self.odometer += add_mileage
            print(add_mileage, 'miles has been added to the odometer')
        else:
            print('what are you trying to do? \nYou think I am stupid?')

    def fill_tank(self, volume):
        if volume <= self.tank_size:
            print('Fill up the gas', volume, 'gallons')
        else:
            print("You can't fill up the tank more than it can take!")

class ElectricCar(Car):
    def __init__(self, make, model, year, type='sports car'):
        super().__init__(make, model, year, type)
        self.odometer = 0
        self.battery = Battery()

    # special attributes
    def battery(self):
        print('battery size is ' + str(self.battery_size))
        return self.battery_size

    # 如果父类的方法对于子类不再合适,那么可以进行重写来覆盖
    def fill_tank(self, volume):
        print('Electric car does not have a gas tank!')
        # 以上方法如果被删除,则会转而执行父类的相同名称的方法

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
my_car.read_odometer()
my_car.fill_tank(40)

print()

my_tesla = ElectricCar('Tesla', 'Model S', 2017)
my_tesla.get_car_info()
my_tesla.battery.battery_info()
# 注意这里,BBBattery是来自my_tesla的self.BBBattery属性,而不是Battery这个class的名字!!
my_tesla.read_odometer()
my_tesla.fill_tank(40)
my_tesla.battery.get_range()



