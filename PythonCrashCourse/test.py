# Inheritance, Parent class, Child class, subclass, super class
# 讲电动车的电池拆分成一个独立的类, 这样电池的很多属性可以在这个类中细化

class Car():
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.tank = Tank()

    def get_car_info(self):
        long_name = self.make + ' ' + self.model
        print('The car is', long_name)


class Tank():
    def __init__(self, tank_size=20):
        self.tank_size = tank_size

    def tank_info(self):
        print('The tank size is', self.tank_size, 'gallons')


my_car = Car('Audi', 'S4')
my_car.get_car_info()
my_car.tank.tank_info()
print(my_car.model)





