"""
    定义函数,在全局变量list_phones中,查找单价小于6000的所有手机
    定义函数,在全局变量list_phones中,查找蓝色手机(单个)
"""

class Phone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color


# 1
list_phones = [
    Phone("华为1", 5999, "蓝色"),
    Phone("华为2", 6999, "红色"),
    Phone("苹果1", 9999, "金色"),
    Phone("苹果2", 7999, "白色"),
    Phone("三星2", 4999, "白色"),
]

def func01():
    for phone in list_phones:
        if phone.price < 6000:
            yield phone

def func02():
    for phone in list_phones:
        if phone.color == "蓝色":
            return phone

