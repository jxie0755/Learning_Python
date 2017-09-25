# 如果把ecar这个模块导入其超类car, 那么这个ecar的模块就包含全部的类,直接可以从ecar中调用Car和Electric Car
# 但是逻辑上来说,不建议这么做,还是分别import比较保险

import ecar

help(ecar.Car)
help(ecar.ElectricCar)

my_new_car = ecar.Car('Audi', 'S4', 2017)
my_new_ecar = ecar.ElectricCar('Tesla', 'Model S', 2016)

my_new_car.increment_odometer(2500)
my_new_car.get_car_info()
my_new_car.read_odometer()

my_new_ecar.get_car_info()
my_new_ecar.read_odometer()
my_new_ecar.gas_tank(20)
my_new_ecar.BBBattery.battery_info()
my_new_ecar.BBBattery.get_range()
