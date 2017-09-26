from M_car import Car

class ElectricCar(Car):
    '''Electric car information summary'''
    def __init__(self, make, model, year, odometer=0):
        super().__init__(make, model, year, odometer)
        self.BBBattery = Battery()  # 此处精髓在于, 在初始化阶段新添一个本来没有的参数,这个参数实际上是Battery类的实例.
        # 这样做的好处就在于, 每当生成一个ECar的实例(my_tesla), 都会自动生成一个电池属性,但它不属于ECar自身的实参,而是引用了来自Battery类的实例,所以有效的精简了每一个类的复杂程度.

        # self.battery_size = battery_size 取消原有的自带属性

    def get_car_info(self):
        Car.get_car_info(self)
        # print('Battery size: ', self.battery_size)

    def gas_tank(self, tank_size):
        print('You don\'t have a gas tank!')

class Battery():
    '''Battery class for ECar to use as attribute'''
    # 独立battery成为一个类
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def battery_info(self):
        print("The battery size is:", self.battery_size)

    #增加其他属性,比如续航历程
    def get_range(self):
        range = self.battery_size * 3 + 30
        print('The car\'s range is', range, 'miles')
