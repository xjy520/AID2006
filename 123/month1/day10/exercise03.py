"""
    实例变量 - 练习
        1.画出列表list_dogs内存图
        2.画出调用find_dog_by_name函数内存图
"""


class Dog:
    def __init__(self, varieties, name,  age, weight):
        self.varieties = varieties
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


# def find_dog_by_name(name):
#     for dog in list_dogs:
#         if dog.name == name:
#             return dog
#
#
# result = find_dog_by_name("黑米")
# print(result.name)


#   练习1 : 创建函数,在狗列表中查找品种是"黑背"的狗对象(如果有多个也查找第一个)
#   练习2 : 创建函数,在狗列表中查找所有体重大于50的狗对象

# def find_dog_by_varieties(varieties):
#     for dog in list_dogs:
#         if dog.varieties == varieties:
#             return dog
#
# result=find_dog_by_varieties("黑背") #这是打印的狗列表的内存地址
# print(result.name)

def find_dog_by_weight(weight):
    list=[]
    for dog in list_dogs:
        if dog.weight > 50:
            list.append(dog)


