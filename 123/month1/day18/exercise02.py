"""
    lambda 表达式
        匿名方法

"""
# 普通函数
def func01(p1,p2):
    return p1 > p2


# 匿名方法:
# 写法一 : 有参数有返回值
lambda p1, p2: p1 > p2

# 写法二 : 有参数无返回值
def func02(p1):
    print("参数是:",p1)

lambda p1: print("参数是:", p1)

# 写法三 : 无参数有返回值
def fun03():
    return 123

lambda : 132

# 写法四 : 无参无返回值
def func04():
    print("hello world")

lambda : print("hello world")

# 普通函数可以,但是lambda不支持的写法
def func05():
    for i in range(5):
        print(i)

# 注意1 : python语言的lambda函数体只能有一句话
# lambda : for i in range(5):print(i)   报错

def func06(p1):
    p1[0] = 10

list01 = [1]
func06(list01)

#注意2 : python语言的lambda函数不支持赋值语句
# lambda p1:p1[0] = 10


"""
    lambda 应用 - 作为函数的实参
        定义函数,只为传参,需要使用lambda
"""

import iterable_tools

class Phone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

list_phones = [
    Phone("华为1", 5999, "蓝色"),
    Phone("华为2", 6999, "红色"),
    Phone("苹果1", 9999, "金色"),
    Phone("苹果2", 7999, "白色"),
    Phone("三星2", 4999, "白色"), ]
#   将查找条件定义在函数中
# def color(item):
#     return item.color == "白色"
#
# for i in iterable_tools.IterableHelper.find_all(list_phones, color):
#     print(i.__dict__)

result = iterable_tools.IterableHelper.find_all(list_phones,lambda item:item.color == "白色")

"""
    定义函数,在手机列表中,获取所有手机的品牌
    定义函数,在手机列表中,获取所有手机的品牌和颜色
"""
result01 = iterable_tools.IterableHelper.find_all_phone(list_phones,lambda item:item.brand)
for i in result01:
    print(i.__dict__)

result02 = iterable_tools.IterableHelper.find_all_phone(list_phones,lambda  item:(item.brand,item.color))
for i in result02:
    print(i)
