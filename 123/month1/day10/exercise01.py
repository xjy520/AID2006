#   类命名:所有单词开头大写,不要使用下划线隔开
class MobilePhone:
    def __init__(self,brand,price,color):
        self.brand=brand
        self.price=price
        self.color=color

    def call(self):
        print(self.brand,"手机打电话")

p01=MobilePhone("苹果",9999,"白色")
#   调用实例方法
p01.call()