"""
    面向对象
        步骤:
            1.识别对象
            2.分配职责
            3.建立交互
        特征:
            1.封装:分
            2.继承:隔
            3.多态:做
        原则:
            1.开闭原则 - 目标
            2.单一职责 - 对封装的补充
            3.依赖倒置 - 引出继承
            4.组合复用 - 继承是抽象变化,不是代码复用
    程序:  曾经 - 程序= 算法 + 数据结构 (面向过程)
          现今 - 程序 = 对象 + 交互  (面向对象)
"""


"""
    实现添加商品信息
"""
class CommodityModle:
    def __init__(self,cid,name,price,sid = 0):
        self.cid = cid
        self.name = name
        self.price = price
        self.sid = sid

class CommodityView:
    def __init__(self):
        self.contort = CommodityController()

    def display(self):
        print("1:获取商品信息")
        print("2:添加商品信息")
        print("3:删除商品信息")
        print("4:修改商品信息")
        print("5:获取最贵的商品信息")

    def select_menu(self):
        item = input("请输入选项:")
        if item == "2":
            return self.input_commodity()
        if item == "5":
            return self.order_price_list()

    def input_commodity(self):
        cid = input("输入商品编号:")
        name = input("输入商品名称:")
        price = input("输入商品价格:")
        com = CommodityModle(cid,name,price)
        self.contort.add_commodity(com)

    def delete_commdity(self):
        sid = int(input("输入商品编号:"))
        if self.contort.remove_commodity(sid)== True:
            print("删除成功")
        else:
            print("删除失败")

    def order_price_list(self):
        self.contort.max_price_list()
        print(self.contort.max_price_list().__dict__)


class CommodityController:
    def __init__(self):
        self.list_commodity = []
        self.start_sid = 1001

    def add_commodity(self,infos):
        infos.sid = self.start_sid
        self.start_sid += 1
        self.list_commodity.append(infos)

    def remove_commodity(self,sid):
        for i in self.list_commdity:
            if i.sid == sid:
                self.list_commodity.remove(i)
                return True
        return False

    def max_price_list(self):
        max_price = self.list_commodity[0]
        for i in range(0,len(self.list_commodity)):
            if max_price.price < self.list_commodity[i].price:
                max_price.price = self.list_commodity[i].price
        return max_price




view = CommodityView()
while True:
    view.display()
    view.select_menu()


"""
    MVC : 软件架构
          Model : 数据模型
          View  : 负责处理界面逻辑
          Controller : 负责处理业务逻辑
"""








