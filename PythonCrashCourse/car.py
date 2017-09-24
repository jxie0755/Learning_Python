# Inheritance, Parent class, Child class, subclass, super class
# 讲电动车的电池拆分成一个独立的类, 这样电池的很多属性可以在这个类中细化
# 将此文件另存为Car.py以供其他文件导入类

class Car():
    '''car information summary'''
    def __init__(self, make, model, year, odometer=0):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer

    def get_car_info(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        print(long_name)

    def read_odometer(self):
        print('The car has been driven: ' + str(self.odometer) + ' miles')

    def update_odometer(self, mileage):
        if mileage > self.odometer:
            self.odometer = mileage
        else:
            print('you can\'t roll an odometer back!' )

    def increment_odometer(self, add_mileage):
        if add_mileage > 0:
            self.odometer += add_mileage
        else:
            print('what are you trying to do? \nYou think I am stupid?')

    def gas_tank(self, tank_size):
        print('fill up the gas tank', tank_size, 'gallons')

class ElectricCar(Car):
    '''Electric car information summary'''
    def __init__(self, make, model, year, odometer=0):
        super().__init__(make, model, year, odometer)
        self.BBBattery = Battery()  # 此处精髓在于, 在初始化阶段新添一个本来没有的参数,这个参数实际上是Battery类的实例.
        # 这样做的好处就在于, 每当生成一个ECar的实例(my_tesla), 都会自动生成一个电池属性,但它不属于ECar自身的实参,而是引用了来自Battery类的实例,所以有效的精简了每一个类的复杂程度.

        # self.battery_size = battery_size 取消原有的自带属性

    def get_car_info(self):
        Car.get_car_info(self)
        # print('Battery size: ', self.battery_size)

    def gas_tank(self, tank_size):
        print('You don\'t have a gas tank!')

class Battery():
    '''Battery class for ECar to use as attribute'''
    # 独立battery成为一个类
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def battery_info(self):
        print("The battery size is:", self.battery_size)

    #增加其他属性,比如续航历程
    def get_range(self):
        range = self.battery_size * 3 + 30
        print('The car\'s range is', range, 'miles')
