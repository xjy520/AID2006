"""
    转换字符串
        __str__  --->   对人友好
        __repr__    --->    对机器友好
"""
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     对象 -> 字符串:  没有语法限制
#     def __str__(self):
#         return "我叫%s,今年%d"%(self.name,self.age) #必须是return
#     def __repr__(self):
#         return "Person('%s',%d)"%(self.name,self.age)
# #
# p01 = Person("悟空",24)
# #打印自定义对象
# print(p01)
#本质:
#   message = p01.__str__()#自定义对象 --->  字符串
#   print(message)

#价值:将字符串作为python代码执行
# message = p01.__repr__()    # "Person('悟空',25)"
# p02 = eval(message)     # 执行("Person('悟空',25)")
# p01.name = "大圣"     #更改p01
# print(p02)          #不会影响p02



#
# class Phone:
#     def __init__(self,brand,color,price):
#         self.brand = brand
#         self.color = color
#         self.price = price
#
#     def __str__(self):
#         return "%s手机%s颜色的价格是%s"%(self.brand,self.color,self.price)
#
# class Employees:
#     def __init__(self,cid,did,name,money):
#         self.cid = cid
#         self.did = did
#         self.name = name
#         self.money = money
#
#     def __str__(self):
#         return "%s的编号是%s,部门编号是%s,月薪是%s"%(self.name,self.cid,self.did,self.money)
#
# p01 = Phone("华为1","蓝",5999)
# print(p01)
# e01 = Employees(1001,9002,"师傅",60000)
# print(e01)


class Phone:
    def __init__(self,brand,color,price):
        self.brand = brand
        self.color = color
        self.price = price

    def __repr__(self):
        return "Phone('%s','%s',%d)"%(self.brand,self.color,self.price)

p01 = Phone("华为","白色",10000)
print(p01)
p02 = eval(p01.__repr__())
p01.brand = "苹果"
print(p02)
print(p01)