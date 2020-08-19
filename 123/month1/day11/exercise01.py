"""
    类成员
        在类中方法外创建
            变量名 = 数据
        使用
            类名.变量名
    类方法
        创建
            @classmethod
            def 方法名(cls):

    类变量
        1.随类的加载而加载(存在优先于对象)
        2.只有一份被所有对象共享(实力方法可以操作类变量,但类方法不能操作实例变量)

"""


class ICBC:
    # 类变量:总行(大家)的数据
    total_money = 100000000

    # 类方法
    @classmethod
    def print_total_money(cls):
        # 通过类名方法读取类变量与通过cls访问类变量,效果相同,但后者可读性更高
        # print("总行的钱是",ICBC.total_money)
        print("总行的钱是",cls.total_money)  # 推荐

    def __init__(self, name, money):
        # 实例变量:支行(自己)的数据
        # 每次创建一个支行,就会在内存中分配一套实例变量
        self.name = name
        self.money = money
        # 总行钱减少
        ICBC.total_money -= self.money


# 通过实例对象访问实例成员
ttzh = ICBC("天坛支行", 1000000)
trtzh = ICBC("陶然亭支行", 2000000)
# 通过类访问类成员
# h = ICBC.total_money()


"""
    对象计数器
"""


class Wife:
    count = 0

    def __init__(self, name):
        self.name = name
        Wife.count += 1


w01 = Wife("建宁")
w02 = Wife("双儿")
w03 = Wife("阿珂")
w04 = Wife("翠花")
w05 = Wife("小郡主")
print(Wife.count)




"""
    Python变量总结
"""
#--------------------面向过程----------------------
# 全局变量
a = 10

def func01():
#局部变量 : 定义在函数中,整个函数可以使用
    b = 20

#---------------------面向对象---------------------
class MyClass:
    #类变量:定义在类中,通过类名使用
    d = 40
    def __init__(self):
        #实例变量:定义在构造函数中,通过对象使用
        #每个对象储存一份
        self.c = 30

m01 = MyClass()