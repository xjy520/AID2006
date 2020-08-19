class CommodityController:
    """
        逻辑控制器：负责处理业务逻辑(存储/查询)
    """

    def __init__(self):
        self.__list_commoditys = []
        self.__start_cid = 1001

    @property
    def list_commoditys(self):
        """
            商品列表
        """
        return self.__list_commoditys

    def add_commodity(self, commodity_target):
        """
            添加商品信息
        :param commodity_target:CommodityModel类型的商品
        """
        # 设置学生的编号(自增长)
        commodity_target.cid = self.__start_cid
        self.__start_cid += 1
        self.__list_commoditys.append(commodity_target)

    def remove_commodity(self, cid):
        """
            移除商品信息
        :param cid:int类型商品编号
        :return:是否移除成功
        """
        for commodity in self.__list_commoditys:
            if commodity.cid == cid:
                self.__list_commoditys.remove(commodity)
                return True
        return False

    def modify(self, commodity):
        """
            修改商品信息
        :param commodity:CommodityModel类型的商品
        :return:是否修改成功
        """
        for item in self.__list_commoditys:
            if item.cid == commodity.cid:
                item.name = commodity.name
                item.price = commodity.price
                return True
        return False

    def get__commodity_by_max_price(self):
        """
            获取价格最高的商品
        :return: 商品对象
        """
        max_value = self.__list_commoditys[0]
        for i in range(1, len(self.__list_commoditys)):
            if max_value.price < self.__list_commoditys[i].price:
                max_value = self.__list_commoditys[i]
        return max_value
