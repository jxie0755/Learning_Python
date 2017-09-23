# Inheritance, Parent class, Child class, subclass, super class
# 讲电动车的电池拆分成一个独立的类, 这样电池的很多属性可以在这个类中细化

class Car():
    '''car information summary'''
    def __init__(self, make, model, year, odometer):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer

    def get_car_info(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

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

class Battery():
    # 独立battery成为一个类
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def battery_info(self):
        print("The battery size is:", self.battery_size)

class ElectricCar(Car):
    def __init__(self, make, model, year, odometer):
        super().__init__(make, model, year, odometer)
        self.battery = Battery()
        # self.battery_size = battery_size 拆分电池属性出来, 设置容量的99

    def get_car_info(self):
        print(Car.get_car_info(self))
        # print('Battery size: ', self.battery_size)

    def gas_tank(self, tank_size):
        print('You don\'t have a gas tank!')


my_car = Car('Audi', 'S4', 2016, 0)
print(my_car.get_car_info())
my_car.read_odometer()
my_car.gas_tank(40)

print()

my_tesla = ElectricCar('Tesla', 'Model S', 2017, 13500)
my_tesla.get_car_info()
my_tesla.battery.battery_info()
my_tesla.read_odometer()
my_tesla.gas_tank(40)

