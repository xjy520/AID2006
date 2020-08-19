#   练习 : 将下列面向过程的代码变成面向对象代码
#   步骤 : 1.根据字典创建类
#         2.修改商品列表(字典 --> 自定义对象)
#         3.
# list_commodity_infos = [
#     {"cid": 1001, "name": "屠龙刀", "price": 10000},
#     {"cid": 1002, "name": "倚天剑", "price": 10000},
#     {"cid": 1003, "name": "金箍棒", "price": 52100},
#     {"cid": 1004, "name": "口罩", "price": 20},
#     {"cid": 1005, "name": "酒精", "price": 30},
# ]

class CommodityInfos:
    def __init__(self,cid,name,price):
        self.cid = cid
        self.name = name
        self.price = price

list_commodity_infos = [CommodityInfos(1001,"屠龙刀",10000),
                        CommodityInfos(1002,"倚天剑",10000),
                        CommodityInfos(1003,"金箍棒",52100),
                        CommodityInfos(1004,"口罩",20),
                        CommodityInfos(1005,"酒精",30)
                        ]
def print_commodity_infos():
    for commdity in list_commodity_infos:
        print("商品编号%d,商品名称%s,商品单价%d"%(commdity.cid,commdity.name,commdity.price))
print_commodity_infos()