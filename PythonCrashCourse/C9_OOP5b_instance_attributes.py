# 这是很重要的一次尝试,将整个Tank class独立出来,然后使得它能根据car model的不同来给出不同的tank size
# Link car model to the tank_size
# 完全体: 将car_tank_size也放入到Tank的class中 -- 彻底的独立.
# 利用嵌套的dict,使得不单能够分辨model,连make也可以分辨

class Car():
    def __init__(self, make, model):
        self.makeC = make
        self.modelC = model
        self.tank = Tank(self.makeC, self.modelC)

    def get_car_info(self):
        long_name = self.makeC + ' ' + self.modelC
        print('The car is', long_name)

# 要注意这里的make和model分别是跟的那个类里的make和model
# 这里生成Tank()实例时,引用的是Car实例的makeC和modelC作为参数
# 然后这个makeC和modelC变成了Tank()实例中的makeT和modelT, 根据方法,寻找Tank中的dict数据得到相对应的size

class Tank():
    # This is a better way, because the mapping should be in the Tank
    car_tank_sizes = {'Audi': {'A4': 20, 'A6': 25, 'A8': 30},
                      'BMW': {'Series 3': 21, 'Series 5': 26, 'Series 7': 31}}
                      # attributes does not need to be in __init__()

    def __init__(self, makeT, modelT):
        self.tank_size = Tank.car_tank_sizes.get(makeT, {}).get(modelT)

        # 这样虽然可以实现,如果出现读取内置mapping之外的数据,则会引发KeyError, 除非引入try,except写法
        # self.tank_size = Tank.car_tank_sizes[f'{makeT}'][f'{modelT}']

        # 这样可以使用itemgetter得到数据,同样会引发KeyError
        # from operator import itemgetter
        # self.tank_size = itemgetter(modelT)(itemgetter(makeT)(Tank.car_tank_sizes))


    def tank_info(self):
        if self.tank_size == None:  # 设置一个if条件,避免意外
            print('We don\'t have information for this car')
        else:
            print('The tank size is', self.tank_size, 'gallons')


my_car1 = Car('Audi', 'A6')
my_car1.get_car_info()
my_car1.tank.tank_info()

my_car2 = Car('BMW', 'Series 5')
my_car2.get_car_info()
my_car2.tank.tank_info()

my_car3 = Car('Mercedez', 'Series E')  # get()函数引发None
my_car3.get_car_info()
my_car3.tank.tank_info()

