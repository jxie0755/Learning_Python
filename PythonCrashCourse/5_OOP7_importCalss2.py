import car

help(car.Car)
help(car.ElectricCar)
help(car.Battery)

my_new_car = car.Car('Audi', 'A8', 2017)
my_new_car.increment_odometer(2500)
my_new_car.get_car_info()
my_new_car.read_odometer()

my_new_ECar = car.ElectricCar('Tesla', 'Model S', 2017)
my_new_ECar.get_car_info()
my_new_ECar.read_odometer()
my_new_ECar.gas_tank(20)
my_new_ECar.BBBattery.battery_info()
my_new_ECar.BBBattery.get_range()


