# 9-1 餐馆 ：创建一个名为Restaurant 的类，其方法__init__() 设置两个属性：restaurant_name 和cuisine_type 。
# 创建一个名 为describe_restaurant() 的方法和一个名为open_restaurant() 的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
# 根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用前述两个方法。

class Restaurant(object):
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'{self.restaurant_name} serves {self.cuisine_type} food')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is now opened for business!')

    def set_number_served(self, new_num):
        self.number_served = new_num

    def increment_number_served(self, increment):
        self.number_served += increment

elgalloblanco = Restaurant('El Gallo Blanco', 'Mexican')
teressa = Restaurant("Teressa's Cafe", 'Italian')

print(elgalloblanco.restaurant_name)  # >>> El Gallo Blanco
print(teressa.cuisine_type)  # >>> Italian

elgalloblanco.describe_restaurant()  # >>> El Gallo Blanco serves Mexican food
teressa.open_restaurant()  # >>> Teressa's Cafe is now opened for business!

print(elgalloblanco.number_served)  # >>> 0
elgalloblanco.number_served = 100
print(elgalloblanco.number_served)  # >>> 100

teressa.set_number_served(1234)
print(teressa.number_served)  # >>> 1234
teressa.increment_number_served(234)
print(teressa.number_served)  # >>> 1468
