# #   += : 尽量在原有基础上改变(不可变对象只能创新,可变对象不创新)
# class Vector:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def __iadd__(self, other):
#         self.x += other.x
#         self.y += other.y
#         return self
#
# v01 = Vector(1,2)
# v02 = Vector(3,4)
# v01 += v02 #v01.__iadd__(v02)
# print(id(v01))





class Phone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def __eq__(self, other):
        return self.brand == other.brand

    def __lt__(self, other):
        return self.price < other.priace


list_phones = [
    Phone("华为1", 5999, "蓝色"),
    Phone("华为2", 6999, "红色"),
    Phone("苹果1", 9999, "金色"),
    Phone("苹果2", 7999, "白色"),
    Phone("三星2", 4999, "白色"),
    Phone("华为1", 5999, "蓝色")
]
print(Phone("华为1", 5999, "蓝色")==Phone("华为1", 5999, "蓝色"))  # Phone("华为1", 5999, "蓝色").__eq__(Phone("华为1", 5999, "蓝色")
print(Phone("华为1", 4561, "带我去") in list_phones)

