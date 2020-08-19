import model
import bll


class CommodityView:
    """
        界面视图：负责处理界面逻辑(input/print)
    """

    def __init__(self):
        # 对象.实例变量 = 类名()
        self.__controller = bll.CommodityController()

    def __display_menu(self):
        print("1) 获取商品信息")
        print("2) 显示商品信息")
        print("3) 删除商品信息")
        print("4) 修改商品信息")
        print("5) 显示最贵商品信息")

    def __select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            # 对象.实例方法()
            self.__input_commodity()
        elif item == "2":
            self.__show_commoditys()
        elif item == "3":
            self.__delete_commodity()
        elif item == "4":
            self.__update_commodity()
        elif item == "5":
            self.__show_commodity_by_max_price()

    def __input_commodity(self):
        commodity = model.CommodityModel()
        commodity.name = input("请输入商品名称：")
        commodity.price = int(input("请输入商品单价："))
        # 对象.实例变量.实例方法(参数)
        self.__controller.add_commodity(commodity) #type:model.CommodityModel

    def __show_commoditys(self):
        for commodity in self.__controller.list_commoditys:
            print(commodity.__dict__)

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __delete_commodity(self):
        cid = int(input("请输入商品编号："))
        if self.__controller.remove_commodity(cid):
            print("删除成功")
        else:
            print("删除失败")

    def __update_commodity(self):
        commodity = model.CommodityModel()
        commodity.cid = input("请输入商品编号：")
        commodity.name = input("请输入商品名称：")
        commodity.price = input("请输入商品单价：")
        if self.__controller.modify(commodity):
            print("修改成功")
        else:
            print("需改失败")

    def __show_commodity_by_max_price(self):
        commodity = self.__controller.get__commodity_by_max_price()
        print(commodity.__dict__)


