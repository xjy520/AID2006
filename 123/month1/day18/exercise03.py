"""
    需求2:
        定义函数,删除手机列表中所有蓝色手机
        定义函数,删除手机列表中所有单价大于7000的手机
"""
import iterable_tools

class Phone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

list_phones = [
    Phone("华为1", 5999, "蓝色"),
    Phone("HUAWEI2", 6999, "红色"),
    Phone("苹果1", 9999, "金色"),
    Phone("苹果2", 7999, "白色"),
    Phone("三星2", 4999, "白色"),
]

# iterable_tools.IterableHelper.delete(list_phones,lambda item:item.color == "蓝色")
# for i in list_phones:
#     print(i.__dict__)
#
# iterable_tools.IterableHelper.delete(list_phones,lambda item:item.price > 7000)
# for i in list_phones:
#     print(i.__dict__)

print(iterable_tools.IterableHelper.find_max(list_phones, lambda item: item.price).__dict__)

print(iterable_tools.IterableHelper.find_max(list_phones,lambda item:len(item.brand)).__dict__)

print(iterable_tools.IterableHelper.count(list_phones,lambda item:item.color == "白色"))

print(iterable_tools.IterableHelper.count(list_phones,lambda item:item.price > 7000))