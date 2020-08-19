"""
    三大特征
        1.封装    定义:将一些基本数据类型复合程一个自定义类型
                  优势:将数据与对数据的操作相关联
                      代码可读性更高

"""
"""
    行为封装
        创建类型时,应该保障数据在有效范围内
        对外提供必要功能(如:读取年龄,修改年龄),隐藏实现细节(保护年龄范围)
        1.方法内部操作私有变量(私有变量是真是储存的数据)
        2.@property 在创建属性对象并且将下面的方法作为参数
          再将对象的地址交给下面的方法名称关联
             属性名 = property(读取方法)
        3.@age.setter
             属性名.setter(写入方法)
"""
# 需求:保护数据有效范围 22 - 30
class Wife:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property       #创建属性对象 property(读取方法)
    def age(self):
        return self._age    #会执行age(self,value)函数

    @age.setter
    def age(self, value):
        if 22 < value < 30:
            self._age = value
        else:
            raise Exception("我不要")


w01 = Wife("双儿", 25)


"""
    练习:
    创建敌人类
    创建实例变量并保证数据在有效范围内
        姓名,血量,攻击
            0-100  1-30
"""


class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 0 <= value <= 100:
            self.__hp = value
        else:
            raise Exception("血量错误")

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        if 0 <= value <= 30:
            self.__damage = value
        else:
            raise Exception("数据错误")


e01 = Enemy("灭霸", 100, 30)
print(e01.name)
print(e01.hp)
print(e01.damage)


"""
    私有成员 : 只能在类中访问,类外不能访问
        做法 : 以双下划线命名
        本质 : 看上去成员名称为__data,实际_MyClass__data
                    双下划线家名称     单下划线加类名加双下划线加名称
"""
# class MyClass:
#     def __init__(self):
#         self.__data = 10
#
#     def __func01(self):
#         print("func01")
#
#
# m01 = MyClass()
# # print(m01.__data)   #不能在类外访问私有变量
# #不建议
# m01._MyClass__data = 20
# print(m01._MyClass__data)
# print(m01.__dict__)

