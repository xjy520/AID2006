"""
    作用域
        程序格式
        适用性:
            在大范围(多个函数)内需要操作数据,使用全局变量
            在小范围(一个函数)内需要操作数据,使用局部变量
"""
# # ------------------全局变量---------------
# #   全局作用域:文件内
# b = 20
#
# # -------------------函数-----------------
# def func01():
#     #局部作用域:函数内
#     a=10
#     print(a)
#     print(b)
# # -------------------入口------------------




"""
    作用域
        在局部作用域修改全局变量
"""
# b = 20
#
# def func01():
#     # 声明全局变量,否则认为是局部变量
#     global b
#     b = 200
#
# func01()
# print(b)


# -------------------------全局变量-------------------------
dict_commodity_infos={
    1001:{"name":"屠龙刀","price":10000},
    1002:{"name":"倚天剑","price":10000},
    1003:{"name":"金箍棒","price":52100},
    1004:{"name":"口罩","price":20},
    1005:{"name":"酒精","price":30}
}

list_orders=[
    {"cid":1001,"count":1},
    {"cid":1002,"count":3},
    {"cid":1005,"count":2}
]

def get_commodity_info():
    for key,value in dict_commodity_infos.items():
        print_cmmodity(key,value)


def print_commoditys_by_lt_2w():
    for key,value in dict_commodity_infos.items():
        if dict_commodity_infos[key]["price"]>20000:
            print_cmmodity(key,value)


def print_cmmodity(key,value):
    print("商品编号%d,商品名称%s,商品单价%d" % (key, value["name"], value["price"]))
