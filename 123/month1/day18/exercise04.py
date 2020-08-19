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

print(iterable_tools.IterableHelper.verdict(list_phones,lambda item:item.brand == "三星2"))

print(iterable_tools.IterableHelper.verdict(list_phones,lambda item:item.price > 10000))

iterable_tools.IterableHelper.sort(list_phones,lambda item:item.price)
print(list_phones)

iterable_tools.IterableHelper.sort(list_phones,lambda item:len(item.brand))
print(list_phones)