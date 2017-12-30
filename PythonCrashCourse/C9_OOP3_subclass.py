# Inheritance, Parent class, Child class, subclass, super class
# 继续使用Car的例子,在下面创建一个electric car的子类

class Car():
    '''car information summary'''
    def __init__(self, make, model, year, tank=35, odometer=500):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
        self.tank_size = tank

    def get_car_info(self):
        description = str(self.year) + ' ' + self.make + ' ' + self.model
        return description

    def read_odometer(self):
        print('The car has been driven: ' + str(self.odometer) + ' miles')
        return self.odometer

    def update_odometer(self, mileage):
        if mileage > self.odometer:
            self.odometer = mileage
        else:
            print('you can\'t roll an odometer back!')
        return Car.read_odometer(self)

    def increment_odometer(self, add_mileage):
        if add_mileage > 0:
            self.odometer += add_mileage
            print(add_mileage, 'miles has been added to the odometer')
        else:
            print('what are you trying to do? \nYou think I am stupid?')

    def fill_tank(self, volume):
        if volume <= self.tank_size:
            print('Fill up the gas', volume, 'gallons')
        else:
            print("You can't fill up the tank more than it can take!")


# 一个类继承继承 另一个类时，它将自动获得另一个类的所有属性和方法；原有的 类称为父类父类 ，而新类称为子类子类 。
# 子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。

class ElectricCar(Car):  # 创建子类的方法是创建时参数填写父类的名字
    # 添加一个电动车独有的属性,电瓶容量(battery_size)
    def __init__(self, make, model, year, battery_size, odometer=1000):  # 此处设置默认值,超类处的默认值被覆盖
    # 添加ECar的init有一个battery, 调整顺序,默认值odometer在最后.

        super().__init__(make, model, year, odometer)  # super()中不需要battery
                                                       # 注意超类的odometer不要再给默认值了,不然无法修改子类的odometer
                                                       # 注意这里gas tank不再是电动车的属性
        # Car.__init__(self, make, model, year, odometer) # also works

        self.battery_size = battery_size  # 新加一个子类特有的属性,battery_size

    def get_car_info(self):
        description = Car.get_car_info(self)
        return description

    # odometer section
    def read_odometer(self):
        return Car.read_odometer(self)

    def update_odometer(self, mileage):
        Car.update_odometer(self, mileage)
        return self.odometer

    def increment_odometer(self, add_mileage):
        Car.increment_odometer(self, add_mileage)

    # special attributes
    def battery(self):
        print('battery size is ' + str(self.battery_size))
        return self.battery_size

    def fill_tank(self, volume):
        print('Electric car does not have a gas tank!')



my_car = Car('Audi', 'S4', 2016)
print(my_car.get_car_info())

print(my_car.read_odometer())
print(my_car.update_odometer(1999))
my_car.increment_odometer(200)
print(my_car.read_odometer())

my_car.fill_tank(32)


print()

my_tesla = ElectricCar('Tesla', 'Model S', 2017, 99, 1000)
print(my_tesla.get_car_info())

print(my_tesla.read_odometer())
print(my_tesla.update_odometer(3000))
my_tesla.increment_odometer(500)
print(my_tesla.read_odometer())

# 若是父类中的某些方法,对于子类来说不能用,那么就在子类中创造同样名称的方法,然后返回一个不能用的print即可
my_tesla.fill_tank(32)
print(my_tesla.battery())

