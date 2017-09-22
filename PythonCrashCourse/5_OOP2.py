# 创建汽车类,信息汇总

# 重点是如何修改属性(odometer)里程数
# 可以不为属性设置实参,而是在设定初始值直接赋值.
# 随后创立方法来读取这个属性, 也可以在对象中临时修改这个属性

# 就算是设定为实参,也是可以修改的,方法完全相同
# 要么就设定实参,在创造对象是就赋予一个数,要么就不设定实参,但是赋予一个默认值,二者皆可

class Car():
    '''car information summary'''
    def __init__(self, make, model, year, odometer):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer

    def get_car_info(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        print('The car has been driven: ' + str(self.odometer) + ' miles')

    # 添加一个方法来改变里程表读数
    def update_odometer(self, mileage):
        # 添加了一个禁止回调里程表的设置
        if mileage > self.odometer:
            self.odometer = mileage
        else:
            print('you can\'t roll an odometer back!' )

    # 设置一个增加里程的方法,在原里程读数上增加里程
    def increment_odometer(self, add_mileage):
        # 同样设置一禁止负数增量,避免被人回调.
        if add_mileage > 0:
            self.odometer += add_mileage
        else:
            print('what are you trying to do? \nYou think I am stupid?')

# 注意:以上两个方法只能禁止用户回调里程表,如果有人能接触原代码,则可以通过直接变动属性值回调.

my_car = Car('Audi', 'S4', 2016, 0)
print(my_car.get_car_info())
my_car.read_odometer()

# 修改odometer数字
my_car.odometer = 18000
my_car.read_odometer()

# 使用方法修改odometer
my_car.update_odometer(16000)
my_car.read_odometer()

my_car.increment_odometer(2000)
my_car.read_odometer()

my_car.increment_odometer(-1000)
my_car.read_odometer()
