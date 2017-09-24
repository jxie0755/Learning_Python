# 这是很重要的一次尝试,将整个Tank class独立出来,然后使得它能根据car model的不同来给出不同的tank size
# Link car model to the tank_size
# 这里是将一个dict放入在Car class类,然后Tank的method可以根据这个dict来给出不同的答案.
# 还不是完全体,因为tank信息还是存在了Car这个class里. 参见下一个版本5_OOP6.py

class Car():
    car_tank_sizes = {'Audi': {'A4': '20', 'A6': 25, 'A8': 30}}

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.tank = Tank(Car.car_tank_sizes.get(self.make, {}).get(self.model))

    def get_car_info(self):
        long_name = self.make + ' ' + self.model
        print('The car is', long_name)


class Tank():
    def __init__(self, tank_size):
        if (tank_size is None):
            self.tank_size = 20
        else:
            self.tank_size = tank_size

    def tank_info(self):
        print('The tank size is', self.tank_size, 'gallons')


my_car = Car('Audi', 'A6')
my_car.get_car_info()
my_car.tank.tank_info()
