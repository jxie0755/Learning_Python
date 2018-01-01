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

class Tank():
    # This is a better way, because the mapping should be in the Tank
    car_tank_sizes = {'Audi': {'A4': 20, 'A6': 25, 'A8': 30},
                      'BMW': {'Series 3': 21, 'Series 5': 26, 'Series 7': 31}}
                      # attributes does not need to be in __init__()

    def __init__(self, makeT, modelT):
        self.tank_size = Tank.car_tank_sizes.get(makeT, {}).get(modelT)

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

my_car3 = Car('Mercedez', 'Series E')
my_car3.get_car_info()
my_car3.tank.tank_info()
