"""
    实例变量 - 练习
        1. 画出列表list_dogs内存图
        2. 画出调用find_dog_by_name函数内存图
"""


class Dog:
    def __init__(self, variety, name, age, weight):
        self.variety = variety
        self.name = name
        self.age = age
        self.weight = weight


d01 = Dog("拉布拉多", "米咻", 5, 70)
list_dogs = [
    d01,
    Dog("拉布拉多", "黑米", 4, 60),
    Dog("黑背", "哮天犬", 4, 30),
    Dog("藏獒", "小黑", 4, 80),
]


def find_dog_by_name(name):
    for dog in list_dogs:
        if dog.name == name:
            return dog


result = find_dog_by_name("黑米")
print(result.__dict__)
