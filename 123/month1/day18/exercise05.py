"""
    内置高阶函数

"""
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

# 1.过滤器 : filter
for i in filter(lambda item: item.color == "白色", list_phones):
    print(i.__dict__)

# 2.映射 : map
for i in map(lambda item: item.brand, list_phones):
    print(i)

# 3.找最大值 : max
print(max(list_phones, key=lambda item: item.price).__dict__)

# 4.找最小值 : min
# 略...

# 5.排序 : sorted
# 注意 : 没有修改原列表(需要接收返回值)
# 升序
result = sorted(list_phones, key=lambda item: item.price)
# 降序
result = sorted(list_phones,key=lambda item: item.price,reverse = True)
