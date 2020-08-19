"""
    静态方法 : 表达一种工具,不能(需要)操作对象或类成员
    使用方式 : 类.静态方法名
    因为在项目中处处需要使用通用函数
    所以将通用函数统一储存在Common包的iterable_tools的模块中
"""


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

import iterable_tools


def color(item):
    return item.color == "白色"


for i in iterable_tools.IterableHelper.find_all(list_phones, color):
    print(i.__dict__)


def brand(item):
    return item.brand == "苹果2"

print(iterable_tools.IterableHelper.find_single(list_phones,brand).__dict__)
