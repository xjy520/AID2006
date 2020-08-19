"""
    属性的各种写法
"""

# 写法1:读写属性
# 作用:可以在读取和写入时进行有效性验证
# 快捷键:props+回车
# class MyClass:
#     def __init__(self, data):
#         self.data = data
#
#     # @property
#     # def data(self):
#     #     return self.__data
#     #
#     # @data.setter
#     # def data(self,value):
#     #     self.__data = value
#
#
# m01 = MyClass(10)
# print(m01.data)
#

# 写法2:只读
# 作用:限制数据只能被读取,不能被修改
# 快捷键:prop+回车
# class MyClass:
#     def __init__(self, data):
#         self.__data = data
#
#     @property
#     def data(self):
#         return self.__data
#
#
# m01 = MyClass(10)
# #m01.data = 20  #报错,不能修改
# print(m01.data)
#
#
# # 写法3:只写属性
# # 作用:限制数据只能被修改,不能被读取
# class MyClass:
#     def __init__(self, data):
#         self.data = data
#
#     data = property()
#     @data.setter
#     def data(self,value):
#         self.__data = value
#
#     def set_data(self,value):
#         self.__data = value
#     property(None,set_data())
#
#
# m01 = MyClass(10)
# print(m01.data)



"""
    只写属性练习:
    限制鼠标实例变量在有效范围内
        品牌、      单价、   重量、    颜色
        字符小于6  0-10000、100-1000
"""


class Mouse:
    def __init__(self, brand, price, weight, colour):
        self.brand = brand
        self.price = price
        self.weight = weight
        self.colour = colour

    brand = property()

    @brand.setter
    def brand(self, value):
        if len(value) < 6:
            self.__brand = value

    price = property()

    @price.setter
    def price(self, value):
        if 0 <= value <= 10000:
            self.__price = value

    weight = property()

    def weight(self, value):
            if 100 <= value <= 1000:
                self.__weight = value


m01 = Mouse("双飞燕", 100, 150, "白色")
print(m01.brand)
print(m01.price)
print(m01.weight)
print(m01.colour)

