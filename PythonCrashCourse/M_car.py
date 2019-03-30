# Inheritance, Parent class, Child class, subclass, super class
# 讲电动车的电池拆分成一个独立的类, 这样电池的很多属性可以在这个类中细化
# 将此文件另存为Car.py以供其他文件导入类

class Car():
    '''car information summary'''
    def __init__(self, id, make, model, year, odometer=0):
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
        print('new car obtained')

    def __str__(self):  # a string version to represent the object (used as a description)
        # return f'{self.year} {self.make} {self.model}'
        return 'car' + self.id

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

DenisNewCar = Car('001','Audi', 'A4', '2017')  # >>> print 'new car obtained' when create the object
print(DenisNewCar)  # >>> '2017 Audi A4' used as a 'name' to represent the object
                    # >>> 'car001' as an ID
