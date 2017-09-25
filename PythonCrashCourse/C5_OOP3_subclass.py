# Inheritance, Parent class, Child class, subclass, super class
# 继续使用Car的例子,在下面创建一个electric car的子类

class Car():
    '''car information summary'''
    def __init__(self, make, model, year, odometer=5500):
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

class ElectricCar(Car):
    # 添加一个电动车独有的属性,电瓶容量(battery_size)
    def __init__(self, make, model, year, battery_size, odometer=13500):  # 此处设置默认值,超类处的默认值被覆盖
    # 添加ECar的init有一个battery, 调整顺序,默认值odometer在最后.

        super().__init__(make, model, year, odometer)  # super中不需要battery
                                                      # 注意超类的odometer不要再给默认值了,不然无法修改子类的odometer
        # Car.__init__(self, make, model, year, odometer) # also works

        self.battery_size = battery_size

    def get_car_info(self):
        print(Car.get_car_info(self))
        print('Battery size:', self.battery_size)

    def gas_tank(self, tank_size):
        print('You don\'t have a gas tank!')

my_car = Car('Audi', 'S4', 2016)
print(my_car.get_car_info())
my_car.read_odometer()
my_car.gas_tank(40)

print()

my_tesla = ElectricCar('Tesla', 'Model S', 2017, 99)
my_tesla.get_car_info()
my_tesla.read_odometer()
my_tesla.gas_tank(40)
# 若是父类中的某些方法,对于子类来说不能用,那么就在子类中创造同样名称的方法,然后返回一个不能用的print即可

