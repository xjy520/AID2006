"""
    分而治之
        将一个大的需求分解为许多类
        每个类处理一个独立的功能
    变则疏之
        变化的地方进行分装

"""


"""
    封装设计思想
        分而治之
        变则疏之
"""
# 需求:老张开车去东北
# 变化:老张 老李  老王  (数据不同)--->    使用对象区分
#      车  飞机  轮船  (行为不同)--->    使用类区分

# 写法1:直接创建对象调用
# 语义 :老张每次使用新车去某地

# 写法2:在构造函数中创建对象
# 语义 :老张每次开自己的车去某地

# 写法3:对象通过参数传递
# 语义 :老张使用(参数)去某地
class Person:
    def __init__(self,name):
        self.name = name
# 2.    self.car = Car()
    def go_to(self,position): #3. def go_to(self,position,car)
        print(self.name,"去",position)
# 2.    self.car.run()
    # 1.car = Car()
    # 1.car.run()
class Car:
    def run(self):
        print("开汽车")

lz = Person("老张")
car = Car()           #3.
lz.go_to("东北",car)  #3.