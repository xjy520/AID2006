"""
    继承 - 数据
"""
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# 1. 子类没有构造函数,将使用父类构造函数
# class Student(Person):
#     pass
#
# s01 = Student("悟空",25)
# print(s01.__dict__)

# 2.子类构造函数,将覆盖父类构造函数
#   此时: 子类必须通过super()函数调用父类构造函数
# class Student(Person):
#     #子类构造函数参数:父类构造函数参数,子类构造函数
#     def __init__(self,name,age,score):
#         self.score = score
#         super().__init__(name,age)
#
# s01 = Student("悟空",25,100)
# print(s01.__dict__)


class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

class ElectricCar(Car):
    # 子类构造函数 : 父类构造函数参数 + 子类构造函数参数
    def __init__(self,brand,speed,battery,power):
        self.battery = battery
        self.power = power
        super().__init__(brand,speed)
e01= ElectricCar("五菱",150,15000,5000)
print(e01.__dict__)