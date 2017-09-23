class Car():
    '''car information summary'''
    def __init__(self, odometer=19500):
        self.odometer = odometer

    def read_odometer(self):
        print('The car has been driven: ' + str(self.odometer) + ' miles')

Mcar = Car()
Mcar.read_odometer()

class Battery():
    # 独立battery成为一个类
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def battery_info(self):
        print("The battery size is: " + str(self.battery_size) + '.')

Tbattery = Battery()
Tbattery.battery_info()
