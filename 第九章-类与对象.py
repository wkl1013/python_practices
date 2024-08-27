# # 创建一个类
# class Dog:
#
#     def __init__(self, name, age):
#         """初始化属性：name 和 age"""
#         self.name = name
#         self.age = age
#         self.color = 'yellow'  # 给属性设置默认值
#
#     def sit(self):
#         print(f"{self.name}收到命令后坐下。")
#
#     def roll_cover(self):
#         print(f"{self.name}在地上打滚。")
#
#     def get_descriptions(self):
#         descriptions = f"{self.name}, {self.age}, {self.color}"
#         return descriptions
#
#
# # 创建一个狗类的实例
# my_dog = Dog('Mike', 3)
# print(my_dog.name, my_dog.age)
# my_dog.sit()
# my_dog.roll_cover()
# print(my_dog.get_descriptions())



# 类的继承
class Car:
    """一次模拟汽车的类"""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reading = 0

    # 展示汽车的相关属性
    def get_description(self):
        long_name = f"{self.brand}, {self.model}, {self.year}"
        return long_name

    # 展示汽车的里程数
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    # 更新里程数
    def update_odometer(self, new_mile):
        if new_mile >= self.odometer_reading:
            self.odometer_reading = new_mile
        else:
            print("你不能指定这个里程，因为他比原里程还短。")

    def increase_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """创建一个电动车类，继承自上述的汽车类"""

    # 定义本类的属性
    def __init__(self, brand, model, year):
        """初始化父类属性， 表明本类中的相关属性继承自父类属性"""
        super().__init__(brand, model, year)
        self.battery_size = 75  # 定义本类独有的属性，电池容量

    # 父类方法的重写覆盖
    def get_description(self):
        long_name = f"{self.brand}, {self.model}, {self.year}, {self.battery_size}"
        return long_name

    # 子类中新增加的方法
    def describe_battery(self):
        print(f"this cat has a {self.battery_size}-Kwh battery")

my_tesla = ElectricCar('tesla', 'model-Y', '2020')
print(my_tesla.get_description())



#  Python中常用的标准库
from random import randint
print(randint(1,100))

from random import choice, choices
players = ["科比", "C罗", "梅西", "马龙"]
luck_one = choice(players)
print(luck_one)
