# 使用import命令,记得如果不是用from...import, 必须要加引用前缀 (car.Car等等)

import car0

help(car0.Car)
help(car0.ElectricCar)
help(car0.Battery)

my_new_car = car0.Car('Audi', 'A8', 2017)
my_new_car.increment_odometer(2500)
my_new_car.get_car_info()
my_new_car.read_odometer()

my_new_ecar = car0.ElectricCar('Tesla', 'Model S', 2017)
my_new_ecar.get_car_info()
my_new_ecar.read_odometer()
my_new_ecar.gas_tank(20)
my_new_ecar.BBBattery.battery_info()
my_new_ecar.BBBattery.get_range()


