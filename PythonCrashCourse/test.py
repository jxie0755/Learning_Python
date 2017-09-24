class Car():
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.tank = Tank(Tank.car_tank_sizes.get(self.make,{}).get(self.model))

    def get_car_info(self):
        long_name = self.make + ' ' + self.model
        print('The car is', long_name)

class Tank():
    car_tank_sizes = {'Audi': {'A4': '20', 'A6': 25, 'A8': 30}}

    def __init__(self, tank_size):
        self.tank_size = tank_size

    def tank_info(self):
        print('The tank size is', self.tank_size, 'gallons')

my_car = Car('Audi', 'A6')
my_car.get_car_info()
my_car.tank.tank_info()
